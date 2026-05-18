# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
import traceback
from ui_base_window import BaseFramelessWindow
from ui_event_booked import Ui_EventBook
from ui_popup import Ui_Popup

class Ui_BookingApp(BaseFramelessWindow):
    def __init__(self, gateway, event_java, active_client, categorie_selectata, user_email):
        super().__init__()
        self.gateway = gateway
        self.event_java = event_java
        self.active_client = active_client
        self.categorie_selectata = categorie_selectata
        self.user_email = user_email
        self.setupUi()

    def setupUi(self):
        self.setObjectName("BookingWindow")
        self.resize(1300, 1000)

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

        self.layout_grid = QtWidgets.QGridLayout(self.content_widget)
        self.layout_grid.setContentsMargins(50, 50, 50, 50)
        self.layout_grid.setHorizontalSpacing(50)
        self.layout_grid.setVerticalSpacing(30)

        self.layout_grid.setColumnStretch(0, 45)
        self.layout_grid.setColumnStretch(1, 55)

        self.lbl_title = QtWidgets.QLabel(f"Confirm booking for \n{self.event_java.getName()}")
        self.lbl_title.setStyleSheet(
            "font-size: 34px; font-weight: 850; color: #1e1b4b; background: transparent; line-height: 120%;")
        self.lbl_title.setWordWrap(True)
        self.layout_grid.addWidget(self.lbl_title, 0, 0)

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setGridVisible(False)
        self.calendar.setMinimumHeight(460)
        self.calendar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: #FFFFFF;
                border: 2px solid #f3f4f6;
                border-radius: 24px;
            }
            QCalendarWidget QWidget { 
                color: #1e1b4b; 
            }
            QCalendarWidget #qt_calendar_navigationbar {
                background-color: #f3f4f6;
                border-top-left-radius: 24px;
                border-top-right-radius: 24px;
                border-bottom: 1px solid #cbd5e1;
                padding: 10px;
            }
            QCalendarWidget QToolButton {
                color: #1e1b4b;
                background-color: transparent;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #f1f5f9;
            }
            QCalendarWidget QAbstractItemView { 
                background-color: #FFFFFF; 
                font-size: 18px; 
                selection-background-color: #1e1b4b; 
                selection-color: #FFFFFF;
                border-bottom-left-radius: 24px;
                border-bottom-right-radius: 24px;
                outline: 0px;
            }
            QCalendarWidget QHeaderView::section {
                background-color: #FFFFFF;
                color: #6b7280;
                font-size: 15px;
                font-weight: bold;
                border: none;
                padding: 8px;
            }
        """)
        self.calendar.selectionChanged.connect(self.update_availability)
        self.layout_grid.addWidget(self.calendar, 1, 0)

        self.right_container = QtWidgets.QVBoxLayout()
        self.right_container.setSpacing(25)
        self.right_container.setContentsMargins(0, 0, 0, 0)

        self.details_card = QtWidgets.QFrame()
        self.details_card.setObjectName("DetailsCard")
        self.details_card.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.details_card.setStyleSheet("""
            #DetailsCard {
                background-color: #f3f4f6;
                border: 2px solid #cbd5e1;
                border-radius: 24px;
            }
        """)
        self.details_layout = QtWidgets.QVBoxLayout(self.details_card)
        self.details_layout.setContentsMargins(40, 45, 40, 45)
        self.details_layout.setSpacing(25)

        try:
            locatie = self.event_java.getLocation()
            oras = self.event_java.getCity()
            text_locatie_completa = f"📍 {locatie}, {oras}"
        except Exception as e:
            text_locatie_completa = f"📍 {self.event_java.getLocation()}"

        self.lbl_booking_venue = QtWidgets.QLabel(text_locatie_completa)
        self.lbl_booking_venue.setStyleSheet("font-size: 28px; font-weight: 500; color: #1e1b4b; background: transparent;")
        self.lbl_booking_venue.setWordWrap(True)
        self.details_layout.addWidget(self.lbl_booking_venue)

        line_venue = QtWidgets.QFrame()
        line_venue.setFrameShape(QtWidgets.QFrame.HLine)
        line_venue.setStyleSheet("background-color: #cbd5e1; max-height: 1px;")
        self.details_layout.addWidget(line_venue)

        self.lbl_slots = QtWidgets.QLabel("Booking for:")
        self.lbl_slots.setStyleSheet("font-size: 28px; font-weight: 500; color: #1e1b4b; background: transparent;")
        self.details_layout.addWidget(self.lbl_slots)

        self.lbl_ticket_info = QtWidgets.QLabel(
            f"Ticket: {self.categorie_selectata.getTicketType()}\n\n Price: {self.categorie_selectata.getPrice()} RON"
        )
        self.lbl_ticket_info.setStyleSheet("font-size: 28px; color: #1e1b4b; background: transparent; font-weight: 500; line-height: 140%;")

        self.lbl_time_detail = QtWidgets.QLabel()
        self.lbl_time_detail.setStyleSheet("font-size: 28px; background: transparent; font-weight: 700;")
        self.details_layout.addWidget(self.lbl_time_detail)

        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.HLine)
        line1.setStyleSheet("background-color: #cbd5e1; max-height: 1px;")

        self.details_layout.addWidget(line1)
        self.details_layout.addWidget(self.lbl_ticket_info)

        self.details_layout.addStretch()
        self.right_container.addWidget(self.details_card)

        self.list_slots = QtWidgets.QListWidget()
        self.list_slots.hide()
        self.right_container.addWidget(self.list_slots)

        self.btn_confirm = QtWidgets.QPushButton("CONFIRM BOOKING")
        self.btn_confirm.setMinimumHeight(85)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm.setStyleSheet("""
            QPushButton {
                background-color: #1e1b4b; 
                color: #FFFFFF;
                font-weight: 850; 
                border-radius: 22px; 
                font-size: 24px;
                letter-spacing: 0.5px;
                border: none;
            }
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.btn_confirm.clicked.connect(self.handle_booking)
        self.right_container.addWidget(self.btn_confirm)

        self.btn_back = QtWidgets.QPushButton("← Cancel Booking")
        self.btn_back.setMinimumHeight(75)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: #1e1b4b; 
                font-size: 22px; 
                font-weight: bold; 
                border: 2px solid #cbd5e1;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #f1f5f9;
                border-color: #1e1b4b;
            }
        """)
        self.btn_back.clicked.connect(self.close)
        self.right_container.addWidget(self.btn_back)

        self.layout_grid.addLayout(self.right_container, 1, 1)

        try:
            java_date_ora = self.event_java.getDateTime()

            if hasattr(java_date_ora, 'getYear'):
                year = java_date_ora.getYear()
                month = java_date_ora.getMonthValue()
                day = java_date_ora.getDayOfMonth()
                hour = java_date_ora.getHour() if hasattr(java_date_ora, 'getHour') else 20
                minute = java_date_ora.getMinute() if hasattr(java_date_ora, 'getMinute') else 0

                self.event_date = QtCore.QDate(year, month, day)
                t_obj = datetime.time(hour, minute)
                self.formatted_time_slot = t_obj.strftime("%I:%M %p")
            else:
                data_ora_str = str(java_date_ora)
                if " la ora " in data_ora_str:
                    parts = data_ora_str.split(" la ora ")
                    date_part = parts[0].strip()
                    time_part = parts[1].strip()

                    day, month, year = map(int, date_part.split("/"))
                    self.event_date = QtCore.QDate(year, month, day)

                    if len(time_part.split(":")) == 3:
                        t_obj = datetime.datetime.strptime(time_part, "%H:%M:%S")
                    else:
                        t_obj = datetime.datetime.strptime(time_part, "%H:%M")
                    self.formatted_time_slot = t_obj.strftime("%I:%M %p")
                else:
                    data_ora_str = data_ora_str.replace("T", " ")
                    dt_obj = datetime.datetime.strptime(data_ora_str, "%d/%m/%Y - %H:%M")
                    self.event_date = QtCore.QDate(dt_obj.year, dt_obj.month, dt_obj.day)
                    self.formatted_time_slot = dt_obj.strftime("%I:%M %p")

            self.calendar.blockSignals(True)
            self.calendar.setMinimumDate(self.event_date)
            self.calendar.setMaximumDate(self.event_date)
            self.calendar.setSelectedDate(self.event_date)
            self.calendar.blockSignals(False)

        except Exception as e:
            print(f"Eroare la parsarea datelor reale din DB: {e}")
            traceback.print_exc()
            self.event_date = QtCore.QDate.currentDate()
            self.formatted_time_slot = "08:00 PM"

        self.update_availability()

    def update_availability(self):
        try:
            selected_qdate = self.calendar.selectedDate()
            selected_date = selected_qdate.toString("dd.MM.yyyy")
            self.lbl_slots.setText(f"Booking for: {selected_date}")

            self.list_slots.clear()

            if hasattr(self, 'event_date') and selected_qdate == self.event_date:
                if hasattr(self, 'formatted_time_slot'):
                    self.list_slots.addItem(self.formatted_time_slot)
                    self.list_slots.setCurrentRow(0)

                    self.lbl_time_detail.setText(f"Time Session: {self.formatted_time_slot}")
                    self.lbl_time_detail.setStyleSheet("font-size: 28px; color: #1e1b4b; background: transparent; font-weight: 500;")
            else:
                item = QtWidgets.QListWidgetItem("No slots available for this date")
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable & ~QtCore.Qt.ItemIsEnabled)
                self.list_slots.addItem(item)

                self.lbl_time_detail.setText("❌ No sessions available for this date.")
                self.lbl_time_detail.setStyleSheet("font-size: 28px; color: #ef4444; font-weight: 600;")
        except Exception as e:
            print(f"Eroare prinsă în update_availability: {e}")
            traceback.print_exc()

    def handle_booking(self):
        selected_item = self.list_slots.currentItem()
        # if not selected_item or selected_item.text() == "No slots available for this date":
        #     self.popup = Ui_Popup("Please select a valid time slot!", title="Selection Error")
        #     self.popup.show()
        #     return

        try:
            q_date = self.calendar.selectedDate()
            java_date = self.gateway.jvm.java.time.LocalDate.of(q_date.year(), q_date.month(), q_date.day())

            time_str = selected_item.text()
            dt_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
            java_time = self.gateway.jvm.java.time.LocalTime.of(dt_obj.hour, dt_obj.minute)

            new_booking = self.gateway.jvm.Booking(
                self.active_client,
                self.event_java,
                java_date,
                java_time,
                self.categorie_selectata
            )

            user_id = self.gateway.jvm.UserManager.getInstance().getIdByEmail(self.user_email)

            if user_id == -1:
                self.popup = Ui_Popup(f"User with email '{self.user_email}' was not found in the database!",
                                        title="Session Error")
                self.popup.show()
                return

            manager_prog = self.gateway.jvm.BookingManager.getInstance(user_id)

            if manager_prog.addBooking(new_booking):
                self.close()

                self.success_screen = Ui_EventBook(
                    self.gateway, self.event_java, self.active_client,
                    self.categorie_selectata, self.user_email
                )
                self.success_screen.show()
        except Exception as e:
            traceback.print_exc()
            err_msg = str(e)
            if "DUPLICATE_BOOKING" in err_msg:
                self.popup = Ui_Popup("This profile has already booked a ticket for this specific event session!",
                                        title="Already Booked")
                self.popup.show()
            else:
                self.popup = Ui_Popup(f"An error occurred: {e}", title="System Error")
                self.popup.show()