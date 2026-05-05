from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileSelection(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 850)
        Dialog.setStyleSheet("""
            QDialog {
                background-color: #0f172a; 
            }
            * {
                font-family: 'Segoe UI', sans-serif;
                color: #f8fafc;
            }
        """)

        self.layout = QtWidgets.QVBoxLayout(Dialog)
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.layout.setSpacing(30)

        self.label_title = QtWidgets.QLabel("Manage Profiles")
        self.label_title.setStyleSheet("""
            font-size: 48px; 
            font-weight: 850; 
            color: #38bdf8; 
            letter-spacing: 2px;
            margin-bottom: 15px;
        """)
        self.layout.addWidget(self.label_title)

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
                font-size: 22px; /* Font generos pentru date */
                padding: 15px;
                selection-background-color: #3d7068;
            }
            QHeaderView::section {
                background-color: #1e293b;
                color: #38bdf8;
                padding: 15px;
                font-weight: bold;
                font-size: 18px; /* Header mai vizibil */
                border: none;
                border-bottom: 3px solid #38bdf8;
                text-transform: uppercase;
            }
            QTableWidget::item {
                padding: 20px;
            }
        """)

        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setSpacing(20)

        button_style = """
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                border-radius: 15px;
                padding: 20px 30px;
                min-width: 200px;
            }
        """

        self.btn_add = QtWidgets.QPushButton("＋ Add Profile")
        self.btn_add.setStyleSheet(button_style + """
            QPushButton { background-color: #1e1b4b; border: 2px solid #4338ca; }
            QPushButton:hover { background-color: #312e81; border: 2px solid #38bdf8; }
        """)

        self.btn_view = QtWidgets.QPushButton("View Details")
        self.btn_view.setStyleSheet(button_style + """
            QPushButton { background-color: #1e1b4b; border: 2px solid #4338ca; }
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
        self.btn_layout.addWidget(self.btn_view)
        self.btn_layout.addStretch()
        self.btn_layout.addWidget(self.btn_select)

        self.layout.addLayout(self.btn_layout)