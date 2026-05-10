from PyQt5 import QtWidgets, QtCore, QtGui
from ui_log_in import Ui_Authentification
from ui_sign_up import Ui_Register
from ui_complete_profile import Ui_CompleteProfile
from ui_profile_selection import Ui_ProfileSelection

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
        parola = self.lineEdit_passwd.text()

        # Referință scurtă către clasa Java prin Gateway
        v = self.gateway.jvm.ValidatorParola

        # Verificăm fiecare condiție apelând Java
        results = {
            "length": v.areLungimeMinima(parola),
            "upper": v.areMajuscula(parola),
            "digit": v.areCifra(parola),
            "special": v.areCaracterSpecial(parola)
        }

        # Actualizăm culorile în UI pe baza răspunsului Java
        for key, met_condition in results.items():
            label = self.password_hints[key]
            if met_condition:
                label.setStyleSheet("color: #22c55e; font-size: 18px; font-weight: bold;")  # Verde
                label.setText(label.text().replace("●", "✔"))
            else:
                label.setStyleSheet("color: #94a3b8; font-size: 18px;")  # Gri înapoi
                label.setText(label.text().replace("✔", "●"))
    def handle_signup(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_passwd.text()
        confirmation = self.lineEdit_confirm_passwd.text()

        if password != confirmation:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        try:
            if not self.manager.isEmailValid(email):
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid email format!")
                return

            if not self.manager.isParolaValida(password):
                QtWidgets.QMessageBox.warning(self, "Error", "Password does not meet security requirements!")
                return

            new_user = self.manager.inregistreazaUtilizator(email, password)

            if new_user is not None:
                QtWidgets.QMessageBox.information(self, "Success", "Account created successfully!")
                self.complete_win = CompleteProfileApp(self.gateway, self.manager, email)
                if self.complete_win.exec_() == QtWidgets.QDialog.Accepted:
                    from explore_02 import ExploreApp
                    self.dashboard = ExploreApp(self.gateway, self.manager, email)
                    self.dashboard.show()
                    self.accept()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Registration failed!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Communication Error", f"Details: {e}")

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
            user = self.manager.getUtilizator(email, password)

            if user is not None:
                from explore_02 import ExploreApp
                self.dashboard = ExploreApp(self.gateway, self.manager, email)
                self.dashboard.show()
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Invalid email or password!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Java communication failed: {e}")

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
            QtWidgets.QMessageBox.warning(self, "Selection", "Choose a profile!")
            return

        manager = self.gateway.getManagerClienti(self.current_user_email)
        lista = manager.getLista()

        self.selected_client = lista.get(selected_row)

        self.accept()

    def load_profiles(self):
        manager = self.gateway.getManagerClienti(self.current_user_email)
        lista_beneficiari = manager.getLista()

        self.table.setRowCount(0)
        for i in range(lista_beneficiari.size()):
            client = lista_beneficiari.get(i)
            persoana = client.getPersoana()

            self.table.insertRow(i)
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(persoana.getNume()))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(persoana.getPrenume()))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(persoana.getCNP()))

    def handle_add_profile(self):
        manager = self.gateway.getManagerClienti(self.current_user_email)
        if manager.getLista().size() >= 10:
            QtWidgets.QMessageBox.warning(self, "Limit Reached", "You can only have up to 10 profiles.")
            return

        from auth_01 import CompleteProfileApp
        add_win = CompleteProfileApp(self.gateway, manager, self.current_user_email)
        if add_win.exec_() == QtWidgets.QDialog.Accepted:
            self.load_profiles()

    def handle_delete_profile(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection Required", "Please select a profile to delete.")
            return

        # Cerem confirmare (UX bun)
        reply = QtWidgets.QMessageBox.question(
            self, 'Confirm Delete',
            "Are you sure you want to delete this profile? This action cannot be undone.",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                manager_clienti = self.gateway.getManagerClienti(self.current_user_email)

                # IMPORTANT: Verifică dacă în Java metoda se numește stergeClient sau removeClient
                success = manager_clienti.stergeClient(selected_row)

                if success:
                    QtWidgets.QMessageBox.information(self, "Success", "Profile deleted successfully.")
                    self.load_profiles()  # Refresh tabel
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "Could not delete profile.")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "System Error", f"Java error: {e}")
    def handle_view_details(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Selection", "Select a profile first!")
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
            self.incarca_date_existente()  # Apelăm funcția de pre-completare

        self.btn_complete.clicked.connect(self.handle_completion)
        self.btn_skip.clicked.connect(self.accept)

    def incarca_date_existente(self):
        try:
            # Luăm managerul și lista de la Java
            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            lista = manager_clienti.getLista()
            client = lista.get(self.profile_index)
            p = client.getPersoana()

            # Punem textul existent în casetele de input folosind dicționarul self.inputs
            if "Last Name" in self.inputs:
                self.inputs["Last Name"].setText(p.getNume())
            if "First Name" in self.inputs:
                self.inputs["First Name"].setText(p.getPrenume())
            if "CNP" in self.inputs:
                self.inputs["CNP"].setText(p.getCNP())
            if "Phone Number" in self.inputs:
                self.inputs["Phone Number"].setText(client.getTelefon())
            if "County" in self.inputs:
                # Folosește getRegion() sau getJudet() în funcție de ce ai în Java
                self.inputs["County"].setText(p.getRegion())
            if "City" in self.inputs:
                self.inputs["City"].setText(p.getLocalitate())

        except Exception as e:
            print(f"Eroare la pre-completarea datelor: {e}")

    def handle_completion(self):
        try:
            data = {k: v.text().strip() for k, v in self.inputs.items()}

            if not all(data.values()):
                QtWidgets.QMessageBox.warning(self, "Eroare", "All fields must be completed!")
                return

            if len(data["CNP"]) != 13 or not data["CNP"].isdigit():
                QtWidgets.QMessageBox.warning(self, "Eroare", "Invalid cnp!")
                return

            client_java = self.gateway.jvm.Client(
                data["Last Name"],
                data["First Name"],
                data["CNP"],
                "N/A",
                "N/A",
                data["County"],
                data["City"],
                data["Phone Number"]
            )

            varsta = client_java.getVarsta()
            if varsta < 0:
                QtWidgets.QMessageBox.critical(self, "Eroare", "CNP invalid!")
                return

            manager_clienti = self.gateway.getManagerClienti(self.current_user_email)
            if self.profile_index is not None:
                manager_clienti.actualizeazaClient(self.profile_index, client_java)
            else:
                manager_clienti.adaugaClient(client_java)
            self.accept()

        except KeyError as e:
            QtWidgets.QMessageBox.critical(self, "Eroare UI", f"no input: {str(e)}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Crash", f"Err compatibilitye: {str(e)}")

    def handle_skip(self):
        self.open_explore()

    def open_explore(self):
        from explore_02 import ExploreApp
        self.dashboard = ExploreApp(self.gateway, self.manager, self.current_user_email)
        self.dashboard.show()
        self.accept()