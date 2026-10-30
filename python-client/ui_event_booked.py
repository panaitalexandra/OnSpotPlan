# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from ui_base_window import BaseFramelessWindow


class Ui_EventBook(BaseFramelessWindow):
    def __init__(self, gateway, event_java, active_client, categorie_selectata, user_email):
        super().__init__()
        self.gateway = gateway
        self.event_java = event_java
        self.active_client = active_client
        self.categorie_selectata = categorie_selectata
        self.user_email = user_email
        self.setupUi()

    def setupUi(self):
        self.setObjectName("EventBookWindow")
        self.resize(1200, 1000)

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
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.layout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.layout_main.setContentsMargins(60, 50, 60, 50)
        self.layout_main.setSpacing(30)

        self.lbl_success_title = QtWidgets.QLabel("🎉 Booking Confirmed!")
        self.lbl_success_title.setStyleSheet("font-size: 48px; font-weight: 750; color: #1e1b4b; text-align: center;")
        self.lbl_success_title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_main.addWidget(self.lbl_success_title)

        self.lbl_email_notice = QtWidgets.QLabel(f"A digital ticket has been sent to:\n{self.user_email}")
        self.lbl_email_notice.setStyleSheet("font-size: 28px; color: #475569; font-weight: 500; line-height: 140%;")
        self.lbl_email_notice.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_main.addWidget(self.lbl_email_notice)

        self.ticket_card = QtWidgets.QFrame()
        self.ticket_card.setObjectName("TicketCard")
        self.ticket_card.setStyleSheet("""
            #TicketCard {
                background-color: #f3f4f6;
                border: 2px dashed #cbd5e1;
                border-radius: 28px;
            }
        """)
        self.ticket_layout = QtWidgets.QVBoxLayout(self.ticket_card)
        self.ticket_layout.setContentsMargins(45, 45, 45, 45)
        self.ticket_layout.setSpacing(25)

        self.lbl_event_name = QtWidgets.QLabel(self.event_java.getName())
        self.lbl_event_name.setStyleSheet("font-size: 38px; font-weight: 750; color: #1e1b4b; background: transparent")
        self.lbl_event_name.setWordWrap(True)
        self.ticket_layout.addWidget(self.lbl_event_name)

        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.HLine)
        line1.setStyleSheet("background-color: #cbd5e1; max-height: 1px;")
        self.ticket_layout.addWidget(line1)

        try:
            locatie_completa = f"Location: {self.event_java.getLocation()}, {self.event_java.getCity()}"
        except Exception:
            locatie_completa = f"Location: {self.event_java.getLocation()}"

        self.lbl_ticket_venue = QtWidgets.QLabel(locatie_completa)
        self.lbl_ticket_venue.setStyleSheet("font-size: 28px; font-weight: 600; color: #1e1b4b; background: transparent")
        self.lbl_ticket_venue.setWordWrap(True)
        self.ticket_layout.addWidget(self.lbl_ticket_venue)

        self.lbl_ticket_date = QtWidgets.QLabel(f"Date: {self.event_java.getDateTime()}")
        self.lbl_ticket_date.setStyleSheet("font-size: 28px; font-weight: 600; color: #1e1b4b; background: transparent")
        self.ticket_layout.addWidget(self.lbl_ticket_date)

        line2 = QtWidgets.QFrame()
        line2.setFrameShape(QtWidgets.QFrame.HLine)
        line2.setStyleSheet("background-color: #cbd5e1; max-height: 1px;")
        self.ticket_layout.addWidget(line2)

        try:
            person = self.active_client.getPerson()
            nume_complet = f"Attendee: {person.getLast_name()} {person.getFirst_name()}"
        except Exception:
            nume_complet = "Attendee: Profile Holder"

        self.lbl_attendee = QtWidgets.QLabel(nume_complet)
        self.lbl_attendee.setStyleSheet("font-size: 28px; font-weight: 600; color: #1e1b4b; background: transparent")
        self.ticket_layout.addWidget(self.lbl_attendee)

        self.lbl_ticket_type = QtWidgets.QLabel(
            f"Ticket: {self.categorie_selectata.getTicketType()}\n\nTotal Paid: {self.categorie_selectata.getPrice()} RON"
        )
        self.lbl_ticket_type.setStyleSheet("font-size: 28px; font-weight: 600; color: #1e1b4b; line-height: 140%; background: transparent")
        self.ticket_layout.addWidget(self.lbl_ticket_type)

        self.layout_main.addWidget(self.ticket_card)

        self.layout_main.addStretch()

        self.btn_done = QtWidgets.QPushButton("Back to Event Booking")
        self.btn_done.setMinimumHeight(85)
        self.btn_done.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_done.setStyleSheet("""
            QPushButton {
                background-color: #1e1b4b; 
                color: #FFFFFF;
                font-weight: 850; 
                border-radius: 25px; 
                font-size: 24px;
                letter-spacing: 0.5px;
                border: none;
            }
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.btn_done.clicked.connect(self.handle_done)
        self.layout_main.addWidget(self.btn_done)

    def handle_done(self):
        # Dacă am primit referința către Explore, o reafișăm pe ecran
        if hasattr(self, 'explore_win') and self.explore_win is not None:
            self.explore_win.show()

        # Închidem fereastra biletului
        self.close()