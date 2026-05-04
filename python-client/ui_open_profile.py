# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenProfile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 1100)
        Dialog.setStyleSheet("background-color: #121212;")

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: white; border-radius: 30px;")
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.layout.setSpacing(30)

        # Header
        self.label_title = QtWidgets.QLabel("My Profile")
        self.label_title.setStyleSheet("font-size: 55px; font-weight: bold; color: #1e1b4b; margin-bottom: 10px;")
        self.layout.addWidget(self.label_title)

        # Secțiune Afișare Date[cite: 6, 7]
        self.info_labels = {}
        fields = ["Full Name", "Phone Number", "Address", "City"]

        for field in fields:
            lbl_title = QtWidgets.QLabel(field)
            lbl_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #94a3b8; margin-top: 10px;")
            self.layout.addWidget(lbl_title)

            lbl_value = QtWidgets.QLabel("Not provided")
            lbl_value.setStyleSheet(
                "font-size: 26px; color: #1e1b4b; padding: 10px 0px; border-bottom: 1px solid #f1f5f9;")
            self.layout.addWidget(lbl_value)
            self.info_labels[field] = lbl_value

        self.layout.addStretch()  # Împinge butoanele în jos[cite: 4]

        # --- Zona de butoane (Un singur set de butoane pentru tot) ---
        self.btn_modify = QtWidgets.QPushButton("Modify Profile Details")
        self.btn_modify.setMinimumHeight(85)
        self.btn_modify.setStyleSheet("""
            QPushButton { 
                background-color: #1e1b4b; color: white; font-size: 26px; 
                font-weight: bold; border-radius: 20px; 
            } 
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.layout.addWidget(self.btn_modify)

        self.btn_close = QtWidgets.QPushButton("Back to Explore")
        self.btn_close.setMinimumHeight(70)
        self.btn_close.setStyleSheet("""
            QPushButton { 
                background-color: transparent; color: #64748b; font-size: 22px; 
                text-decoration: underline; border: none;
            } 
            QPushButton:hover { color: #1e1b4b; }
        """)
        self.layout.addWidget(self.btn_close)

        self.verticalLayout.addWidget(self.frame)