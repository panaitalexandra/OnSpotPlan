# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
from ui_base_window import BaseFramelessWindow

class Ui_BookingApp(BaseFramelessWindow):
    def __init__(self, gateway, event_name, active_client):
        super().__init__() # Lansează BaseFramelessWindow (Frameless, TitleBar, etc.)
        self.gateway = gateway
        self.event_name = event_name
        self.active_client = active_client

        self.setupUi()

    def setupUi(self):
        self.setObjectName("BookingWindow")
        self.resize(1000, 1250)

        # Widget-ul de conținut (ancorat în body-ul alb al ferestrei mamă)
        self.content_widget = QtWidgets.QWidget()
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
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        # Layout-ul orizontal principal pentru conținut
        self.layout_horizontal = QtWidgets.QHBoxLayout(self.content_widget)
        self.layout_horizontal.setContentsMargins(40, 40, 40, 40)
        self.layout_horizontal.setSpacing(40)

        # --- PANEL STÂNGA (Calendar) ---
        self.left_panel = QtWidgets.QVBoxLayout()

        self.lbl_title = QtWidgets.QLabel(f"Select a Date for\n{self.event_name}")
        self.lbl_title.setStyleSheet("font-size: 32px; font-weight: bold; color: #38bdf8; background: transparent;")
        self.left_panel.addWidget(self.lbl_title)

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setGridVisible(False)
        self.calendar.setStyleSheet("""
            QCalendarWidget QAbstractItemView { 
                background-color: #1e293b; 
                selection-background-color: #3d7068; 
                selection-color: white;
                border-radius: 10px;
            }
            QCalendarWidget QWidget { 
                alternate-background-color: #334155; 
                color: white; 
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #1e1b4b;
                font-size: 16px;
                border-radius: 5px;
                margin: 5px;
            }
        """)
        self.calendar.selectionChanged.connect(self.update_availability)
        self.left_panel.addWidget(self.calendar)
        self.layout_horizontal.addLayout(self.left_panel, 60)

        # --- PANEL DREAPTA (Sloturi) ---
        self.right_panel = QtWidgets.QVBoxLayout()

        self.lbl_slots = QtWidgets.QLabel("Available Time Slots")
        self.lbl_slots.setStyleSheet("font-size: 22px; font-weight: bold; color: #f8fafc; background: transparent;")
        self.right_panel.addWidget(self.lbl_slots)

        self.list_slots = QtWidgets.QListWidget()
        self.list_slots.setStyleSheet("""
            QListWidget { 
                background-color: #1e293b; 
                border: 2px solid #334155;
                border-radius: 15px; 
                padding: 10px; 
                font-size: 18px; 
            }
            QListWidget::item { 
                padding: 15px; 
                border-bottom: 1px solid #334155; 
                color: #cbd5e1;
            }
            QListWidget::item:selected { 
                background-color: #3d7068; 
                color: white; 
                border-radius: 10px; 
            }
        """)
        self.list_slots.addItems(["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"])
        self.right_panel.addWidget(self.list_slots)

        self.btn_confirm = QtWidgets.QPushButton("CONFIRM BOOKING")
        self.btn_confirm.setMinimumHeight(80)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm.setStyleSheet("""
            QPushButton {
                background-color: #3d7068; 
                color: white;
                font-weight: bold; 
                border-radius: 20px; 
                font-size: 22px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: #4d8a7f;
            }
        """)
        self.btn_confirm.clicked.connect(self.handle_booking)
        self.right_panel.addWidget(self.btn_confirm)

        self.layout_horizontal.addLayout(self.right_panel, 40)

    def update_availability(self):
        selected_date = self.calendar.selectedDate().toString("dd.MM.yyyy")
        self.lbl_slots.setText(f"Slots for {selected_date}")

    def handle_booking(self):
        selected_item = self.list_slots.currentItem()
        if not selected_item:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a time slot first!")
            return

        try:
            q_date = self.calendar.selectedDate()
            java_date = self.gateway.jvm.java.time.LocalDate.of(q_date.year(), q_date.month(), q_date.day())

            time_str = selected_item.text().split(" ")[0]
            java_time = self.gateway.jvm.java.time.LocalTime.parse(time_str)

            # --- CORECȚIE TEMATICĂ ---
            # Schimbat din "Vaccin" în "Bilet" conform tematicii Event Hub
            ticket_type = self.gateway.jvm.Bilet("Standard Ticket")

            new_booking = self.gateway.jvm.Programare(
                self.active_client,
                self.event_name,
                java_date,
                java_time,
                ticket_type
            )

            manager = self.gateway.jvm.ManagerProgramari()
            is_added = manager.adaugaProgramare(new_booking)

            if is_added:
                p = self.active_client.getPersoana()
                success_msg = (
                    f"Booking Confirmed!\n\n"
                    f"Attendee: {p.getNume()} {p.getPrenume()}\n"
                    f"Event: {self.event_name}\n"
                    f"Date: {q_date.toString('dd.MM.yyyy')}\n"
                    f"Time: {time_str}"
                )
                QtWidgets.QMessageBox.information(self, "Success", success_msg)
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Conflict", "You already have a booking for this slot!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "System Error", f"Backend communication failed: {e}")