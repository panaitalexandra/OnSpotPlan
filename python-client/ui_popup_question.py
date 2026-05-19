# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog


class Ui_PopupQuestion(QDialog):
    def __init__(self, message, title="Confirm Action", parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setModal(True)

        self.message_text = message
        self.title_text = title
        self.setFixedSize(1100, 350)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("QuestionPopupWindow")

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
                color: #261947;
            }
        """)

        self.dialog_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(45, 40, 45, 40)
        self.layout_main.setSpacing(20)

        self.lbl_title = QtWidgets.QLabel(self.title_text)
        self.lbl_title.setStyleSheet("""
            font-size: 36px; 
            font-weight: 850; 
            color: #261947;
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

        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setSpacing(20)

        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        self.btn_cancel.setMinimumHeight(75)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF; 
                color: #261947; 
                font-size: 24px; 
                font-weight: bold; 
                border: 2px solid #cbd5e1;
                border-radius: 20px; 
            }
            QPushButton:hover { background-color: #f1f5f9; border-color: #261947; }
        """)
        self.btn_cancel.clicked.connect(self.reject)
        self.layout_buttons.addWidget(self.btn_cancel)

        self.btn_confirm = QtWidgets.QPushButton("Yes, Action")
        self.btn_confirm.setMinimumHeight(75)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm.setStyleSheet("""
            QPushButton {
                background-color: #261947; 
                color: white; 
                font-size: 24px; 
                font-weight: bold; 
                border-radius: 20px; 
                border: none;
            }
            QPushButton:hover { background-color: #4e1c53; }
        """)
        self.btn_confirm.clicked.connect(self.accept)
        self.layout_buttons.addWidget(self.btn_confirm)

        self.layout_main.addLayout(self.layout_buttons)