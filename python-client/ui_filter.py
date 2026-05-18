# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow


class Ui_Filter(BaseFramelessWindow):
    def __init__(self, parent=None, orase_dinamice=None):
        super().__init__()
        self.setFixedSize(1300, 1300)
        self.selected_city = None
        # Schimbat fallback-ul în "All" pentru a se potrivi perfect cu logica din explore_02.py
        self.orase_de_afisat = orase_dinamice if orase_dinamice else ["All"]
        self.setupUi()

    def setupUi(self):
        self.setObjectName("FilterWindow")

        self.content_widget = QtWidgets.QWidget()
        # Trecem fundalul principal pe alb curat și setăm culoarea textului implicită
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
            QLabel { 
                color: #1e1b4b; 
                font-size: 42px; 
                font-weight: 850; 
                background: transparent;
                margin-bottom: 10px;
            }
            /* Celulele orașelor devin alb-murdar cu margini fine */
            QPushButton#CityCell {
                background-color: #f3f4f6;
                color: #1e1b4b;
                font-size: 24px;
                font-weight: bold;
                border: 2px solid #cbd5e1;
                border-radius: 15px;
                padding: 30px 10px;
            }
            QPushButton#CityCell:hover {
                background-color: #f1f5f9;
                border: 2px solid #1e1b4b;
            }
            /* Când un oraș este selectat, celula devine albastru închis cu text alb */
            QPushButton#CityCell:checked {
                background-color: #1e1b4b;
                border: 2px solid #1e1b4b;
                color: #1e1b4b;
            }
            /* Butonul de confirmare principal primește culoarea plină de brand */
            QPushButton#ConfirmBtn { 
                background-color: #1e1b4b; 
                color: white; 
                font-size: 30px; 
                font-weight: bold; 
                border-radius: 20px; 
                padding: 20px;
                margin-top: 10px;
                border: none;
            }
            QPushButton#ConfirmBtn:hover { 
                background-color: #2e2a70; 
            }
            /* Butonul Back stilizat premium: lat, fără linie dedesubt și cu fundal reactiv */
            QPushButton#BackBtn {
                background-color: #f3f4f6;
                color: #1e1b4b;
                font-size: 24px;
                font-weight: bold;
                border: 2px solid #cbd5e1;
                border-radius: 20px;
                padding: 20px;
                text-decoration: none;
            }
            QPushButton#BackBtn:hover {
                background-color: #f1f5f9;
                border-color: #1e1b4b;
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.filter_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.filter_layout.setContentsMargins(40, 30, 40, 40)
        self.filter_layout.setSpacing(20)

        self.label = QtWidgets.QLabel("Where would you like to go?")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_layout.addWidget(self.label)

        self.grid_widget = QtWidgets.QWidget()
        # Ne asigurăm că grid-ul este transparent pentru a lăsa fundalul alb să se vadă curat
        self.grid_widget.setStyleSheet("background: transparent;")
        self.grid_layout = QtWidgets.QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(15)

        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.setExclusive(True)

        orase = self.orase_de_afisat

        row = 0
        col = 0
        for oras in orase:
            btn = QtWidgets.QPushButton(oras)
            btn.setObjectName("CityCell")
            btn.setCheckable(True)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            if oras == "All":
                btn.setChecked(True)

            self.button_group.addButton(btn)
            self.grid_layout.addWidget(btn, row, col)

            col += 1
            if col > 2:
                col = 0
                row += 1

        self.filter_layout.addWidget(self.grid_widget)

        self.btn_select = QtWidgets.QPushButton("Apply Filter")
        self.btn_select.setObjectName("ConfirmBtn")
        self.btn_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select.clicked.connect(self.accept)
        self.filter_layout.addWidget(self.btn_select)

        self.btn_back = QtWidgets.QPushButton("Back to Explore")
        self.btn_back.setObjectName("BackBtn")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.clicked.connect(self.reject)
        self.filter_layout.addWidget(self.btn_back)

    def get_selection(self):
        selected_button = self.button_group.checkedButton()
        return selected_button.text() if selected_button else None