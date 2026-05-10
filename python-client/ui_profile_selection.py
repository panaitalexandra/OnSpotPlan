# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_ProfileSelection(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ProfileSelectionWindow")
        self.resize(1000, 1250)

        # Widget-ul de conținut (cel care va sta sub bara de titlu)
        self.content_widget = QtWidgets.QWidget()
        # Aplicăm tema dark pe acest widget pentru a acoperi fundalul alb default al body-ului
        self.content_widget.setStyleSheet("""
            QWidget {
                background-color: #0f172a; 
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
            }
            * {
                font-family: 'Segoe UI', sans-serif;
                color: #f8fafc;
            }
            QPushButton#BackBtn {
                background-color: transparent;
                color: #94a3b8;
                font-size: 26px;
                text-decoration: underline;
                border: none;
                margin-top: 10px;
            }
            QPushButton#BackBtn:hover {
                color: #38bdf8;
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout.setContentsMargins(50, 40, 50, 50)
        self.layout.setSpacing(30)

        # --- TITLU ---
        self.label_title = QtWidgets.QLabel("Manage Profiles")
        self.label_title.setStyleSheet("""
            font-size: 48px; 
            font-weight: 850; 
            color: #38bdf8; 
            letter-spacing: 2px;
            background: transparent;
            border: none;
        """)
        self.layout.addWidget(self.label_title)

        # --- TABEL ---
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["LAST NAME", "FIRST NAME", "CNP"])
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setShowGrid(False)
        self.table.verticalHeader().setDefaultSectionSize(70)
        self.table.verticalHeader().setVisible(False)

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #1e293b;
                alternate-background-color: #334155;
                border: 2px solid #475569;
                border-radius: 20px;
                font-size: 22px;
                padding: 10px;
                selection-background-color: #3d7068;
            }
            QHeaderView::section {
                background-color: #1e293b;
                color: #38bdf8;
                padding: 15px;
                font-weight: bold;
                font-size: 18px;
                border: none;
                border-bottom: 3px solid #38bdf8;
                text-transform: uppercase;
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

        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # --- BUTOANE ---
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setSpacing(20)

        button_style = """
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                border-radius: 15px;
                padding: 15px 25px;
                min-width: 180px;
            }
        """

        self.btn_add = QtWidgets.QPushButton("＋ Add Profile")
        self.btn_add.setStyleSheet(button_style + """
            QPushButton { background-color: #1e1b4b; border: 2px solid #4338ca; color: white; }
            QPushButton:hover { background-color: #312e81; border: 2px solid #38bdf8; }
        """)

        self.btn_delete = QtWidgets.QPushButton("Delete Profile")
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(button_style + """
                    QPushButton { 
                        background-color: #7f1d1d; 
                        color: white; 
                        border: 2px solid #b91c1c; 
                    }
                    QPushButton:hover { background-color: #b91c1c; }
                """)

        self.btn_view = QtWidgets.QPushButton("View Details")
        self.btn_view.setStyleSheet(button_style + """
            QPushButton { background-color: #1e1b4b; border: 2px solid #4338ca; color: white; }
            QPushButton:hover { background-color: #312e81; border: 2px solid #38bdf8; }
        """)

        self.btn_select = QtWidgets.QPushButton("SELECT PROFILE")
        self.btn_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select.setStyleSheet(button_style + """
            QPushButton { 
                background-color: #3d7068; 
                color: white; 
                border: none;
                letter-spacing: 1.5px;
            }
            QPushButton:hover { background-color: #4d8a7f; }
        """)

        self.btn_layout.addWidget(self.btn_add)
        self.btn_layout.addWidget(self.btn_delete)
        self.btn_layout.addWidget(self.btn_view)
        self.btn_layout.addStretch()
        self.btn_layout.addWidget(self.btn_select)
        self.layout.addLayout(self.btn_layout)

        self.back_btn_layout = QtWidgets.QHBoxLayout()
        self.btn_back = QtWidgets.QPushButton("Back to Explore")
        self.btn_back.setObjectName("BackBtn")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.clicked.connect(self.reject)  # Reject închide dialogul

        self.back_btn_layout.addStretch()
        self.back_btn_layout.addWidget(self.btn_back)
        self.back_btn_layout.addStretch()

        self.layout.addLayout(self.back_btn_layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "EventHub - Manage Profiles"))
        self.label_title.setText(_translate("Dialog", "Manage Profiles"))
        self.btn_add.setText(_translate("Dialog", "＋ Add Profile"))
        self.btn_delete.setText(_translate("Dialog", " - Delete Profile"))
        self.btn_view.setText(_translate("Dialog", "View Details"))
        self.btn_select.setText(_translate("Dialog", "SELECT PROFILE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ProfileSelection()
    ui.show()
    sys.exit(app.exec_())