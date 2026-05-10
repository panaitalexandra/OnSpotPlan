# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_Explore(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ExploreEventsWindow")
        self.resize(1000, 1250)

        self.content_widget = QtWidgets.QWidget()
        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_main.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_main.setObjectName("verticalLayout_main")

        self.scroll_area = QtWidgets.QScrollArea(self.content_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none; background-color: transparent;")
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.main_container = QtWidgets.QFrame()
        self.main_container.setStyleSheet("background-color: white; border-radius: 40px;")
        self.main_layout = QtWidgets.QVBoxLayout(self.main_container)
        self.main_layout.setContentsMargins(40, 50, 40, 50)
        self.main_layout.setSpacing(35)
        self.main_layout.setObjectName("main_layout")

        self.header_layout = QtWidgets.QHBoxLayout()

        self.label_logo = QtWidgets.QLabel("EventHub")
        self.label_logo.setStyleSheet("font-size: 55px; font-weight: bold; color: #1e1b4b; font-family: 'Segoe UI';")

        self.btn_profile = QtWidgets.QPushButton("Profiles")
        self.btn_profile.setMinimumHeight(60)
        self.btn_profile.setMinimumWidth(180)
        self.btn_profile.setStyleSheet("""
            QPushButton {
                background-color: #f1f5f9;
                color: #1e1b4b;
                font-size: 24px;
                font-weight: 600;
                border-radius: 20px;
                padding: 10px 20px;
                border: 1px solid #cbd5e1;
            }
            QPushButton:hover {
                background-color: #e2e8f0;
            }
        """)
        self.btn_logout = QtWidgets.QPushButton("Log Out")
        self.btn_logout.setMinimumHeight(70)
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet("""
                    QPushButton {
                        background-color: #f1f5f9;
                        color: #ef4444;
                        border: 2px solid #ef4444;
                        border-radius: 35px;
                        padding: 0 30px;
                        font-size: 24px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #fee2e2;
                    }
                """)
        self.header_layout.addWidget(self.label_logo)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.btn_profile)
        self.header_layout.addWidget(self.btn_logout)

        self.main_layout.addLayout(self.header_layout)
        self.lbl_active_user = QtWidgets.QLabel("Current Profile: None")
        self.lbl_active_user.setObjectName("lbl_active_user")
        self.lbl_active_user.setStyleSheet("""
                    color: #38bdf8; 
                    font-size: 30px; 
                    font-weight: bold; 
                    margin-top: 10px;
                    margin-left: 5px;
                """)
        self.main_layout.addWidget(self.lbl_active_user)
        self.lineEdit_search = QtWidgets.QLineEdit()
        self.lineEdit_search.setPlaceholderText("Search events, organizers, or cities...")
        self.lineEdit_search.setMinimumHeight(100)
        self.lineEdit_search.setStyleSheet(
            "background-color: #ffffff; border: 2px solid #d1d5db; border-radius: 25px; padding-left: 30px; font-size: 32px; color: #4b5563;")
        self.main_layout.addWidget(self.lineEdit_search)

        self.btn_filters = QtWidgets.QPushButton("  ≡  Filters")
        self.btn_filters.setMinimumHeight(90)
        self.btn_filters.setStyleSheet(
            "background-color: #1e1b4b; color: white; font-size: 32px; font-weight: bold; border-radius: 25px;")
        self.main_layout.addWidget(self.btn_filters)

        self.cat_layout = QtWidgets.QHBoxLayout()
        self.cat_layout.setSpacing(20)
        categories = ["All Events", "Music", "Tech", "Food"]
        for cat in categories:
            btn = QtWidgets.QPushButton(cat)
            btn.setMinimumHeight(70)
            btn.setStyleSheet(
                "background-color: white; color: #4b5563; border: 2px solid #d1d5db; border-radius: 35px; padding: 0 40px; font-size: 26px;")
            self.cat_layout.addWidget(btn)
        self.main_layout.addLayout(self.cat_layout)

        self.rec_header = QtWidgets.QHBoxLayout()
        self.label_rec = QtWidgets.QLabel("Recommended for You")
        self.label_rec.setStyleSheet("font-size: 38px; font-weight: bold; color: #1f2937;")
        self.rec_header.addWidget(self.label_rec)
        self.rec_header.addStretch()
        self.main_layout.addLayout(self.rec_header)

        self.scroll_area.setWidget(self.main_container)
        self.verticalLayout_main.addWidget(self.scroll_area)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ExploreEvents", "Explore Events - EventHub"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Explore()
    ui.setupUi()
    sys.exit(app.exec_())