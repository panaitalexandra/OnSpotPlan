# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog


class Ui_Popup(QDialog):
    def __init__(self, message, title="Notification", parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setModal(True)
        self.message_text = message
        self.title_text = title
        self.setFixedSize(1100, 300)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ErrorPopupWindow")
        self.dialog_layout = QtWidgets.QVBoxLayout(self)
        self.dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { 
                background-color: #e4e4e4; 
                border-radius: 20px; 
            }
            * {
                font-family: 'Segoe UI', sans-serif;
                color: #1e1b4b;
            }
        """)

        self.dialog_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(45, 40, 45, 40)
        self.layout_main.setSpacing(20)

        self.lbl_title = QtWidgets.QLabel(self.title_text)
        self.lbl_title.setStyleSheet("""
            font-size: 36px; 
            font-weight: 850; \n            
            color: #311b4b;
            background: transparent;
        """)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_main.addWidget(self.lbl_title)

        self.lbl_message = QtWidgets.QLabel(self.message_text)
        self.lbl_message.setStyleSheet("""
            font-size: 28px; 
            color: #201c1c; 
            font-weight: 500;
            line-height: 140%;
            background: transparent;
        """)
        self.lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_message.setWordWrap(True)
        self.layout_main.addWidget(self.lbl_message)

        self.layout_main.addStretch()

        self.btn_ok = QtWidgets.QPushButton("OK")
        self.btn_ok.setMinimumHeight(65)
        self.btn_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ok.setStyleSheet("""
            QPushButton {
                background-color: #311b4b; 
                color: white; 
                font-size: 24px; 
                font-weight: bold; 
                border-radius: 20px; 
            }
            QPushButton:hover { background-color: #4e1c53; }
        """)
        self.btn_ok.clicked.connect(self.accept)
        self.layout_main.addWidget(self.btn_ok)