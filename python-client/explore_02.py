# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from ui_explore import Ui_Explore
from ui_filter import Ui_Filter
from ui_open_profile import Ui_OpenProfile
from ui_event import Ui_Event
from ui_popup import Ui_Popup
from ui_popup_question import Ui_PopupQuestion


class ExploreApp(Ui_Explore):
    def __init__(self, gateway, manager, email):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.active_client = None
        self.update_categories()

        self.btn_filters.clicked.connect(self.filter_city)
        self.btn_profile.clicked.connect(self.open_profile)
        self.btn_logout.clicked.connect(self.handle_logout)

        self.lineEdit_search.textChanged.connect(self.update_search)

        self.set_default_profile()

        if "all events" in self.category_buttons:
            self.category_buttons["all events"].clicked.connect(lambda: self.update_events("All Cities", "city"))
        if "music" in self.category_buttons:
            self.category_buttons["music"].clicked.connect(lambda: self.update_events("Music", "type"))
        if "tech" in self.category_buttons:
            self.category_buttons["tech"].clicked.connect(lambda: self.update_events("Tech", "type"))
        if "food" in self.category_buttons:
            self.category_buttons["food"].clicked.connect(lambda: self.update_events("Food", "type"))

        self.update_events("All Cities", "city")

    def update_categories(self):
        try:
            while self.cat_layout.count():
                item = self.cat_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            self.category_buttons = {}

            manager_ev = self.gateway.jvm.EventManager.getInstance()
            events = manager_ev.getAllEvents()
            categories = set()

            for i in range(events.size()):
                event_java = events.get(i)
                if event_java.getType():
                    categories.add(event_java.getType().strip().title())

            category_list = sorted(list(categories))

            btn_all = QtWidgets.QPushButton("All Events")
            self.style_category_button(btn_all)
            btn_all.clicked.connect(lambda: self.update_events("All Cities", "city"))
            self.cat_layout.addWidget(btn_all)

            visible = 3
            visible_categories = category_list[:visible]
            hidden_categories = category_list[visible:]

            for cat in visible_categories:
                btn = QtWidgets.QPushButton(cat)
                self.style_category_button(btn)
                btn.clicked.connect(lambda checked, c=cat: self.update_events(c, "type"))
                self.cat_layout.addWidget(btn)

            if hidden_categories:
                btn_more = QtWidgets.QPushButton("More ▾")
                self.style_category_button(btn_more)

                more_menu = QtWidgets.QMenu(self)
                more_menu.setStyleSheet("""
                    QMenu {
                        background-color: #1e293b;
                        border: 2px solid #334155;
                        border-radius: 15px;
                        padding: 10px;
                    }
                    QMenu::item {
                        color: #B7C8E1;
                        font-size: 22px;
                        padding: 15px 30px;
                        background-color: transparent;
                    }
                    QMenu::item:selected {
                        background-color: #3d7068;
                        color: white;
                        border-radius: 10px;
                    }
                """)

                for hidden_cat in hidden_categories:
                    action = more_menu.addAction(hidden_cat)
                    action.triggered.connect(lambda checked, c=hidden_cat: self.update_events(c, "type"))

                btn_more.setMenu(more_menu)
                self.cat_layout.addWidget(btn_more)

            self.cat_layout.addStretch()

        except Exception as e:
            self.popup = Ui_Popup(f"Error generating categories dynamically: {e}", title="Error")
            self.popup.show()

    def style_category_button(self, button):
        button.setMinimumHeight(70)
        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setStyleSheet("""
            QPushButton {
                background-color: white; color: #4b5563; 
                border: 2px solid #d1d5db; border-radius: 35px; 
                padding: 0 40px; font-size: 26px; font-weight: 600;
            }
            QPushButton:hover { background-color: #f1f5f9; color: #1e1b4b; border-color: #cbd5e1; }
            QPushButton::menu-indicator { image: none; } 
        """)

    def set_default_profile(self):
        try:
            client_manager = self.gateway.getProfileManager(self.current_user_email)
            client_list = client_manager.getProfileList()

            if not client_list.isEmpty():
                self.active_client = client_list.get(0)
                p = self.active_client.getPerson()

                full_name = f"{p.getLast_name()} {p.getFirst_name()}"
                self.lbl_active_user.setText(f"Signed in as, {full_name}")
                self.lbl_active_user.setStyleSheet("color: #1e1b4b; font-weight:500; font-size: 26px;")
            else:
                self.lbl_active_user.setText("No profile selected")
        except Exception as e:
            self.popup = Ui_Popup(f"Please select profile: {e}", title="Error")
            self.popup.show()

    def open_profile(self):
        try:
            from auth_01 import ProfileSelectionApp

            self.selection_win = ProfileSelectionApp(self.gateway, self.manager, self.current_user_email)
            self.selection_win.explore_parent = self
            self.selection_win.show()
            self.hide()

        except Exception as e:
            self.popup = Ui_Popup(f"Error: {e}", title="Error")
            self.popup.show()

    def handle_logout(self):
        self.logout_popup = Ui_PopupQuestion(
            "Are you sure you want to log out?",
            title="Logout"
        )
        if hasattr(self.logout_popup, 'btn_confirm'):
            self.logout_popup.btn_confirm.setText("Yes, Log Out")

        if self.logout_popup.exec_() == QtWidgets.QDialog.Accepted:
            from auth_01 import LoginApp
            self.login_win = LoginApp(self.gateway, self.manager)
            self.login_win.show()
            self.close()

    def filter_city(self):
        try:
            manager_ev = self.gateway.jvm.EventManager.getInstance()
            event_list = manager_ev.getAllEvents()
            unique_cities = set()

            for i in range(event_list.size()):
                event_java = event_list.get(i)
                city_text = event_java.getCity()
                if city_text:
                    unique_cities.add(city_text.strip().title())

            dialog_city_list = ["All Cities"] + sorted(list(unique_cities))

            dialog = Ui_Filter(self, orase_dinamice=dialog_city_list)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                chosen_city = dialog.get_selection()
                if chosen_city:
                    self.update_events(chosen_city, "city")
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.popup = Ui_Popup(f"Could not load cities from DB: {e}", title="Filter Error")
            self.popup.show()
            dialog = Ui_Filter(self)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                oras = dialog.get_selection()
                if oras:
                    self.update_events(oras, "type")

    def update_search(self, text):
        self.update_events(text, filter_type="search")

    def update_events(self, filter_value, filter_type="type"):
        try:
            while self.events_list_layout.count():
                item = self.events_list_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            manager_ev = self.gateway.jvm.EventManager.getInstance()
            event_list = manager_ev.getAllEvents()

            displayed_card_count = 0

            for i in range(event_list.size()):
                event_java = event_list.get(i)
                show_event = False

                if filter_value == "All" or filter_value == "All Cities":
                    show_event = True

                elif filter_type == "city":
                    if event_java.getCity() and filter_value.lower() == event_java.getCity().lower():
                        show_event = True

                elif filter_type == "type":
                    if event_java.getType() and filter_value.lower() == event_java.getType().lower():
                        show_event = True

                elif filter_type == "search":
                    if not filter_value.strip():
                        show_event = True
                    else:
                        search_term = filter_value.lower()
                        in_name = search_term in event_java.getName().lower() if event_java.getName() else False
                        in_location = search_term in event_java.getLocation().lower() if event_java.getLocation() else False
                        in_description = search_term in event_java.getDescription().lower() if event_java.getDescription() else False
                        if in_name or in_location or in_description:
                            show_event = True

                if show_event:
                    card = self.create_real_card_widget(event_java, displayed_card_count)
                    self.events_list_layout.addWidget(card)
                    displayed_card_count += 1

        except Exception as e:
            import traceback
            traceback.print_exc()
            self.popup = Ui_Popup(f"Could not load events: {e}", title="Error")
            self.popup.show()

    def update_locations(self, selected_county):
        self.update_events(selected_county, "city")

    def create_real_card_widget(self, event_java, card_index):
        card_frame = QtWidgets.QFrame()
        card_frame.setObjectName("EventCard")
        card_frame.setMinimumHeight(300)

        bg_color = "#f1f5f9" if card_index % 2 == 0 else "#f3f4f6"

        card_frame.setStyleSheet(f"""
            #EventCard {{
                background-color: {bg_color};
                border-radius: 40px;
                border: 1px solid #cbd5e1;
            }}
        """)

        layout = QtWidgets.QVBoxLayout(card_frame)
        layout.setContentsMargins(30, 30, 30, 30)

        lbl_name = QtWidgets.QLabel(event_java.getName())
        lbl_name.setStyleSheet("""
            background-color: transparent; 
            color: #0B1C30; 
            font-family: 'Montserrat', 'Inter', 'Segoe UI', sans-serif;
            font-size: 38px; 
            font-weight: 500; 
            letter-spacing: -0.5px;
        """)

        info_text = f"""
        <p style='line-height: 150%; margin: 0;'>
            📍 {event_java.getLocation()}<br>
            📅 {event_java.getDateTime()}
        </p>
        """
        lbl_info = QtWidgets.QLabel()
        lbl_info.setText(info_text)
        lbl_info.setStyleSheet("""
            background-color: transparent; 
            color: #213145; 
            font-family: 'Inter', 'Segoe UI', sans-serif;
            font-size: 26px; 
            font-weight: 300;
        """)

        btn_view = QtWidgets.QPushButton("View Details")
        btn_view.setFixedSize(350, 70)
        btn_view.setStyleSheet("""
            QPushButton {
                background-color: #1e1b4b; 
                color: #EAF1FF; 
                font-family: 'Inter', 'Segoe UI', sans-serif;
                font-size: 26px; 
                font-weight: 500; 
                border-radius: 20px;
            }
            QPushButton:hover { background-color: #2e2a70; }
        """)

        btn_view.clicked.connect(lambda checked, ev=event_java: self.open_event_details(ev))
        btn_view.setCursor(QtCore.Qt.PointingHandCursor)

        layout.addWidget(lbl_name)
        layout.addWidget(lbl_info)
        layout.addStretch()
        layout.addWidget(btn_view, 0, QtCore.Qt.AlignRight)

        return card_frame

    def open_event_details(self, event_java):
        self.detail_win = Ui_Event(self.gateway, event_java, self.active_client, self.current_user_email)
        self.detail_win.show()


class ProfileApp(Ui_OpenProfile):
    def __init__(self, gateway, manager, email, index=0):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.profile_index = index
        self.explore_parent = None
        self.load_profile_data()

        self.btn_modify.clicked.connect(self.open_edit_profile)
        self.btn_back_explore.clicked.connect(self.handle_back_to_explore)

        if hasattr(self, 'btn_close'):
            self.btn_close.clicked.connect(self.handle_back_to_explore)

    def load_profile_data(self):
        try:
            client_manager = self.gateway.getProfileManager(self.current_user_email)
            client_list = client_manager.getProfileList()

            if not client_list.isEmpty() and self.profile_index < client_list.size():
                profile_obj = client_list.get(self.profile_index)
                p = profile_obj.getPerson()

                self.info_labels["Full Name"].setText(f"{p.getLast_name()} {p.getFirst_name()}")

                if "National ID" in self.info_labels:
                    self.info_labels["National ID"].setText(p.getNationalId())

                self.info_labels["Phone Number"].setText(p.getPhone_number())
                self.info_labels["Region"].setText(p.getRegion())

                if "City" in self.info_labels:
                    self.info_labels["City"].setText(p.getCity())

        except Exception as e:
            self.popup = Ui_Popup(f"Err could not upload profile data: {e}", title="Error")
            self.popup.show()

    def open_edit_profile(self):
        from auth_01 import CompleteProfileApp
        self.edit_win = CompleteProfileApp(
            self.gateway,
            self.manager,
            self.current_user_email,
            profile_index=self.profile_index
        )
        if self.edit_win.exec_() == QtWidgets.QDialog.Accepted:
            self.load_profile_data()

    def handle_back_to_explore(self):
        self.close()