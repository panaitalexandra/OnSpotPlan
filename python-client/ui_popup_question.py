# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from ui_base_window import BaseFramelessWindow

class Ui_PopupQuestion(BaseFramelessWindow):
    def __init__(self, message, title="Confirm Action", parent=None):
        super().__init__()
        self.message_text = message
        self.title_text = title
        self.setFixedSize(1050, 450)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("QuestionPopupWindow")

        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { 
                background-color: #FFFFFF; 
                border-bottom-left-radius: 20px; 
                border-bottom-right-radius: 20px; 
            }
            * {
                font-family: 'Segoe UI', sans-serif;
                color: #1e1b4b;
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(45, 40, 45, 40)
        self.layout_main.setSpacing(20)

        self.lbl_title = QtWidgets.QLabel(self.title_text)
        self.lbl_title.setStyleSheet("font-size: 36px; font-weight: 850; color: #1e1b4b; background: transparent;")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_main.addWidget(self.lbl_title)

        self.lbl_message = QtWidgets.QLabel(self.message_text)
        self.lbl_message.setStyleSheet("font-size: 24px; color: #475569; font-weight: 500; line-height: 140%; background: transparent;")
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
                color: #1e1b4b; 
                font-size: 22px; 
                font-weight: bold; 
                border: 2px solid #cbd5e1;
                border-radius: 20px; 
            }
            QPushButton:hover { background-color: #f1f5f9; border-color: #1e1b4b; }
        """)
        self.btn_cancel.clicked.connect(self.reject)
        self.layout_buttons.addWidget(self.btn_cancel)

        self.btn_confirm = QtWidgets.QPushButton("Yes, Delete")
        self.btn_confirm.setMinimumHeight(75)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm.setStyleSheet("""
            QPushButton {
                background-color: #ef4444; 
                color: white; 
                font-size: 22px; 
                font-weight: bold; 
                border-radius: 20px; 
                border: none;
            }
            QPushButton:hover { background-color: #dc2626; }
        """)
        self.btn_confirm.clicked.connect(self.accept)
        self.layout_buttons.addWidget(self.btn_confirm)

        self.layout_main.addLayout(self.layout_buttons)