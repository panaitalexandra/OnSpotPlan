from PyQt5 import QtWidgets, QtCore, QtGui
from ui_log_in import Ui_Authentification
from ui_sign_up import Ui_Register
from ui_complete_profile import Ui_CompleteProfile
from ui_profile_selection import Ui_ProfileSelection

class RegisterApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager):
        super(RegisterApp, self).__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.ui.pushButton_register.clicked.connect(self.handle_signup)
        self.ui.label_back_to_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_back_to_login.mousePressEvent = self.switch_to_login

    def handle_signup(self):
        email = self.ui.lineEdit_email.text()
        password = self.ui.lineEdit_passwd.text()
        confirmation = self.ui.lineEdit_confirm_passwd.text()

        if password != confirmation:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        try:
            if not self.manager.isEmailValid(email):
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid email format!")
                return

            if not self.manager.isParolaValida(password):
                QtWidgets.QMessageBox.warning(self, "Error", "Password does not meet security requirements!")
                return

            new_user = self.manager.inregistreazaUtilizator(email, password)

            if new_user is not None:
                QtWidgets.QMessageBox.information(self, "Success", "Account created successfully!")
                self.complete_win = CompleteProfileApp(self.gateway, self.manager, email)
                if self.complete_win.exec_() == QtWidgets.QDialog.Accepted:
                    self.accept()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Registration failed!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Communication Error", f"Details: {e}")

    def switch_to_login(self, event):
        self.login_window = LoginApp(self.gateway, self.manager)
        self.login_window.show()
        self.close()


class LoginApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager):
        super(LoginApp, self).__init__()
        self.ui = Ui_Authentification()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.ui.pushButton_login.clicked.connect(self.handle_login)
        self.ui.label_signin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_signin.mousePressEvent = self.switch_to_signup

    def handle_login(self):
        email = self.ui.lineEdit_email.text()
        password = self.ui.lineEdit_passwd.text()

        try:
            user = self.manager.getUtilizator(email, password)

            if user is not None:
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid email or password!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Java communication failed: {e}")

    def switch_to_signup(self, event):
        self.signup_window = RegisterApp(self.gateway, self.manager)
        self.signup_window.show()
        self.close()


class ProfileSelectionApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager, email):
        super(ProfileSelectionApp, self).__init__()
        self.ui = Ui_ProfileSelection()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email

        self.ui.btn_add.clicked.connect(self.handle_add_profile)
        self.ui.btn_view.clicked.connect(self.handle_view_details)
        self.ui.btn_select.clicked.connect(self.handle_select)

        self.load_profiles()

    def handle_select(self):
        selected_row = self.ui.table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection", "Te rugăm să selectezi un profil!")
            return

        manager = self.gateway.getManagerClienti(self.current_user_email)
        lista = manager.getLista()

        self.selected_client = lista.get(selected_row)

        self.accept()

    def load_profiles(self):
        """Populează tabelul folosind ManagerClienti.getLista()[cite: 14, 15]"""
        manager = self.gateway.getManagerClienti(self.current_user_email)
        lista_beneficiari = manager.getLista()

        self.ui.table.setRowCount(0)
        for i in range(lista_beneficiari.size()):
            client = lista_beneficiari.get(i)
            persoana = client.getPersoana()

            self.ui.table.insertRow(i)
            self.ui.table.setItem(i, 0, QtWidgets.QTableWidgetItem(persoana.getNume()))
            self.ui.table.setItem(i, 1, QtWidgets.QTableWidgetItem(persoana.getPrenume()))
            self.ui.table.setItem(i, 2, QtWidgets.QTableWidgetItem(persoana.getCNP()))

    def handle_add_profile(self):
        manager = self.gateway.getManagerClienti(self.current_user_email)
        if manager.getLista().size() >= 10:
            QtWidgets.QMessageBox.warning(self, "Limit Reached", "You can only have up to 10 profiles.")
            return

        from auth_01 import CompleteProfileApp
        add_win = CompleteProfileApp(self.gateway, manager, self.current_user_email)
        if add_win.exec_() == QtWidgets.QDialog.Accepted:
            self.load_profiles()

    def handle_view_details(self):
        selected_row = self.ui.table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection", "Te rugăm să selectezi un beneficiar mai întâi!")
            return

        from explore_02 import ProfileApp

        self.details_win = ProfileApp(
            self.gateway,
            self.manager,
            self.current_user_email,
            index=selected_row
        )

        self.details_win.exec_()
        self.load_profiles()

class CompleteProfileApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager,email, profile_index=None):
        super(CompleteProfileApp, self).__init__()
        self.ui = Ui_CompleteProfile()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.profile_index = profile_index
        self.ui.btn_complete.clicked.connect(self.handle_completion)
        self.ui.btn_skip.clicked.connect(self.accept)

    def handle_completion(self):
        try:
            data = {k: v.text().strip() for k, v in self.ui.inputs.items()}

            if not all(data.values()):
                QtWidgets.QMessageBox.warning(self, "Eroare", "Toate câmpurile sunt obligatorii!")
                return

            if len(data["CNP"]) != 13 or not data["CNP"].isdigit():
                QtWidgets.QMessageBox.warning(self, "Eroare", "CNP-ul trebuie să conțină exact 13 cifre!")
                return

            client_java = self.gateway.jvm.Client(
                data["Last Name"],
                data["First Name"],
                data["CNP"],
                "N/A",
                "N/A",
                data["County"],
                data["City"],
                data["Phone Number"]
            )

            varsta = client_java.getVarsta()
            if varsta < 0:
                QtWidgets.QMessageBox.critical(self, "Eroare", "Sistemul Java a raportat un CNP invalid!")
                return

            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            if self.profile_index is not None:
                manager_clienti.actualizeazaClient(self.profile_index, client_java)
            else:
                manager_clienti.adaugaClient(client_java)
            self.accept()

        except KeyError as e:
            QtWidgets.QMessageBox.critical(self, "Eroare UI", f"Lipsește câmpul de intrare: {str(e)}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Crash", f"Eroare de compatibilitate: {str(e)}")

    def handle_skip(self):
        self.open_explore()

    def open_explore(self):
        from explore_02 import ExploreApp
        self.dashboard = ExploreApp(self.gateway, self.manager, self.current_user_email)
        self.dashboard.show()
        self.accept()