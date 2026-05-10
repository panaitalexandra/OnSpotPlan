# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow


class Ui_Filter(BaseFramelessWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setFixedSize(1000, 1250)
        self.selected_city = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("FilterWindow")

        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { 
                background-color: #0f172a; 
                border-bottom-left-radius: 20px; 
                border-bottom-right-radius: 20px; 
            }
            QLabel { 
                color: #38bdf8; 
                font-size: 42px; 
                font-weight: 850; 
                background: transparent;
                margin-bottom: 10px;
            }
            QPushButton#CityCell {
                background-color: #1e293b;
                color: white;
                font-size: 24px;
                font-weight: bold;
                border: 2px solid #334155;
                border-radius: 15px;
                padding: 30px 10px;
            }
            QPushButton#CityCell:hover {
                background-color: #1e1b4b;
                border: 2px solid #38bdf8;
            }
            QPushButton#CityCell:checked {
                background-color: #3d7068;
                border: 2px solid #38bdf8;
                color: white;
            }
            QPushButton#ConfirmBtn { 
                background-color: #3d7068; 
                color: white; 
                font-size: 30px; 
                font-weight: bold; 
                border-radius: 20px; 
                padding: 20px;
                margin-top: 10px;
            }
            QPushButton#ConfirmBtn:hover { 
                background-color: #4d8a7f; 
            }
            QPushButton#BackBtn {
            background-color: transparent;
            color: #94a3b8;
            font-size: 24px;
            text-decoration: underline;
            border: none;
        }
        QPushButton#BackBtn:hover {
            color: #38bdf8;
        }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.filter_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.filter_layout.setContentsMargins(40, 30, 40, 40)
        self.filter_layout.setSpacing(20)

        self.label = QtWidgets.QLabel("Unde vrei să ieși?")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_layout.addWidget(self.label)

        self.grid_widget = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(15)

        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.setExclusive(True)

        # Lista extinsă de orașe
        orase = [
            "Constanta", "Ialomita", "Tulcea",
            "Calarasi", "Braila", "Ilfov",
            "Bucuresti", "Galati", "Prahova",
            "Arges", "Dambovita", "Giurgiu"
        ]

        row = 0
        col = 0
        for oras in orase:
            btn = QtWidgets.QPushButton(oras)
            btn.setObjectName("CityCell")
            btn.setCheckable(True)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            self.button_group.addButton(btn)
            # Adăugăm în grid (3 coloane acum)
            self.grid_layout.addWidget(btn, row, col)

            col += 1
            if col > 2:  # Trecem la rândul următor după 3 coloane
                col = 0
                row += 1

        self.filter_layout.addWidget(self.grid_widget)

        self.btn_select = QtWidgets.QPushButton("Confirmă Selecția")
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