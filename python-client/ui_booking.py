from PyQt5 import QtWidgets, QtCore, QtGui
import datetime


class Ui_BookingApp(QtWidgets.QDialog):
    def __init__(self, gateway, event_name, active_client):
        super().__init__()
        self.gateway = gateway
        self.event_name = event_name
        self.active_client = active_client

        self.setWindowTitle(f"Book Your Spot - {event_name}")
        self.resize(1000, 700)
        self.setStyleSheet("background-color: #0f172a; color: white; font-family: 'Segoe UI';")

        self.layout = QtWidgets.QHBoxLayout(self)

        self.left_panel = QtWidgets.QVBoxLayout()

        self.lbl_title = QtWidgets.QLabel(f"Select a Date for\n{event_name}")
        self.lbl_title.setStyleSheet("font-size: 28px; font-weight: bold; color: #38bdf8;")
        self.left_panel.addWidget(self.lbl_title)

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet("""
            QCalendarWidget QAbstractItemView { background-color: #1e293b; selection-background-color: #3d7068; }
            QCalendarWidget QWidget { alternate-background-color: #334155; color: white; }
        """)
        self.calendar.selectionChanged.connect(self.update_availability)
        self.left_panel.addWidget(self.calendar)
        self.layout.addLayout(self.left_panel, 60)  # Ocupă 60% din lățime

        self.right_panel = QtWidgets.QVBoxLayout()

        self.lbl_slots = QtWidgets.QLabel("Available Time Slots")
        self.lbl_slots.setStyleSheet("font-size: 20px; font-weight: bold; margin-top: 10px;")
        self.right_panel.addWidget(self.lbl_slots)

        self.list_slots = QtWidgets.QListWidget()
        self.list_slots.setStyleSheet("""
            QListWidget { background-color: #1e293b; border-radius: 15px; padding: 10px; font-size: 18px; }
            QListWidget::item { padding: 15px; border-bottom: 1px solid #334155; }
            QListWidget::item:selected { background-color: #3d7068; color: white; border-radius: 10px; }
        """)
        self.list_slots.addItems(["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM", "04:00 PM"])
        self.right_panel.addWidget(self.list_slots)

        self.btn_confirm = QtWidgets.QPushButton("CONFIRM BOOKING")
        self.btn_confirm.setMinimumHeight(70)
        self.btn_confirm.setStyleSheet(
            "background-color: #3d7068; font-weight: bold; border-radius: 15px; font-size: 20px;")
        self.btn_confirm.clicked.connect(self.handle_booking)
        self.right_panel.addWidget(self.btn_confirm)

        self.layout.addLayout(self.right_panel, 40)  # Ocupă 40% din lățime

    def update_availability(self):
        selected_date = self.calendar.selectedDate().toString("dd.MM.yyyy")
        self.lbl_slots.setText(f"Available Slots for {selected_date}")

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

            ticket_type = self.gateway.jvm.Vaccin("Standard Ticket")

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
                    f"Location: {self.event_name}\n"
                    f"Date: {q_date.toString('dd.MM.yyyy')}\n"
                    f"Time: {time_str}"
                )
                QtWidgets.QMessageBox.information(self, "Success", success_msg)
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Duplicate Booking", "A booking already exists for this profile at the selected time!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "System Error", f"Failed to communicate with Java backend: {e}")