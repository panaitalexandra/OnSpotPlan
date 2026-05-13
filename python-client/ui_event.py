# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from ui_base_window import BaseFramelessWindow
from ui_booking import Ui_BookingApp


class Ui_Event(BaseFramelessWindow):
    def __init__(self, gateway, event_data, active_client):
        super().__init__()
        self.gateway = gateway
        self.event_data = event_data
        self.active_client = active_client
        self.setupUi()

    def setupUi(self):
        import os

        # Calea pe care o primește fereastra
        path_imagine = self.event_data.get('imagine', 'resources/ev1.jpg')

        print("--- DIAGNOSTICARE IMAGINE ---")
        print(f"Director curent de lucru (CWD): {os.getcwd()}")
        print(f"Calea relativă căutată: {path_imagine}")
        print(f"Calea absolută calculată: {os.path.abspath(path_imagine)}")
        print(f"Fișierul există la această locație? {'DA' if os.path.exists(path_imagine) else 'NU'}")
        print("-----------------------------")
        self.setObjectName("EventDetailWindow")
        self.resize(1200, 1300)
        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { background-color: #0f172a; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; }
            * { font-family: 'Segoe UI', sans-serif; color: #f8fafc; }
            QPushButton#BackBtn { background-color: transparent; color: #94a3b8; font-size: 24px; text-decoration: underline; border: none; }
            QPushButton#BackBtn:hover { color: #38bdf8; }
        """)
        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(0)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: none; background: transparent;")
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 30)
        self.scroll_layout.setSpacing(0)

        self.lbl_image = QtWidgets.QLabel()
        self.lbl_image.setMinimumHeight(550)
        pixmap = QtGui.QPixmap(self.event_data.get('imagine', 'resources/placeholder.jpg'))
        if not pixmap.isNull():
            self.lbl_image.setPixmap(
                pixmap.scaled(1200, 550, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation))
        self.lbl_image.setScaledContents(True)
        self.scroll_layout.addWidget(self.lbl_image)

        self.info_container = QtWidgets.QWidget()
        self.info_layout = QtWidgets.QVBoxLayout(self.info_container)
        self.info_layout.setContentsMargins(60, 40, 60, 20)
        self.info_layout.setSpacing(15)

        self.badge_container = QtWidgets.QHBoxLayout()
        self.lbl_region = QtWidgets.QLabel(f"  📍 {self.event_data.get('regiune', 'Unknown')}  ")
        self.lbl_region.setStyleSheet("""
                    background-color: #1e293b; color: #38bdf8; border-radius: 12px; 
                    font-size: 18px; font-weight: bold; padding: 8px; border: 1px solid #334155;
                """)
        self.badge_container.addWidget(self.lbl_region)
        self.badge_container.addStretch()
        self.info_layout.addLayout(self.badge_container)

        self.lbl_title = QtWidgets.QLabel(self.event_data.get('nume', 'Event Name'))
        self.lbl_title.setStyleSheet("font-size: 52px; font-weight: 850; color: #38bdf8;")
        self.lbl_title.setWordWrap(True)
        self.info_layout.addWidget(self.lbl_title)

        self.lbl_venue = QtWidgets.QLabel(f"At {self.event_data.get('locatie', 'Main Venue')}")
        self.lbl_venue.setStyleSheet("font-size: 26px; color: #38bdf8; font-weight: 600; margin-bottom: 20px;")
        self.info_layout.addWidget(self.lbl_venue)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setStyleSheet("background-color: #334155; max-height: 1px; margin: 10px 0;")
        self.info_layout.addWidget(line)

        self.lbl_about_title = QtWidgets.QLabel("About this event")
        self.lbl_about_title.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #94a3b8; text-transform: uppercase;")
        self.info_layout.addWidget(self.lbl_about_title)

        self.lbl_description = QtWidgets.QLabel(self.event_data.get('descriere', 'No description...'))
        self.lbl_description.setWordWrap(True)
        self.lbl_description.setStyleSheet("font-size: 22px; color: #94a3b8;")
        self.info_layout.addWidget(self.lbl_description)

        # CORECCȚIE 1: Schimbat din self.text_container în self.info_container
        self.scroll_layout.addWidget(self.info_container)

        self.scroll.setWidget(self.scroll_content)
        self.layout_main.addWidget(self.scroll)

        self.footer = QtWidgets.QFrame()
        self.footer.setMinimumHeight(130)
        self.footer.setStyleSheet(
            "background-color: #1e293b; border-top: 2px solid #334155; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px;")

        # CORECCȚIE 2: Definit footer_layout
        self.footer_layout = QtWidgets.QHBoxLayout(self.footer)
        self.footer_layout.setContentsMargins(60, 0, 60, 0)

        self.btn_back = QtWidgets.QPushButton("← Back to Explore")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet(
            "QPushButton { background: transparent; color: #94a3b8; font-size: 20px; font-weight: 600; border: none; } QPushButton:hover { color: #f8fafc; }")
        self.btn_back.clicked.connect(self.close)

        self.btn_proceed = QtWidgets.QPushButton("BOOK TICKETS NOW")
        self.btn_proceed.setFixedSize(380, 70)
        self.btn_proceed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_proceed.setStyleSheet(
            "QPushButton { background-color: #38bdf8; color: #0f172a; font-weight: 800; border-radius: 20px; font-size: 20px; letter-spacing: 1px; } QPushButton:hover { background-color: #7dd3fc; }")
        self.btn_proceed.clicked.connect(self.open_booking)

        self.footer_layout.addWidget(self.btn_back)
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(self.btn_proceed)
        self.layout_main.addWidget(self.footer)

    def open_booking(self):
        self.gateway.booking_win = Ui_BookingApp(self.gateway, self.event_data['nume'], self.active_client)
        self.gateway.booking_win.show()
        self.close()