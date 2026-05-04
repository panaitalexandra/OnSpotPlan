import random
from PyQt5 import QtWidgets, QtCore
from ui_explore import Ui_Explore
from ui_filter import Ui_Filter
from ui_open_profile import Ui_OpenProfile

class ExploreApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager, email):
        super(ExploreApp, self).__init__()
        self.ui = Ui_Explore()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.locatie_service = self.gateway.entry_point.getLocatieService()
        self.actualizeaza_locatii("Constanta")
        self.ui.btn_filters.clicked.connect(self.selecteaza_oras)
        self.ui.btn_profile.clicked.connect(self.deschide_profil)

    def deschide_profil(self):
        # Deschidem fereastra de profil ca dialog modal[cite: 2]
        self.profile_win = ProfileApp(self.gateway, self.manager, self.current_user_email)
        self.profile_win.exec_()

    def selecteaza_oras(self):
        dialog = Ui_Filter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            oras = dialog.get_selection()
            if oras:
                self.actualizeaza_locatii(oras)

    def actualizeaza_locatii(self, judet_selectat):
        try:
            while self.ui.main_layout.count() > 5:  # Păstrăm header-ul și filtrele
                item = self.ui.main_layout.takeAt(5)
                if item.widget():
                    item.widget().deleteLater()

            locatii = self.locatie_service.getLocatiiDupaJudet(judet_selectat)

            for nume in locatii:
                card = self.creeaza_widget_card(nume)
                self.ui.main_layout.addWidget(card)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Eroare", f"Nu am putut încărca locațiile: {e}")

    def creeaza_widget_card(self, nume_locatie):

        colors = [
            "#1e1b4b", "#312e81", "#4338ca", "#581c87",
            "#701a75", "#86198f", "#1e3a8a", "#0f172a"
        ]
        card_frame = QtWidgets.QFrame()
        card_frame.setMinimumHeight(250)
        card_frame.setStyleSheet(f"background-color: {random.choice(colors)}; border-radius: 40px;")

        layout = QtWidgets.QVBoxLayout(card_frame)

        lbl_nume = QtWidgets.QLabel(nume_locatie)
        lbl_nume.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")

        btn_book = QtWidgets.QPushButton("Book Now")
        btn_book.setFixedSize(280, 50)
        btn_book.setStyleSheet("""
            QPushButton {
                background-color: #3d7068; 
                color: white; 
                font-size: 22px;             /* Dimensiune mai echilibrată */
                font-weight: bold;
                border-radius: 25px;         /* Aceasta oferă rotunjirea[cite: 4, 7] */
                border: none;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #4d8a7f;   /* Nuanță mai deschisă la trecerea mouse-ului */
            }
        """)
        btn_book.clicked.connect(lambda: self.deschide_rezervare(nume_locatie))

        layout.addWidget(lbl_nume)
        layout.addStretch()
        layout.addWidget(btn_book, 0, QtCore.Qt.AlignRight)

        return card_frame

    def deschide_rezervare(self, nume_locatie):
        QtWidgets.QMessageBox.information(self, "Rezervare", f"Ai ales să rezervi la: {nume_locatie}")


class ProfileApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager, email):
        super(ProfileApp, self).__init__()
        self.ui = Ui_OpenProfile()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        # Încărcăm datele utilizatorului curent din Java[cite: 1, 8]
        self.incarca_date_profil()

        self.ui.btn_modify.clicked.connect(self.deschide_modificare)
        self.ui.btn_close.clicked.connect(self.close)

    def incarca_date_profil(self):
        try:
            # Cerem managerul pentru user-ul logat
            manager = self.gateway.getManagerClienti(self.current_user_email)
            lista = manager.getLista()  # Returnează ArrayList<Client>[cite: 10]

            if not lista.isEmpty():
                profil = lista.get(0)  # Luăm primul set de date salvat[cite: 10]
                self.ui.info_labels["Full Name"].setText(profil.getPersoana().getNume())
                self.ui.info_labels["Phone Number"].setText(profil.getTelefon())
                # ... restul câmpurilor
        except Exception as e:
            print(f"Eroare la încărcare: {e}")

    def deschide_modificare(self):
        # Importăm aici pentru a evita erorile de import circular[cite: 2]
        from auth_01 import CompleteProfileApp

        # Deschidem fereastra de editare
        self.edit_win = CompleteProfileApp(self.gateway, self.manager, self.current_user_email)

        # Dacă utilizatorul a apăsat "Complete" în fereastra de editare
        if self.edit_win.exec_() == QtWidgets.QDialog.Accepted:
            # Reîmprospătăm datele afișate pe ecranul curent[cite: 1, 2]
            self.incarca_date_profil()