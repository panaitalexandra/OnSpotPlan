import random
from operator import index

from PyQt5 import QtWidgets, QtCore
from ui_explore import Ui_Explore
from ui_filter import Ui_Filter
from ui_open_profile import Ui_OpenProfile
from ui_booking import Ui_BookingApp

class ExploreApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager, email):
        super(ExploreApp, self).__init__()
        self.ui = Ui_Explore()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.active_client = None
        self.locatie_service = self.gateway.entry_point.getLocatieService()
        self.actualizeaza_locatii("Constanta")
        self.ui.btn_filters.clicked.connect(self.selecteaza_oras)
        self.ui.btn_profile.clicked.connect(self.deschide_profil)
        self.seteaza_profil_implicit()

    def seteaza_profil_implicit(self):
        try:
            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            lista_clienti = manager_clienti.getLista()

            if not lista_clienti.isEmpty():
                self.active_client = lista_clienti.get(0)  # <--- ACEASTA ESTE LINIA CRITICĂ
                persoana = self.active_client.getPersoana()  # [cite: 6]

                nume_complet = f"{persoana.getNume()} {persoana.getPrenume()}"
                self.ui.lbl_active_user.setText(f"Current Profile: {nume_complet}")
            else:
                self.ui.lbl_active_user.setText("No profile selected")

        except Exception as e:
            print(f"Eroare la setarea profilului implicit: {e}")

    def deschide_profil(self):
        try:
            from auth_01 import ProfileSelectionApp
            self.selection_win = ProfileSelectionApp(self.gateway, self.manager, self.current_user_email)

            if self.selection_win.exec_() == QtWidgets.QDialog.Accepted:
                if hasattr(self.selection_win, 'selected_client'):
                    self.active_client = self.selection_win.selected_client  # <--- ACEASTA ESTE LINIA CRITICĂ
                    persoana = self.active_client.getPersoana()  # [cite: 6]

                    nume_activ = f"{persoana.getNume()} {persoana.getPrenume()}"
                    self.ui.lbl_active_user.setText(f"Current Profile: {nume_activ}")
                    self.ui.lbl_active_user.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 16px;")
        except Exception as e:
            print(f"Eroare la actualizare label: {e}")

    def deschide_rezervare(self, nume_locatie):
        """Lanseaază fereastra de calendar pentru locația selectată."""
        if self.active_client is None:
            QtWidgets.QMessageBox.warning(self, "Selection Required",
                                          "Please select or add a profile first!")
            return

        # Deschidem UI-ul de Booking creat anterior[cite: 6, 8]
        self.booking_win = Ui_BookingApp(self.gateway, nume_locatie, self.active_client)
        self.booking_win.exec_()

    def selecteaza_oras(self):
        dialog = Ui_Filter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            oras = dialog.get_selection()
            if oras:
                self.actualizeaza_locatii(oras)

    def actualizeaza_locatii(self, judet_selectat):
        try:
            while self.ui.main_layout.count() > 6:
                item = self.ui.main_layout.takeAt(6)
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
        if self.active_client is None:
            QtWidgets.QMessageBox.warning(self, "Atentie", "Selectati un profil inainte de rezervare!")
            return

        self.booking_win = Ui_BookingApp(self.gateway, nume_locatie, self.active_client)
        self.booking_win.exec_()

class ProfileApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager, email, index=0):
        super(ProfileApp, self).__init__()
        self.ui = Ui_OpenProfile()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.profile_index = index
        self.incarca_date_profil()

        self.ui.btn_modify.clicked.connect(self.deschide_modificare)
        self.ui.btn_close.clicked.connect(self.close)

    def incarca_date_profil(self):
        try:
            manager = self.gateway.getManagerClienti(self.current_user_email)
            lista = manager.getLista()

            if not lista.isEmpty() and self.profile_index < lista.size():
                profil = lista.get(self.profile_index)
                p = profil.getPersoana()

                self.ui.info_labels["Full Name"].setText(f"{p.getNume()} {p.getPrenume()}")

                if "CNP" in self.ui.info_labels:
                    self.ui.info_labels["CNP"].setText(p.getCNP())

                self.ui.info_labels["Phone Number"].setText(p.getTelefon())

                self.ui.info_labels["Region"].setText(p.getJudet())

                if "City" in self.ui.info_labels:
                    self.ui.info_labels["City"].setText(p.getLocalitate())

        except Exception as e:
            print(f"Eroare la popularea datelor în ProfileApp: {e}")

    def deschide_modificare(self):
        from auth_01 import CompleteProfileApp

        self.edit_win = CompleteProfileApp(
            self.gateway,
            self.manager,
            self.current_user_email,
            profile_index=self.profile_index
        )

        if self.edit_win.exec_() == QtWidgets.QDialog.Accepted:
            self.incarca_date_profil()

    def handle_select(self):
        selected_row = self.ui.table.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection", "Te rugăm să selectezi un profil din tabel!")
            return

        self.accept()