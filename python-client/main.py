import sys
from PyQt5 import QtWidgets
from py4j.java_gateway import JavaGateway, GatewayParameters
from auth_01 import LoginApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    try:
        gateway = JavaGateway()

        java_manager = gateway.entry_point.getUserManager()

        login = LoginApp(gateway, java_manager)
        login.show()

        sys.exit(app.exec_())

    except Exception as e:
        print(f"Eroare la pornire: {e}")