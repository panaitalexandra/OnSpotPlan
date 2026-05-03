# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Explore(object):
    def setupUi(self, ExploreEvents):
        ExploreEvents.setObjectName("ExploreEvents")
        ExploreEvents.resize(1000, 1250)
        ExploreEvents.setStyleSheet("background-color: #121212;")

        self.verticalLayout_main = QtWidgets.QVBoxLayout(ExploreEvents)
        self.verticalLayout_main.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_main.setObjectName("verticalLayout_main")

        self.main_container = QtWidgets.QFrame(ExploreEvents)
        self.main_container.setStyleSheet("background-color: white; border-radius: 40px;")
        self.main_layout = QtWidgets.QVBoxLayout(self.main_container)
        self.main_layout.setContentsMargins(40, 50, 40, 50)
        self.main_layout.setSpacing(35)

        # --- HEADER SECTION ---
        self.header_layout = QtWidgets.QHBoxLayout()
        self.btn_search_icon = QtWidgets.QPushButton("🔍")
        self.btn_search_icon.setFixedSize(80, 80)
        self.btn_search_icon.setStyleSheet("border: none; font-size: 45px; color: #1e1b4b;")

        self.label_logo = QtWidgets.QLabel("EventHub")
        self.label_logo.setStyleSheet("font-size: 55px; font-weight: bold; color: #1e1b4b; font-family: 'Segoe UI';")

        self.label_profile = QtWidgets.QLabel("👤")
        self.label_profile.setFixedSize(90, 90)
        self.label_profile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_profile.setStyleSheet("background-color: #e2e8f0; border-radius: 45px; font-size: 40px;")

        self.header_layout.addWidget(self.btn_search_icon)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.label_logo)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.label_profile)
        self.main_layout.addLayout(self.header_layout)

        # --- SEARCH BAR ---
        self.lineEdit_search = QtWidgets.QLineEdit()
        self.lineEdit_search.setPlaceholderText("Search events, organizers, or cities...")
        self.lineEdit_search.setMinimumHeight(100)
        self.lineEdit_search.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #d1d5db;
                border-radius: 25px;
                padding-left: 30px;
                font-size: 32px;
                color: #4b5563;
            }
        """)
        self.main_layout.addWidget(self.lineEdit_search)

        # --- FILTERS BUTTON ---
        self.btn_filters = QtWidgets.QPushButton("  ≡  Filters")
        self.btn_filters.setMinimumHeight(90)
        self.btn_filters.setStyleSheet("""
            QPushButton {
                background-color: #1e1b4b;
                color: white;
                font-size: 32px;
                font-weight: bold;
                border-radius: 25px;
            }
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.main_layout.addWidget(self.btn_filters)

        # --- CATEGORIES ---
        self.cat_layout = QtWidgets.QHBoxLayout()
        self.cat_layout.setSpacing(20)
        categories = ["All Events", "Music", "Tech", "Food"]
        for cat in categories:
            btn = QtWidgets.QPushButton(cat)
            btn.setMinimumHeight(70)
            if cat == "All Events":
                btn.setStyleSheet("background-color: #1e1b4b; color: white; border-radius: 35px; padding: 0 40px; font-size: 26px; font-weight: bold;")
            else:
                btn.setStyleSheet("background-color: white; color: #4b5563; border: 2px solid #d1d5db; border-radius: 35px; padding: 0 40px; font-size: 26px;")
            self.cat_layout.addWidget(btn)
        self.main_layout.addLayout(self.cat_layout)

        # --- RECOMMENDATION HEADER ---
        self.rec_header = QtWidgets.QHBoxLayout()
        self.label_rec = QtWidgets.QLabel("Recommended for You")
        self.label_rec.setStyleSheet("font-size: 38px; font-weight: bold; color: #1f2937;")
        self.btn_view_all = QtWidgets.QPushButton("View All")
        self.btn_view_all.setStyleSheet("border: none; color: #4338ca; font-size: 28px; font-weight: bold; text-decoration: underline;")
        self.rec_header.addWidget(self.label_rec)
        self.rec_header.addStretch()
        self.rec_header.addWidget(self.btn_view_all)
        self.main_layout.addLayout(self.rec_header)

        # --- EVENT CARD ---
        self.event_card = QtWidgets.QFrame()
        self.event_card.setMinimumHeight(550)
        self.event_card.setStyleSheet("""
            QFrame {
                background-color: #1e1b4b;
                border-radius: 40px;
                /* Imaginea de fundal ar trebui setată în main.py pentru flexibilitate */
            }
        """)
        self.card_layout = QtWidgets.QVBoxLayout(self.event_card)
        self.card_layout.setContentsMargins(40, 40, 40, 40)
        self.card_layout.setSpacing(15)

        self.tag_tech = QtWidgets.QLabel("TECH")
        self.tag_tech.setFixedSize(140, 60)
        self.tag_tech.setAlignment(QtCore.Qt.AlignCenter)
        self.tag_tech.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); color: white; border-radius: 15px; font-size: 24px; font-weight: bold;")

        self.label_date = QtWidgets.QLabel("Sept 24 • Global Innovation Center")
        self.label_date.setStyleSheet("color: #e2e8f0; font-size: 26px; background: transparent;")

        self.label_event_title = QtWidgets.QLabel("Future Forward Summit 2024")
        self.label_event_title.setStyleSheet("color: white; font-size: 48px; font-weight: bold; background: transparent;")

        self.bottom_card = QtWidgets.QHBoxLayout()
        self.label_price = QtWidgets.QLabel("$199.00")
        self.label_price.setStyleSheet("color: white; font-size: 42px; font-weight: bold; background: transparent;")

        self.btn_book = QtWidgets.QPushButton("Book Now")
        self.btn_book.setFixedSize(280, 90)
        self.btn_book.setStyleSheet("""
            QPushButton {
                background-color: #3d7068;
                color: white;
                border-radius: 20px;
                font-size: 32px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #4d8a7f; }
        """)

        self.bottom_card.addWidget(self.label_price)
        self.bottom_card.addStretch()
        self.bottom_card.addWidget(self.btn_book)

        self.card_layout.addWidget(self.tag_tech)
        self.card_layout.addStretch()
        self.card_layout.addWidget(self.label_date)
        self.card_layout.addWidget(self.label_event_title)
        self.card_layout.addLayout(self.bottom_card)

        self.main_layout.addWidget(self.event_card)
        self.verticalLayout_main.addWidget(self.main_container)

        self.retranslateUi(ExploreEvents)
        QtCore.QMetaObject.connectSlotsByName(ExploreEvents)

    def retranslateUi(self, ExploreEvents):
        _translate = QtCore.QCoreApplication.translate
        ExploreEvents.setWindowTitle(_translate("ExploreEvents", "Explore Events - EventHub"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ExploreEvents()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())