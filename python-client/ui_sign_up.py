# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_Register(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("RegisterWindow")
        self.resize(1200, 1300)

        self.content_widget = QtWidgets.QWidget()
        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame = QtWidgets.QFrame(self.content_widget)
        self.frame.setStyleSheet("background-color: white;\n"
                                 "border-radius: 20px;\n"
                                 "border: 1px solid #e0e0e0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")

        self.header_layout = QtWidgets.QVBoxLayout()
        self.header_layout.setSpacing(15)
        self.header_layout.setObjectName("header_layout")

        self.label_eventHub = QtWidgets.QLabel(self.frame)
        self.label_eventHub.setStyleSheet("color: #1e1b4b;\n"
                                          "    font-size: 80px;\n"
                                          "    font-weight: bold;\n"
                                          "    font-family: \"Segoe UI\", sans-serif;\n"
                                          "    background: transparent;\n"
                                          "    border: none")
        self.label_eventHub.setObjectName("label_eventHub")
        self.header_layout.addWidget(self.label_eventHub)

        self.label_welcome = QtWidgets.QLabel(self.frame)
        self.label_welcome.setStyleSheet("color: #0f172a;\n"
                                         "    font-size: 55px;\n"
                                         "    font-weight: bold;\n"
                                         "    background: transparent;\n"
                                         "    border: none")
        self.label_welcome.setObjectName("label_welcome")
        self.header_layout.addWidget(self.label_welcome)

        self.label_details = QtWidgets.QLabel(self.frame)
        self.label_details.setStyleSheet("color: #64748b;\n"
                                         "    font-size: 28px;\n"
                                         "    font-weight: 400;\n"
                                         "    background: transparent;\n"
                                         "    border: none")
        self.label_details.setObjectName("label_details")
        self.header_layout.addWidget(self.label_details)

        self.verticalLayout.addLayout(self.header_layout)

        self.input_Layout = QtWidgets.QVBoxLayout()
        self.input_Layout.setSpacing(20)
        self.input_Layout.setObjectName("input_Layout")

        self.label_email = QtWidgets.QLabel(self.frame)
        self.label_email.setStyleSheet("color: #4b5563; font-size: 26px; font-weight: 600; background: transparent; border: none")
        self.label_email.setObjectName("label_email")
        self.input_Layout.addWidget(self.label_email)

        self.lineEdit_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_email.setMinimumHeight(80)
        self.lineEdit_email.setStyleSheet("background-color: #f3f4f6; border: 2px solid #d1d5db; border-radius: 12px; padding: 15px; color: #1f2937; font-size: 28px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.input_Layout.addWidget(self.lineEdit_email)

        self.label_passwd = QtWidgets.QLabel(self.frame)
        self.label_passwd.setStyleSheet("color: #4b5563; font-size: 26px; font-weight: 600; background: transparent; border: none")
        self.label_passwd.setObjectName("label_passwd")
        self.input_Layout.addWidget(self.label_passwd)

        self.lineEdit_passwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_passwd.setMinimumHeight(80)
        self.lineEdit_passwd.setStyleSheet("background-color: #f3f4f6; border: 2px solid #d1d5db; border-radius: 12px; padding: 15px; color: #1f2937; font-size: 28px;")
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.input_Layout.addWidget(self.lineEdit_passwd)

        self.label_confirm_passwd = QtWidgets.QLabel(self.frame)
        self.label_confirm_passwd.setStyleSheet("color: #4b5563; font-size: 26px; font-weight: 600; background: transparent; border: none")
        self.label_confirm_passwd.setObjectName("label_confirm_passwd")
        self.input_Layout.addWidget(self.label_confirm_passwd)

        self.lineEdit_confirm_passwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_confirm_passwd.setMinimumHeight(80)
        self.lineEdit_confirm_passwd.setStyleSheet("background-color: #f3f4f6; border: 2px solid #d1d5db; border-radius: 12px; padding: 15px; color: #1f2937; font-size: 28px;")
        self.lineEdit_confirm_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_passwd.setObjectName("lineEdit_confirm_passwd")
        self.input_Layout.addWidget(self.lineEdit_confirm_passwd)
        self.hints_layout = QtWidgets.QVBoxLayout()
        self.hints_layout.setSpacing(5)

        self.password_hints = {
            "length": QtWidgets.QLabel("● Minim 8 caractere"),
            "upper": QtWidgets.QLabel("● Cel puțin o majusculă"),
            "digit": QtWidgets.QLabel("● Cel puțin o cifră"),
            "special": QtWidgets.QLabel("● Un caracter special (!, #, $, %, ^, *)")
        }

        for hint in self.password_hints.values():
            hint.setStyleSheet("color: #94a3b8; font-size: 18px;")  # Gri inițial
            self.hints_layout.addWidget(hint)

        self.verticalLayout.addLayout(self.input_Layout)
        self.verticalLayout.addLayout(self.hints_layout)


        self.footer_layout = QtWidgets.QVBoxLayout()
        self.footer_layout.setContentsMargins(-1, 40, -1, -1)
        self.footer_layout.setSpacing(25)
        self.footer_layout.setObjectName("footer_layout")

        self.pushButton_register = QtWidgets.QPushButton(self.frame)
        self.pushButton_register.setMinimumHeight(90)
        self.pushButton_register.setStyleSheet("QPushButton {\n"
                                            "    background-color: #1e1b4b;\n"
                                            "    color: white;\n"
                                            "    font-size: 32px;\n"
                                            "    font-weight: bold;\n"
                                            "    border-radius: 15px;\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #2e2a70;\n"
                                            "}")
        self.pushButton_register.setObjectName("pushButton_register")
        self.footer_layout.addWidget(self.pushButton_register)

        self.label_back_to_login = QtWidgets.QLabel(self.frame)
        self.label_back_to_login.setStyleSheet("color: #4b5563; font-size: 24px; background: transparent; border: none;")
        self.label_back_to_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_back_to_login.setObjectName("label_back_to_login")
        self.footer_layout.addWidget(self.label_back_to_login)

        self.verticalLayout.addLayout(self.footer_layout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "EventHub - Create Account"))
        self.label_eventHub.setText(_translate("Dialog", "EventHub"))
        self.label_welcome.setText(_translate("Dialog", "Join Us"))
        self.label_details.setText(_translate("Dialog", "Please enter your details to create a new account"))
        self.label_email.setText(_translate("Dialog", "Email Address"))
        self.label_passwd.setText(_translate("Dialog", "Password"))
        self.label_confirm_passwd.setText(_translate("Dialog", "Confirm Password"))
        self.pushButton_register.setText(_translate("Dialog", "Sign Up"))
        self.label_back_to_login.setText(_translate("Dialog", "Already have an account? Log in"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Register()
    ui.show()
    sys.exit(app.exec_())