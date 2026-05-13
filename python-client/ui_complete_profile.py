# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_CompleteProfile(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("CompleteProfileWindow")
        self.resize(1200, 1300)

        self.content_widget = QtWidgets.QWidget()
        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_main.setContentsMargins(50, 40, 50, 40)

        self.frame = QtWidgets.QFrame(self.content_widget)
        self.frame.setStyleSheet("background-color: white; border-radius: 30px;")
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(15)

        self.label_title = QtWidgets.QLabel("Complete Profile")
        self.label_title.setStyleSheet("font-size: 50px; font-weight: bold; color: #1e1b4b;")
        self.layout.addWidget(self.label_title)


        self.inputs = {}
        fields = [
            ("Last Name", "e.g. Popescu"),
            ("First Name", "e.g. Ion"),
            ("CNP", "13 digits required"),
            ("Phone Number", "07..."),
            ("County", "e.g. Constanta"),
            ("City", "e.g. Navodari")
        ]

        for label_text, placeholder in fields:
            lbl = QtWidgets.QLabel(label_text)
            lbl.setStyleSheet("font-size: 20px; font-weight: 600; color: #4b5563; margin-top: 5px;")
            self.layout.addWidget(lbl)

            line_edit = QtWidgets.QLineEdit()
            line_edit.setPlaceholderText(placeholder)
            line_edit.setMinimumHeight(65)
            line_edit.setStyleSheet("""
                background-color: #f3f4f6; border: 2px solid #d1d5db; 
                border-radius: 12px; padding: 10px 15px; font-size: 24px;
            """)
            if label_text == "CNP":
                line_edit.setMaxLength(13)

            self.layout.addWidget(line_edit)
            self.inputs[label_text] = line_edit

        self.layout.addStretch()

        self.btn_complete = QtWidgets.QPushButton("Save and Continue")
        self.btn_complete.setMinimumHeight(85)
        self.btn_complete.setStyleSheet(
            "QPushButton { background-color: #1e1b4b; color: white; font-size: 28px; font-weight: bold; border-radius: 20px; }")

        self.btn_skip = QtWidgets.QPushButton("Skip for now")
        self.btn_skip.setStyleSheet(
            "QPushButton { background-color: transparent; color: #64748b; font-size: 22px; text-decoration: underline; border: none; }")

        self.layout.addWidget(self.btn_complete)
        self.layout.addWidget(self.btn_skip)
        self.verticalLayout_main.addWidget(self.frame)