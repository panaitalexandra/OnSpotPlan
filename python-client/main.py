import sys
from PyQt5 import QtWidgets
from py4j.java_gateway import JavaGateway
from auth_01 import LoginApp
from explore_02 import ExploreApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    try:
        gateway = JavaGateway()
        java_manager = gateway.entry_point.getManagerUtilizatori()

        login = LoginApp(gateway, java_manager)
        login.show()

        if login.exec_() == QtWidgets.QDialog.Accepted:
            user = login.ui.lineEdit_email.text()
            dashboard = ExploreApp(gateway, java_manager, user)
            dashboard.show()

        sys.exit(app.exec_())

    except Exception as e:
        print(f"Make sure Gateway.java is running! Error occurred: {e}")