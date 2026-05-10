from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow

class Ui_OpenProfile(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("OpenProfileWindow")
        self.resize(1000, 1350)

        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setStyleSheet("""
            QWidget { 
                background-color: #121212; 
                border-bottom-left-radius: 20px; 
                border-bottom-right-radius: 20px; 
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.verticalLayout_root = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_root.setContentsMargins(40, 40, 40, 40)

        self.frame = QtWidgets.QFrame(self.content_widget)
        self.frame.setStyleSheet("background-color: white; border-radius: 40px;")
        self.layout_card = QtWidgets.QVBoxLayout(self.frame)
        self.layout_card.setContentsMargins(60, 60, 60, 60)
        self.layout_card.setSpacing(30)

        self.label_title = QtWidgets.QLabel("Profile Details")
        self.label_title.setStyleSheet("""
            font-size: 75px; 
            font-weight: bold; 
            color: #1e1b4b; 
            margin-bottom: 20px;
            background: transparent;
        """)
        self.layout_card.addWidget(self.label_title)

        self.info_labels = {}
        fields = ["Full Name", "CNP", "Phone Number", "Region", "City"]

        for field in fields:
            lbl_title = QtWidgets.QLabel(field)
            lbl_title.setStyleSheet("""
                font-size: 20px; 
                font-weight: bold; 
                color: #94a3b8; 
                margin-top: 10px;
                background: transparent;
            """)
            self.layout_card.addWidget(lbl_title)

            lbl_value = QtWidgets.QLabel("Not provided")
            lbl_value.setStyleSheet("""
                font-size: 28px; 
                font-weight: 500;
                color: #1e1b4b; 
                padding: 10px 0px; 
                border-bottom: 2px solid #f1f5f9;
                background: transparent;
            """)
            self.layout_card.addWidget(lbl_value)

            self.info_labels[field] = lbl_value

        self.layout_card.addStretch()

        self.btn_modify = QtWidgets.QPushButton("Modify Profile Details")
        self.btn_modify.setMinimumHeight(110)
        self.btn_modify.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modify.setStyleSheet("""
            QPushButton { 
                background-color: #1e1b4b; 
                color: white; 
                font-size: 34px; 
                font-weight: bold; 
                border-radius: 25px; 
            } 
            QPushButton:hover { background-color: #2e2a70; }
        """)
        self.layout_card.addWidget(self.btn_modify)

        self.btn_back_explore = QtWidgets.QPushButton("Back to Explore")
        self.btn_back_explore.setMinimumHeight(90)
        self.btn_back_explore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back_explore.setStyleSheet("""
            QPushButton { 
                background-color: transparent; 
                color: #64748b; 
                font-size: 28px; 
                text-decoration: underline; 
                border: none;
            } 
            QPushButton:hover { color: #1e1b4b; }
        """)
        self.layout_card.addWidget(self.btn_back_explore)

        self.verticalLayout_root.addWidget(self.frame)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("OpenProfileWindow", "EventHub - My Profile"))