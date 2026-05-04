from PyQt5 import QtWidgets, QtCore, QtGui
from ui_log_in import Ui_Authentification
from ui_sign_up import Ui_Register
from ui_complete_profile import Ui_CompleteProfile

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
                    self.accept()  # Închide Register cu succes pentru a intra în Explore
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


class CompleteProfileApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager,email):
        super(CompleteProfileApp, self).__init__()
        self.ui = Ui_CompleteProfile()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        # Ambele butoane închid dialogul cu "Accepted" pentru a merge la Explore[cite: 1, 3]
        self.ui.btn_complete.clicked.connect(self.handle_completion)
        self.ui.btn_skip.clicked.connect(self.accept)

    def handle_completion(self):
        try:
            # 1. Colectăm datele din UI
            nume = self.ui.inputs["Last Name"].text()
            prenume = self.ui.inputs["First Name"].text()
            cnp = self.ui.inputs["CNP"].text()
            tel = self.ui.inputs["Phone Number"].text()
            judet = self.ui.inputs["County"].text()
            oras = self.ui.inputs["City"].text()

            # 2. Creăm obiectul Client în Java (folosind constructorul cu 8 parametri)
            new_client = self.gateway.jvm.Client(nume, prenume, cnp, "N/A", "N/A", judet, oras, tel)

            # 3. Salvăm folosind ManagerClienti
            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            manager_clienti.adaugaClient(new_client)

            # --- SOLUȚIA: ---
            # Nu mai apelăm self.open_explore()!
            # Apelăm doar self.accept() pentru a închide fereastra de editare.
            self.accept()

        except Exception as e:
            print(f"Failed to save profile: {e}")

    def handle_skip(self):
        self.open_explore()

    def open_explore(self):
        from explore_02 import ExploreApp

        # Creăm și afișăm fereastra Explore[cite: 2]
        self.dashboard = ExploreApp(self.gateway, self.manager)
        self.dashboard.show()

        # Închidem dialogul actual, dar Explore va rămâne deschis
        self.accept()