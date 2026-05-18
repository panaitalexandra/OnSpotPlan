# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from ui_base_window import BaseFramelessWindow

class Ui_Popup(BaseFramelessWindow):
    def __init__(self, message, title="Notice", parent=None):
        super().__init__()
        self.message_text = message
        self.title_text = title
        self.setFixedSize(1050, 420)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ErrorPopupWindow")

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
        self.lbl_title.setStyleSheet("""
            font-size: 36px; 
            font-weight: 850; 
            color: #1e1b4b;
            background: transparent;
        """)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_main.addWidget(self.lbl_title)

        self.lbl_message = QtWidgets.QLabel(self.message_text)
        self.lbl_message.setStyleSheet("""
            font-size: 24px; 
            color: #475569; 
            font-weight: 500;
            line-height: 140%;
            background: transparent;
        """)
        self.lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_message.setWordWrap(True)
        self.layout_main.addWidget(self.lbl_message)

        self.layout_main.addStretch()

        self.btn_ok = QtWidgets.QPushButton("Acknowledge")
        self.btn_ok.setMinimumHeight(75)
        self.btn_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ok.setStyleSheet("""
            QPushButton {
                background-color: #1e1b4b; 
                color: white; 
                font-size: 24px; 
                font-weight: bold; 
                border-radius: 20px; 
                border: none;
            }
            QPushButton:hover { 
                background-color: #2e2a70; 
            }
        """)
        self.btn_ok.clicked.connect(self.close)
        self.layout_main.addWidget(self.btn_ok)