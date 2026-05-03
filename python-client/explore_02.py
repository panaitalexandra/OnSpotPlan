from PyQt5 import QtWidgets, QtCore
from ui_explore import Ui_Explore
from ui_filter import Ui_Filter

class ExploreApp(QtWidgets.QDialog):
    def __init__(self, gateway, manager):
        super(ExploreApp, self).__init__()
        self.ui = Ui_Explore()
        self.ui.setupUi(self)
        self.gateway = gateway
        self.manager = manager
        self.locatie_service = self.gateway.entry_point.getLocatieService()
        self.ui.btn_filters.clicked.connect(self.selecteaza_oras)

    def selecteaza_oras(self):
        dialog = Ui_Filter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            oras = dialog.get_selection()
            if oras:
                self.actualizeaza_locatii(oras)

    def actualizeaza_locatii(self, judet_selectat):
        try:
            while self.ui.main_layout.count() > 4:  # Păstrăm header-ul și filtrele
                item = self.ui.main_layout.takeAt(4)
                if item.widget():
                    item.widget().deleteLater()

            locatii = self.locatie_service.getLocatiiDupaJudet(judet_selectat)

            for nume in locatii:
                card = self.creeaza_widget_card(nume)
                self.ui.main_layout.addWidget(card)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Eroare", f"Nu am putut încărca locațiile: {e}")

    def creeaza_widget_card(self, nume_locatie):
        card_frame = QtWidgets.QFrame()
        card_frame.setMinimumHeight(550)
        card_frame.setStyleSheet("background-color: #1e1b4b; border-radius: 40px;")

        layout = QtWidgets.QVBoxLayout(card_frame)

        lbl_nume = QtWidgets.QLabel(nume_locatie)
        lbl_nume.setStyleSheet("color: white; font-size: 48px; font-weight: bold;")

        btn_book = QtWidgets.QPushButton("Book Now")
        btn_book.setFixedSize(280, 50)
        btn_book.setStyleSheet("background-color: #3d7068; color: white; font-size: 32px;")

        btn_book.clicked.connect(lambda: self.deschide_rezervare(nume_locatie))

        layout.addWidget(lbl_nume)
        layout.addStretch()
        layout.addWidget(btn_book, 0, QtCore.Qt.AlignRight)

        return card_frame

    def deschide_rezervare(self, nume_locatie):
        QtWidgets.QMessageBox.information(self, "Rezervare", f"Ai ales să rezervi la: {nume_locatie}")
