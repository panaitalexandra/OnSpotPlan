# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
import os
import PyQt5
from ui_base_window import BaseFramelessWindow
from ui_booking import Ui_BookingApp
from ui_popup import Ui_Popup

pyqt_path = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(pyqt_path, "Qt5", "plugins") if os.path.exists(
    os.path.join(pyqt_path, "Qt5", "plugins")) else os.path.join(pyqt_path, "Qt", "plugins")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path


class Ui_Event(BaseFramelessWindow):
    def __init__(self, gateway, event_java, active_client, user_email):
        super().__init__()
        self.gateway = gateway
        self.event_java = event_java  # Obiectul Java real (Event.java)
        self.user_email = user_email
        self.active_client = active_client
        self.setupUi()

    def setupUi(self):
        self.setObjectName("EventDetailWindow")
        self.resize(1300, 1300)

        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { background-color: #FFFFFF; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; }
            * { font-family: 'Segoe UI', sans-serif; color: #1e1b4b; }
        """)
        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.setSpacing(0)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: none; background: transparent;")

        self.scroll_content = QtWidgets.QWidget()
        self.scroll_content.setStyleSheet("background: transparent;")

        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 30)
        self.scroll_layout.setSpacing(0)

        self.lbl_image = QtWidgets.QLabel()
        self.lbl_image.setFixedHeight(500)
        self.lbl_image.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        try:
            event_id = self.event_java.getId()
            numar_imagine = (event_id % 3)
            if numar_imagine == 0: numar_imagine = 3
            nume_fisier = f"ev{numar_imagine}.jpg"
            path_imagine = os.path.join(BASE_DIR, "resources", nume_fisier)
            if not os.path.exists(path_imagine):
                path_imagine = os.path.join(BASE_DIR, nume_fisier)
        except Exception as e:
            path_imagine = ""

        pixmap = QtGui.QPixmap(path_imagine)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(1300, 500, QtCore.Qt.KeepAspectRatioByExpanding,
                                          QtCore.Qt.SmoothTransformation)
            self.lbl_image.setPixmap(scaled_pixmap)
            self.lbl_image.setScaledContents(False)

        self.scroll_layout.addWidget(self.lbl_image)

        self.info_container = QtWidgets.QWidget()
        self.info_container.setStyleSheet("""
                    QWidget#InfoContainer {
                        background-color: #FFFFFF; 
                        border-top-left-radius: 30px; 
                        border-top-right-radius: 30px;
                        border-top: 1px solid #cbd5e1;
                    }
                    * { color: #1e1b4b; }
                """)
        self.info_container.setObjectName("InfoContainer")

        self.info_layout = QtWidgets.QVBoxLayout(self.info_container)
        self.info_layout.setContentsMargins(60, 40, 60, 20)
        self.info_layout.setSpacing(15)

        self.scroll_layout.addWidget(self.info_container)

        self.badge_container = QtWidgets.QHBoxLayout()
        self.lbl_date_badge = QtWidgets.QLabel(f"  📅 {self.event_java.getDateTime()}  ")
        self.lbl_date_badge.setStyleSheet("""
                    background-color: #f3f4f6; color: #1e1b4b; border-radius: 12px; 
                    font-size: 24px; font-weight: bold; padding: 8px; border: 1px solid #cbd5e1;
                """)
        self.badge_container.addWidget(self.lbl_date_badge)
        self.badge_container.addStretch()
        self.info_layout.addLayout(self.badge_container)

        self.lbl_title = QtWidgets.QLabel(self.event_java.getName())
        self.lbl_title.setStyleSheet("font-size: 52px; font-weight: 850; color: #1e1b4b; margin-top: 5px;")
        self.lbl_title.setWordWrap(True)
        self.info_layout.addWidget(self.lbl_title)

        try:
            locatie = self.event_java.getLocatie()
            oras = self.event_java.getOras()
            locatie_completa = f"📍 {locatie}, {oras}"
        except Exception as e:
            locatie_completa = f"📍 {self.event_java.getLocation()}"

        self.lbl_venue = QtWidgets.QLabel(locatie_completa)
        self.lbl_venue.setStyleSheet("font-size: 32px; color: #475569; font-weight: 700; margin-bottom: 12px;")
        self.lbl_venue.setWordWrap(True)
        self.info_layout.addWidget(self.lbl_venue)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setStyleSheet("background-color: #cbd5e1; max-height: 1px; margin: 10px 0;")
        self.info_layout.addWidget(line)

        self.lbl_about_title = QtWidgets.QLabel("About this event")
        self.lbl_about_title.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #1e1b4b; text-transform: uppercase;")
        self.info_layout.addWidget(self.lbl_about_title)

        self.lbl_description = QtWidgets.QLabel(self.event_java.getDescription())
        self.lbl_description.setWordWrap(True)
        self.lbl_description.setStyleSheet("font-size: 22px; color: #475569; line-height: 140%;")
        self.info_layout.addWidget(self.lbl_description)

        self.info_layout.addSpacing(35)

        self.lbl_ticket_select = QtWidgets.QLabel("SELECT YOUR TICKET TYPE")
        self.lbl_ticket_select.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e1b4b;")
        self.info_layout.addWidget(self.lbl_ticket_select)

        self.combo_bilete = QtWidgets.QComboBox()
        self.combo_bilete.setMinimumHeight(80)
        self.combo_bilete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.combo_bilete.setStyleSheet("""
            QComboBox {
                background-color: #f3f4f6; 
                border: 2px solid #cbd5e1; 
                border-radius: 20px; 
                padding: 10px 25px; 
                font-size: 26px;
                font-weight: 500;
                color: #1e1b4b;
            }
            QComboBox:hover { 
                border: 2px solid #1e1b4b; 
                background-color: #f8fafc;
            }
            QComboBox::drop-down { 
                border: none; 
                width: 60px;
            }

            QAbstractItemView { 
                background-color: #FFFFFF; 
                color: #1e1b4b; 
                border: 2px solid #cbd5e1; 
                border-radius: 20px; 
                font-size: 26px;
                font-weight: 400;
                selection-background-color: #1e1b4b; 
                selection-color: #FFFFFF; 
                outline: 0px;
            }

            QAbstractItemView::item { 
                padding: 22px 25px; 
                border-bottom: 1px solid #e2e8f0;
                background-color: #FFFFFF;
            }

            QAbstractItemView::item:selected { 
                background-color: #1e1b4b; 
                color: #FFFFFF;
            }
        """)

        try:
            categories = self.event_java.getTicketCategories()
            if categories is not None:
                for i in range(categories.size()):
                    cat = categories.get(i)
                    self.combo_bilete.addItem(f"{cat.getTicketType()} — {cat.getPrice()} RON", cat)
        except Exception as e:
            self.popup = Ui_Popup(f"Could not load ticket categories: {e}", title="Loading Error")
            self.popup.show()

        self.info_layout.addWidget(self.combo_bilete)

        self.scroll.setWidget(self.scroll_content)
        self.layout_main.addWidget(self.scroll)

        self.footer = QtWidgets.QFrame()
        self.footer.setMinimumHeight(150)
        self.footer.setStyleSheet("""
            background-color: #FFFFFF; border-top: 2px solid #cbd5e1; 
            border-bottom-left-radius: 30px; border-bottom-right-radius: 30px;
        """)

        self.footer_layout = QtWidgets.QHBoxLayout(self.footer)
        self.footer_layout.setContentsMargins(60, 0, 60, 0)

        self.btn_back = QtWidgets.QPushButton("← Back to Explore")
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("""
            QPushButton { 
                background-color: #f3f4f6; 
                color: #1e1b4b; 
                font-size: 20px; 
                font-weight: bold; 
                border: 2px solid #cbd5e1; 
                border-radius: 20px; 
                padding: 15px 30px; 
            } 
            QPushButton:hover { 
                background-color: #e5e7eb; 
                border-color: #1e1b4b; 
            }
        """)
        self.btn_back.clicked.connect(self.close)

        self.btn_proceed = QtWidgets.QPushButton("BOOK TICKETS NOW")
        self.btn_proceed.setFixedSize(420, 80)
        self.btn_proceed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_proceed.setStyleSheet("""
            QPushButton { 
                background-color: #1e1b4b; color: white; font-weight: 850; 
                border-radius: 25px; font-size: 22px; letter-spacing: 1px; 
                border: none;
            } 
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.btn_proceed.clicked.connect(self.open_booking)

        self.footer_layout.addWidget(self.btn_back)
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(self.btn_proceed)
        self.layout_main.addWidget(self.footer)

    def open_booking(self):
        categorie_selectata = self.combo_bilete.currentData()
        self.booking_win = Ui_BookingApp(self.gateway, self.event_java, self.active_client, categorie_selectata,
                                         self.user_email)
        self.booking_win.show()
        self.close()