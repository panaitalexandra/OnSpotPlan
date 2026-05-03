# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

class Ui_Filter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Selectează Orașul")
        self.setFixedSize(500, 650)

        self.setStyleSheet("""
            QDialog { background-color: #121212; border-radius: 25px; }
            QLabel { color: white; font-size: 36px; font-weight: bold; margin: 20px; }
            QListWidget { 
                background-color: #1e1b4b; color: white; font-size: 26px; 
                border-radius: 20px; padding: 15px; outline: none; border: none;
            }
            QListWidget::item { padding: 20px; border-bottom: 1px solid #2e2a70; }
            QListWidget::item:selected { background-color: #3d7068; border-radius: 12px; }
            QPushButton { 
                background-color: #3d7068; color: white; font-size: 28px; 
                font-weight: bold; border-radius: 20px; padding: 20px; margin-top: 10px;
            }
            QPushButton:hover { background-color: #4d8a7f; }
        """)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Unde vrei să ieși?")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.lista_orase = QtWidgets.QListWidget()
        self.orase = ["Constanta", "Ialomita", "Tulcea", "Calarasi", "Braila", "Ilfov"]
        self.lista_orase.addItems(self.orase)

        self.btn_select = QtWidgets.QPushButton("Confirmă Selecția")
        self.btn_select.clicked.connect(self.accept)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lista_orase)
        self.layout.addWidget(self.btn_select)

    def get_selection(self):
        return self.lista_orase.currentItem().text() if self.lista_orase.currentItem() else None