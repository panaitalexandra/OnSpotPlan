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
        email = self.lineEdit_email.text()
        password = self.lineEdit_passwd.text()
        confirmation = self.lineEdit_confirm_passwd.text()

        if password != confirmation:
            self.popup = Ui_Popup("Passwords do not match!", title="Error")
            self.popup.show()
            return

        try:
            if not self.manager.isEmailValid(email):
                self.popup = Ui_Popup("Invalid email format!", title="Error")
                self.popup.show()
                return

            if not self.manager.isPasswordValid(password):
                self.popup = Ui_Popup("Password does not meet security requirements!", title="Error")
                self.popup.show()
                return

            new_user = self.manager.saveUser(email, password)

            if new_user is not None:
                self.popup = Ui_Popup("Account created successfully!", title="Success")
                self.popup.show()
                self.complete_win = CompleteProfileApp(self.gateway, self.manager, email)
                if self.complete_win.exec_() == QtWidgets.QDialog.Accepted:
                    from explore_02 import ExploreApp
                    self.dashboard = ExploreApp(self.gateway, self.manager, email)
                    self.dashboard.show()
                    self.accept()
                else:
                    self.popup = Ui_Popup("Registration failed!", title="Error")
                    self.popup.show()

        except Exception as e:
            self.popup = Ui_Popup(f"Details: {e}", title="Communication Error")
            self.popup.show()

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

        try:
            user = self.manager.getUser(email, password)

            if user is not None:
                from explore_02 import ExploreApp
                self.dashboard = ExploreApp(self.gateway, self.manager, email)
                self.dashboard.show()
                self.accept()
            else:
                self.popup = Ui_Popup("Invalid email or password!", title="Error")
                self.popup.show()
        except Exception as e:
            self.popup = Ui_Popup(f"Java communication failed: {e}", title="Error")
            self.popup.show()

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

        self.load_profiles()

    def handle_select(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.popup = Ui_Popup("Choose a profile!", title="Selection")
            self.popup.show()
            return

        manager = self.gateway.getProfileManager(self.current_user_email)
        list = manager.getProfileList()

        self.selected_client = list.get(selected_row)

        self.accept()

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
                self.popup = Ui_Popup("All fields must be completed!", title="Error")
                self.popup.show()
                return

            if len(data["CNP"]) != 13 or not data["CNP"].isdigit():
                self.popup = Ui_Popup("National id", title="Error")
                self.popup.show()
                return

            client_java = self.gateway.jvm.Client(
                data["Last Name"],
                data["First Name"],
                data["National ID"],
                data["Phone Number"],
                data["Region"],
                data["City"]
            )

            age = client_java.getAge()
            if age < 0:
                self.popup = Ui_Popup("ageee", title="Error")
                self.popup.show()
                return

            profile_manager = self.gateway.getProfileManager(self.current_user_email)
            if self.profile_index is not None:
                success = profile_manager.updateProfile(self.profile_index, client_java)
            else:
                success = profile_manager.addProfile(client_java)

            if success:
                self.accept()
            else:
                self.popup = Ui_Popup("Could not save data", title="Error")
                self.popup.show()

        except Exception as e:
            err_msg = str(e)
            if "CNP_DUPLICATE" in err_msg:
                self.popup = Ui_Popup(
                    "This National ID is already registered in the database for another profile!",
                    title="Duplicate National ID"
                )
                self.popup.show()
            elif "INVALID_PHONE" in err_msg:
                self.popup = Ui_Popup(
                    "The entered phone number is invalid!\nIt must be 10 digits long and start with 07, 02, or 03.",
                    title="Invalid Phone Number"
                )
                self.popup.show()
            else:
                self.popup = Ui_Popup(f"Err compatibilitye: {err_msg}", title="Crash")
                self.popup.show()

    def handle_skip(self):
        self.open_explore()

    def open_explore(self):
        from explore_02 import ExploreApp
        self.dashboard = ExploreApp(self.gateway, self.manager, self.current_user_email)
        self.dashboard.show()
        self.accept()