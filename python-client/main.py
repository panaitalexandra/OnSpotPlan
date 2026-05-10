import sys
from PyQt5 import QtWidgets
from py4j.java_gateway import JavaGateway
from auth_01 import LoginApp
from explore_02 import ExploreApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    try:
        gateway = JavaGateway()
        java_manager = gateway.entry_point.getManagerUtilizatori()

        login = LoginApp(gateway, java_manager)
        login.show()

        sys.exit(app.exec_())  # Bucla principală pornește aici și rămâne aici.

    except Exception as e:
        print(f"Make sure Gateway.java is running! Error occurred: {e}")