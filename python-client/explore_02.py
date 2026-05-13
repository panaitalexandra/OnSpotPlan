import random

from PyQt5 import QtWidgets, QtCore
from ui_explore import Ui_Explore
from ui_filter import Ui_Filter
from ui_open_profile import Ui_OpenProfile
from ui_event import Ui_Event
from ui_booking import Ui_BookingApp

class ExploreApp(Ui_Explore):
    def __init__(self, gateway, manager, email):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.active_client = None
        self.locatie_service = self.gateway.entry_point.getLocatieService()
        self.actualizeaza_locatii("Constanta")
        self.btn_filters.clicked.connect(self.selecteaza_oras)
        self.btn_profile.clicked.connect(self.deschide_profil)
        self.btn_logout.clicked.connect(self.handle_logout)
        self.seteaza_profil_implicit()

    def seteaza_profil_implicit(self):
        try:
            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            lista_clienti = manager_clienti.getLista()

            if not lista_clienti.isEmpty():
                self.active_client = lista_clienti.get(0)
                persoana = self.active_client.getPersoana()

                nume_complet = f"{persoana.getNume()} {persoana.getPrenume()}"
                self.lbl_active_user.setText(f"Current Profile: {nume_complet}")
                self.lbl_active_user.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 30px;")
            else:
                self.lbl_active_user.setText("No profile selected")

        except Exception as e:
            print(f"Err no profile selected: {e}")

    def deschide_profil(self):
        try:
            from auth_01 import ProfileSelectionApp
            self.selection_win = ProfileSelectionApp(self.gateway, self.manager, self.current_user_email)

            if self.selection_win.exec_() == QtWidgets.QDialog.Accepted:
                if hasattr(self.selection_win, 'selected_client'):
                    self.active_client = self.selection_win.selected_client
                    persoana = self.active_client.getPersoana()

                    nume_activ = f"{persoana.getNume()} {persoana.getPrenume()}"
                    self.lbl_active_user.setText(f"Current Profile: {nume_activ}")
                    self.lbl_active_user.setStyleSheet("color: #38bdf8; font-weight: bold; font-size: 30px;")
        except Exception as e:
            print(f"Err: {e}")

    def handle_logout(self):
        # Cerem confirmare (Opțional, dar recomandat pentru UX)
        reply = QtWidgets.QMessageBox.question(
            self, 'Logout', "Are you sure you want to log out?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            from auth_01 import LoginApp

            self.login_win = LoginApp(self.gateway, self.manager)

            self.login_win.show()

            self.close()

    def deschide_rezervare(self, nume_locatie):
        try:
            # Obținem managerul prin gateway
            manager_ev = self.gateway.jvm.ManagerEvents.getInstance()

            # Apelăm metoda care acum există în ManagerEvenimente
            descriere = manager_ev.getDescriereLocatie(nume_locatie)

            date_eveniment = {
                'nume': nume_locatie,
                'descriere': descriere,
                'regiune': self.oras_actual,
                'imagine': "resources/ev1.jpg"  # Sau logica ta de poze
            }

            self.detail_win = Ui_Event(self.gateway, date_eveniment, self.active_client)
            self.detail_win.show()
        except Exception as e:
            print(f"Eroare Py4J: {e}")

    def selecteaza_oras(self):
        dialog = Ui_Filter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            oras = dialog.get_selection()
            if oras:
                self.actualizeaza_locatii(oras)

    def actualizeaza_locatii(self, judet_selectat):
        try:
            self.oras_actual = judet_selectat

            # CURĂȚARE SIGURĂ: Ștergem cardurile vechi fără să atingem layout-ul principal
            # Presupunem că layout-ul ferestrei tale are o zonă unde pui cardurile.
            # O metodă sigură este să iterăm invers
            for i in reversed(range(self.main_layout.count())):
                item = self.main_layout.itemAt(i)
                widget = item.widget()
                # Ștergem doar widget-urile de tip QFrame (cardurile noastre)
                if isinstance(widget, QtWidgets.QFrame) and widget.objectName() == "EventCard":
                    widget.setParent(None)
                    widget.deleteLater()

            locatii = self.locatie_service.getLocatiiDupaJudet(judet_selectat)

            for nume in locatii:
                card = self.creeaza_widget_card(nume)
                self.main_layout.addWidget(card)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Eroare", f"Could not load locations: {e}")

    def creeaza_widget_card(self, nume_locatie):

        colors = [
            "#1e1b4b", "#312e81", "#4338ca", "#581c87",
            "#701a75", "#86198f", "#1e3a8a", "#0f172a"
        ]
        card_frame = QtWidgets.QFrame()
        card_frame.setObjectName("EventCard")
        card_frame.setMinimumHeight(250)
        card_frame.setStyleSheet(f"background-color: {random.choice(colors)}; border-radius: 40px;")

        layout = QtWidgets.QVBoxLayout(card_frame)

        lbl_nume = QtWidgets.QLabel(nume_locatie)
        lbl_nume.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")

        btn_book = QtWidgets.QPushButton("Check Event")
        btn_book.setFixedSize(280, 50)
        btn_book.setStyleSheet("""
            QPushButton {
                background-color: #3d7068; 
                color: white; 
                font-size: 22px;             
                font-weight: bold;
                border-radius: 25px;         
                border: none;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #4d8a7f;  
            }
        """)
        btn_book.clicked.connect(lambda checked, name=nume_locatie: self.deschide_rezervare(name))
        layout.addWidget(lbl_nume)
        layout.addStretch()
        layout.addWidget(btn_book, 0, QtCore.Qt.AlignRight)

        return card_frame


class ProfileApp(Ui_OpenProfile):
    def __init__(self, gateway, manager, email, index=0):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.profile_index = index
        self.incarca_date_profil()

        self.btn_modify.clicked.connect(self.deschide_modificare)
        self.btn_back_explore.clicked.connect(self.close)
        if hasattr(self, 'btn_back_explore'):
            self.btn_close.clicked.connect(self.close)

    def incarca_date_profil(self):
        try:
            manager = self.gateway.getManagerClienti(self.current_user_email)
            lista = manager.getLista()

            if not lista.isEmpty() and self.profile_index < lista.size():
                profil = lista.get(self.profile_index)
                p = profil.getPersoana()

                self.info_labels["Full Name"].setText(f"{p.getNume()} {p.getPrenume()}")

                if "CNP" in self.info_labels:
                    self.info_labels["CNP"].setText(p.getCNP())

                self.info_labels["Phone Number"].setText(p.getTelefon())

                self.info_labels["Region"].setText(p.getRegion())

                if "City" in self.info_labels:
                    self.info_labels["City"].setText(p.getLocalitate())

        except Exception as e:
            print(f"Err could not upload: {e}")

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
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection", "Select profile from tabel!")
            return

        self.accept()