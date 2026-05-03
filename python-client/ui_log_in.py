# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authentification(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 1250)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame = QtWidgets.QFrame(Dialog)
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

        # --- HEADER SECTION ---
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
                                         "    font-size: 55px;\n"  # MULT MAI MARE
                                         "    font-weight: bold;\n"
                                         "    background: transparent;\n"
                                         "    border: none")
        self.label_welcome.setObjectName("label_welcome")
        self.header_layout.addWidget(self.label_welcome)

        self.label_details = QtWidgets.QLabel(self.frame)
        self.label_details.setStyleSheet("color: #64748b;\n"
                                         "    font-size: 28px;\n"  # MULT MAI MARE
                                         "    font-weight: 400;\n"
                                         "    background: transparent;\n"
                                         "    border: none")
        self.label_details.setObjectName("label_details")
        self.header_layout.addWidget(self.label_details)

        self.verticalLayout.addLayout(self.header_layout)

        # --- INPUT SECTION ---
        self.input_Layout = QtWidgets.QVBoxLayout()
        self.input_Layout.setSpacing(20)
        self.input_Layout.setObjectName("input_Layout")

        # Email
        self.label_email = QtWidgets.QLabel(self.frame)
        self.label_email.setStyleSheet("color: #4b5563;\n"
                                       "    font-size: 26px;\n"  # MULT MAI MARE
                                       "    font-weight: 600;\n"
                                       "    background: transparent;\n"
                                       "    border: none")
        self.label_email.setObjectName("label_email")
        self.input_Layout.addWidget(self.label_email)

        self.lineEdit_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_email.setMinimumHeight(80)  # Caseta de text mai înaltă
        self.lineEdit_email.setStyleSheet("background-color: #f3f4f6;\n"
                                          "    border: 2px solid #d1d5db;\n"
                                          "    border-radius: 12px;\n"
                                          "    padding: 15px;\n"
                                          "    color: #1f2937;\n"
                                          "    font-size: 28px;")  # Textul introdus e imens
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.input_Layout.addWidget(self.lineEdit_email)

        # Parola
        self.label_passwd = QtWidgets.QLabel(self.frame)
        self.label_passwd.setStyleSheet("color: #4b5563;\n"
                                        "    font-size: 26px;\n"
                                        "    font-weight: 600;\n"
                                        "    background: transparent;\n"
                                        "    border: none")
        self.label_passwd.setObjectName("label_passwd")
        self.input_Layout.addWidget(self.label_passwd)

        self.lineEdit_passwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_passwd.setMinimumHeight(80)
        self.lineEdit_passwd.setStyleSheet("background-color: #f3f4f6;\n"
                                           "    border: 2px solid #d1d5db;\n"
                                           "    border-radius: 12px;\n"
                                           "    padding: 15px;\n"
                                           "    color: #1f2937;\n"
                                           "    font-size: 28px;")
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.input_Layout.addWidget(self.lineEdit_passwd)

        # Checkbox
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setStyleSheet("QCheckBox {\n"
                                    "    color: #4b5563;\n"
                                    "    font-size: 24px;\n"  # MULT MAI MARE
                                    "    spacing: 15px;\n"
                                    "    border: none;\n"
                                    "}\n"
                                    "QCheckBox::indicator {\n"
                                    "    width: 20px;\n"  # Pătrățelul bifabil este acum mare
                                    "    height: 20px;\n"
                                    "}")
        self.checkBox.setObjectName("checkBox")
        self.input_Layout.addWidget(self.checkBox)

        self.verticalLayout.addLayout(self.input_Layout)

        # --- FOOTER SECTION ---
        self.footer_layout = QtWidgets.QVBoxLayout()
        self.footer_layout.setContentsMargins(-1, 40, -1, -1)
        self.footer_layout.setSpacing(25)
        self.footer_layout.setObjectName("footer_layout")

        self.pushButton_login = QtWidgets.QPushButton(self.frame)
        self.pushButton_login.setMinimumHeight(90)  # Buton masiv
        self.pushButton_login.setStyleSheet("QPushButton {\n"
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
        self.pushButton_login.setObjectName("pushButton_login")
        self.footer_layout.addWidget(self.pushButton_login)

        self.label_signin = QtWidgets.QLabel(self.frame)
        self.label_signin.setStyleSheet("color: #4b5563;\n"
                                        "    font-size: 24px;\n"
                                        "    background: transparent;\n"
                                        "    border: none;")
        self.label_signin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signin.setObjectName("label_signin")
        self.footer_layout.addWidget(self.label_signin)

        self.verticalLayout.addLayout(self.footer_layout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EventHub Login"))
        self.label_eventHub.setText(_translate("Dialog", "EventHub"))
        self.label_welcome.setText(_translate("Dialog", "Welcome"))
        self.label_details.setText(_translate("Dialog", "Please enter your details to log in"))
        self.label_email.setText(_translate("Dialog", "Email Address"))
        self.label_passwd.setText(_translate("Dialog", "Password"))
        self.checkBox.setText(_translate("Dialog", "Remember me for 30 days"))
        self.pushButton_login.setText(_translate("Dialog", "Log in"))
        self.label_signin.setText(_translate("Dialog", "Don't have an account? Sign up"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())