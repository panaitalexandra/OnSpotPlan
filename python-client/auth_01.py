from PyQt5 import QtWidgets, QtCore, QtGui
from ui_log_in import Ui_Authentification
from ui_sign_up import Ui_Register

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
                self.switch_to_login(None)
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

