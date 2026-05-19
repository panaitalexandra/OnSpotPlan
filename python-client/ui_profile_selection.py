# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_ProfileSelection(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ProfileSelectionWindow")
        self.resize(1200, 1300)

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
            QPushButton#BackBtn {
                background-color: transparent;
                color: #1e1b4b;
                font-size: 26px;
                text-decoration: underline;
                border: none;
                margin-top: 10px;
            }
            QPushButton#BackBtn:hover {
                color: #2e2a70;
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout.setContentsMargins(50, 40, 50, 50)
        self.layout.setSpacing(30)

        self.label_title = QtWidgets.QLabel("Manage Profiles")
        self.label_title.setStyleSheet("""
            font-size: 48px; 
            font-weight: 850; 
            color: #1e1b4b; 
            letter-spacing: 2px;
            background: transparent;
            border: none;
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
                background-color: #f3f4f6; 
                alternate-background-color: #FFFFFF; 
                border: 2px solid #f3f4f6;
                border-radius: 20px;
                font-size: 26px; 
                padding: 10px;
                selection-background-color: #1e1b4b;
                selection-color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: #f3f4f6; 
                color: #1e1b4b;
                padding: 15px;
                font-weight: bold;
                font-size: 22px; 
                border: none;
                border-bottom: 3px solid #1e1b4b;
                text-transform: uppercase;
            }
            QPushButton#BackBtn {
                background-color: transparent;
                color: #1e1b4b;
                font-size: 24px;
                text-decoration: underline;
                border: none;
            }
            QPushButton#BackBtn:hover {
                color: #2e2a70;
            }
        """)

        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setSpacing(20)

        button_style = """
            QPushButton {
                font-size: 24px;          /* Mărit de la 18px pentru lizibilitate premium */
                font-weight: bold;
                border-radius: 18px;      /* Rotunjire adaptată la noua mărime */
                padding: 18px 32px;       /* Padding mărit pentru butoane mai înalte */
                min-width: 220px;         /* Lățime minimă extinsă de la 180px */
            }
        """

        self.btn_add = QtWidgets.QPushButton("＋ Add Profile")
        self.btn_add.setStyleSheet(button_style + """
            QPushButton { background-color: #f3f4f6; border: 2px solid #cbd5e1; color: #1e1b4b; }
            QPushButton:hover { background-color: #f1f5f9; border-color: #1e1b4b; }
        """)

        self.btn_delete = QtWidgets.QPushButton("Delete Profile")
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(button_style + """
                    QPushButton { 
                        background-color: #f3f4f6; 
                        color: #b91c1c; 
                        border: 2px solid #cbd5e1; 
                    }
                    QPushButton:hover { background-color: #f1f5f9; border: 2px solid #b91c1c; }
                """)

        self.btn_view = QtWidgets.QPushButton("View Details")
        self.btn_view.setStyleSheet(button_style + """
            QPushButton { background-color: #f3f4f6; border: 2px solid #cbd5e1; color: #1e1b4b; }
            QPushButton:hover { background-color: #f1f5f9; border-color: #1e1b4b;   }
        """)

        self.btn_select = QtWidgets.QPushButton("SELECT PROFILE")
        self.btn_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select.setStyleSheet(button_style + """
            QPushButton { 
                background-color: #1e1b4b; 
                color: white; 
                border: none;
                letter-spacing: 1.5px;
            }
            QPushButton:hover { background-color: #2e2a70; }
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
        self.btn_back.clicked.connect(self.reject)

        self.btn_back = QtWidgets.QPushButton("Back to Explore")
        self.btn_back.setObjectName("BackBtn")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.clicked.connect(self.reject)

        self.btn_back.setStyleSheet("""
                QPushButton#BackBtn {
                    background-color: #f3f4f6;       /* Fundal alb-murdar / gri discret */
                    color: #1e1b4b;                  /* Textul cu acel albastru închis regal */
                    font-size: 24px;
                    font-weight: bold;
                    border: 2px solid #cbd5e1;       /* Margine fină, curată */
                    border-radius: 18px;             /* Rotunjire modernă identică cu butoanele de sus */
                    padding: 18px 0px;               /* Înalt și confortabil la apăsare */
                    text-decoration: none;           /* Am eliminat complet acel underline învechit */
                }
                QPushButton#BackBtn:hover {
                    background-color: #f1f5f9;       /* Culoarea de hover solicitată de tine */
                    border-color: #1e1b4b;           /* La hover, marginea se aprinde subtil în culoarea brandului */
                }
            """)

        self.layout.addWidget(self.btn_back)
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