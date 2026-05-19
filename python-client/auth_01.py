from PyQt5 import QtWidgets, QtCore, QtGui
from ui_log_in import Ui_Authentification
from ui_popup_question import Ui_PopupQuestion
from ui_sign_up import Ui_Register
from ui_complete_profile import Ui_CompleteProfile
from ui_profile_selection import Ui_ProfileSelection
from ui_popup import Ui_Popup

class RegisterApp(Ui_Register):
    def __init__(self, gateway, manager):
        super().__init__()
        self.gateway = gateway
        self.manager = manager

        self.pushButton_register.clicked.connect(self.handle_signup)
        self.label_back_to_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_back_to_login.mousePressEvent = self.switch_to_login
        self.lineEdit_passwd.textChanged.connect(self.live_validation)

    def live_validation(self):
        password = self.lineEdit_passwd.text()
        v = self.gateway.jvm.PasswordValidation

        results = {
            "length": v.hasMinLength(password),
            "upper": v.containsUppercase(password),
            "digit": v.containsNum(password),
            "special": v.containsSpecial(password)
        }

        for key, met_condition in results.items():
            label = self.password_hints[key]
            if met_condition:
                label.setStyleSheet("color: #22c55e; font-size: 20px; font-weight: bold;")
                label.setText(label.text().replace("●", "✔"))
            else:
                label.setStyleSheet("color: #94a3b8; font-size: 20px;")
                label.setText(label.text().replace("✔", "●"))

    def handle_signup(self):
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_passwd.text()
        confirmation = self.lineEdit_confirm_passwd.text()

        if not email or not password or not confirmation:
            self.popup = Ui_Popup("Please fill in all fields!", title="Error", parent=self)
            self.popup.exec_()
            return

        if password != confirmation:
            self.popup = Ui_Popup("Passwords do not match!", title="Error", parent=self)
            self.popup.exec_()
            return

        try:
            new_user = self.manager.storeUser(email, password)

            if new_user is not None:
                self.popup = Ui_Popup("Account created successfully!", title="Success", parent=self)
                self.popup.exec_()

                self.complete_win = CompleteProfileApp(self.gateway, self.manager, email)
                if self.complete_win.exec_() == QtWidgets.QDialog.Accepted:
                    from explore_02 import ExploreApp
                    self.dashboard = ExploreApp(self.gateway, self.manager, email)
                    self.dashboard.show()
                    self.accept()
            else:
                self.popup = Ui_Popup("Registration failed. Please try again.", title="Error", parent=self)
                self.popup.exec_()

        except Exception as e:
            error_message = str(e)
            if "INVALID_EMAIL_FORMAT" in error_message:
                display_text = "The email address format is invalid. Please enter a valid email."
            elif "EMAIL_ALREADY_EXISTS" in error_message:
                display_text = "This email address is already registered to another account."
            elif "WEAK_PASSWORD" in error_message:
                display_text = "The password does not meet the security requirements (must include uppercase letters, numbers, and special characters)."
            else:
                display_text = f"Registration error: {error_message}"

            self.popup = Ui_Popup(display_text, title="Registration Failed", parent=self)
            self.popup.exec_()

    def switch_to_login(self, event):
        self.login_window = LoginApp(self.gateway, self.manager)
        self.login_window.show()
        self.close()

class LoginApp(Ui_Authentification):
    def __init__(self, gateway, manager):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.pushButton_login.clicked.connect(self.handle_login)
        self.label_signin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_signin.mousePressEvent = self.switch_to_signup

    def handle_login(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_passwd.text()


        if not email or not password:
            self.popup = Ui_Popup("Please fill in all fields!", title="Error", parent=self)
            self.popup.exec_()
            return

        try:
            user = self.manager.getUser(email, password)

            if user is not None:
                from explore_02 import ExploreApp
                self.dashboard = ExploreApp(self.gateway, self.manager, email)
                self.dashboard.show()
                self.accept()

        except Exception as e:
            error_message = str(e)

            if "EMAIL_NOT_FOUND" in error_message:
                display_text = "This email address was not found in our system."
            elif "INCORRECT_PASSWORD" in error_message:
                display_text = "The password you entered is incorrect. Please try again."
            else:
                display_text = f"Authentication failed: {error_message}"

            self.popup = Ui_Popup(display_text, title="Login Failed", parent=self)
            self.popup.exec_()

    def switch_to_signup(self, event):
        self.signup_window = RegisterApp(self.gateway, self.manager)
        self.signup_window.show()
        self.close()


class ProfileSelectionApp(Ui_ProfileSelection):
    def __init__(self, gateway, manager, email):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email

        self.btn_add.clicked.connect(self.handle_add_profile)
        self.btn_delete.clicked.connect(self.handle_delete_profile)
        self.btn_view.clicked.connect(self.handle_view_details)
        self.btn_select.clicked.connect(self.handle_select)

        if hasattr(self, 'btn_back_explore'):
            self.btn_back_explore.clicked.connect(self.handle_back_to_explore)
        elif hasattr(self, 'btn_back'):  # Alternativa 1
            self.btn_back.clicked.connect(self.handle_back_to_explore)
        elif hasattr(self, 'btn_close'):  # Alternativa 2
            self.btn_close.clicked.connect(self.handle_back_to_explore)

        self.load_profiles()

    def handle_select(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.popup = Ui_Popup("Choose a profile!", title="Selection", parent=self)
            self.popup.exec_()
            return

        try:
            manager_profil = self.gateway.getProfileManager(self.current_user_email)
            profile_list = manager_profil.getProfileList()
            selected_profile = profile_list.get(selected_row)

            if hasattr(self, 'explore_parent') and self.explore_parent is not None:
                self.explore_parent.active_client = selected_profile
                self.explore_parent.set_default_profile()
                self.explore_parent.show()
            else:
                from explore_02 import ExploreApp
                self.explore_win = ExploreApp(self.gateway, self.manager, self.current_user_email)
                self.explore_win.active_client = selected_profile
                self.explore_win.set_default_profile()
                self.explore_win.show()

            self.close()

        except Exception as e:
            import traceback
            traceback.print_exc()
            self.popup = Ui_Popup(f"Error switching profile: {e}", title="Error", parent=self)
            self.popup.exec_()

    def handle_back_to_explore(self):
        try:
            from explore_02 import ExploreApp
            self.explore_win = ExploreApp(self.gateway, self.manager, self.current_user_email)
            self.explore_win.show()
            self.close()
        except Exception as e:
            self.popup = Ui_Popup(f"Error returning to Explore: {e}", title="Error")
            self.popup.exec_()

    def load_profiles(self):
        manager = self.gateway.getProfileManager(self.current_user_email)
        users = manager.getProfileList()

        self.table.setRowCount(0)
        for i in range(users.size()):
            client = users.get(i)
            p = client.getPerson()

            self.table.insertRow(i)
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(p.getLast_name()))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(p.getFirst_name()))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(p.getNationalId()))

    def handle_add_profile(self):
        manager = self.gateway.getProfileManager(self.current_user_email)
        if manager.getProfileList().size() >= 10:
            self.popup = Ui_Popup("You can only have up to 10 profiles.!", title="Limit Reached")
            self.popup.show()
            return

        from auth_01 import CompleteProfileApp
        add_win = CompleteProfileApp(self.gateway, manager, self.current_user_email)
        if add_win.exec_() == QtWidgets.QDialog.Accepted:
            self.load_profiles()

    def handle_delete_profile(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.popup = Ui_Popup("Please select a profile to delete!", title="Selection Required")
            self.popup.show()
            return

        self.confirm_popup = Ui_PopupQuestion(
            "Are you sure you want to delete this profile? This action cannot be undone.",
            title="Confirm Delete"
        )

        if self.confirm_popup.exec_() == QtWidgets.QDialog.Accepted:
            try:
                profile_manager = self.gateway.getProfileManager(self.current_user_email)

                success = profile_manager.deleteProfile(selected_row)

                if success:
                    self.popup = Ui_Popup("Profile deleted successfully.", title="Success")
                    self.popup.show()
                    self.load_profiles()
                else:
                    self.popup = Ui_Popup("Could not delete profile.", title="Error")
                    self.popup.show()

            except Exception as e:
                self.popup = Ui_Popup(f"Java error: {e}", title="System Error")
                self.popup.show()

    def handle_view_details(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.popup = Ui_Popup("Select a profile first!", title="Selection")
            self.popup.show()
            return

        from explore_02 import ProfileApp

        self.details_win = ProfileApp(
            self.gateway,
            self.manager,
            self.current_user_email,
            index=selected_row
        )

        self.details_win.exec_()
        self.load_profiles()

class CompleteProfileApp(Ui_CompleteProfile):
    def __init__(self, gateway, manager,email, profile_index=None):
        super().__init__()
        self.gateway = gateway
        self.manager = manager
        self.current_user_email = email
        self.profile_index = profile_index

        if self.profile_index is not None:
            self.label_title.setText("Modify Profile")
            self.btn_complete.setText("Update and Save")
            self.incarca_date_existente()

        self.btn_complete.clicked.connect(self.handle_completion)
        self.btn_skip.clicked.connect(self.accept)

    def incarca_date_existente(self):
        try:
            manager_clienti = self.gateway.getProfileManager(self.current_user_email)
            list = manager_clienti.getProfileList()
            client = list.get(self.profile_index)
            p = client.getPerson()

            if "Last Name" in self.inputs:
                self.inputs["Last Name"].setText(p.getLast_name())
            if "First Name" in self.inputs:
                self.inputs["First Name"].setText(p.getFirst_name())
            if "National ID" in self.inputs:
                self.inputs["National ID"].setText(p.getNationalId())
            if "Phone Number" in self.inputs:
                self.inputs["Phone Number"].setText(client.getPhone_number())
            if "Region" in self.inputs:
                self.inputs["Region"].setText(p.getRegion())
            if "City" in self.inputs:
                self.inputs["City"].setText(p.getCity())

        except Exception as e:
            self.popup = Ui_Popup(f"Eroare la pre-completarea datelor: {e}", title="Error")
            self.popup.show()

    def handle_completion(self):
        try:
            data = {k: v.text().strip() for k, v in self.inputs.items()}

            if not all(data.values()):
                self.popup = Ui_Popup("All fields must be completed!", title="Error", parent=self)
                self.popup.exec_()
                return

            cnp_key = "National ID" if "National ID" in data else "CNP"
            cnp_text = data[cnp_key].strip()

            if len(cnp_text) < 5 or len(cnp_text) > 20 or not cnp_text.isalnum():
                self.popup = Ui_Popup(
                    "The National ID format is invalid. It must be between 5 and 20 characters long and contain only alphanumeric characters.",
                    title="Invalid ID",
                    parent=self
                )
                self.popup.exec_()
                return

            client_java = self.gateway.jvm.Profile(
                data["Last Name"],
                data["First Name"],
                data[cnp_key],
                data["Phone Number"],
                data["Region"],
                data["City"]
            )

            profile_manager = self.gateway.getProfileManager(self.current_user_email)
            if self.profile_index is not None:
                success = profile_manager.updateProfile(self.profile_index, client_java)
            else:
                success = profile_manager.addProfile(client_java)

            if success:
                self.accept()
            else:
                self.popup = Ui_Popup(
                    "The profile could not be saved. Please verify your information and try again.",
                    title="Save Failed",
                    parent=self
                )
                self.popup.exec_()

        except Exception as e:
            import traceback
            print("--- DETALII EROARE ÎN CONSOLĂ ---")
            traceback.print_exc()

            if hasattr(e, 'java_exception') and e.java_exception is not None:
                display_text = e.java_exception.getMessage()
            else:
                err_msg = str(e)
                display_text = err_msg.split(":", 1)[1].strip() if ":" in err_msg else err_msg

            if not display_text or any(x in str(e).lower() for x in ["javapackage", "py4jerror"]) and not hasattr(e,
                                                                                                                  'java_exception'):
                display_text = "A communication error occurred with the database. Please make sure the input data format is acceptable."
                title_text = "System Error"
            else:
                if "already registered" in display_text.lower():
                    title_text = "Duplicate Profile"
                elif "phone number" in display_text.lower():
                    title_text = "Invalid Phone"
                elif "national id" in display_text.lower() or "cnp" in display_text.lower():
                    title_text = "Invalid ID"
                else:
                    title_text = "Validation Error"

            self.popup = Ui_Popup(display_text, title=title_text, parent=self)
            self.popup.exec_()

    def handle_skip(self):
        self.open_explore()

    def open_explore(self):
        from explore_02 import ExploreApp
        self.dashboard = ExploreApp(self.gateway, self.manager, self.current_user_email)
        self.dashboard.show()
        self.accept()