# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_base_window import BaseFramelessWindow


class Ui_CompleteProfile(BaseFramelessWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("CompleteProfileWindow")
        self.resize(1300, 1300)

        self.content_widget = QtWidgets.QWidget()
        # Setează fundalul principal al ferestrei pe alb curat
        self.content_widget.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
            }
            * {
                font-family: 'Segoe UI', sans-serif;
                color: #1e1b4b;
            }
        """)

        if hasattr(self, 'main_layout'):
            self.main_layout.addWidget(self.content_widget)

        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_main.setContentsMargins(50, 40, 50, 40)

        self.frame = QtWidgets.QFrame(self.content_widget)
        # Setează un ID unic pentru card ca să aplicăm corect fundalul gri fără efect de cascadă
        self.frame.setObjectName("CompleteProfileCard")
        self.frame.setStyleSheet("""
            #CompleteProfileCard {
                background-color: #f3f4f6; 
                border: 2px solid #cbd5e1;
                border-radius: 30px;
            }
        """)
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(15)

        self.label_title = QtWidgets.QLabel("Complete Profile")
        self.label_title.setStyleSheet("""
            font-size: 50px; 
            font-weight: bold; 
            color: #1e1b4b;
            background: transparent;
        """)
        self.layout.addWidget(self.label_title)

        self.inputs = {}
        fields = [
            ("Last Name", "e.g. Roman"),
            ("First Name", "e.g. Daniel"),
            ("National ID", "13 digits required"),
            ("Phone Number", "07..."),
            ("Region", "e.g. Constanta"),
            ("City", "e.g. Navodari")
        ]

        for label_text, placeholder in fields:
            lbl = QtWidgets.QLabel(label_text)
            lbl.setStyleSheet("""
                font-size: 24px; 
                font-weight: 600; 
                color: #4b5563; 
                margin-top: 5px;
                background: transparent;
            """)
            self.layout.addWidget(lbl)

            line_edit = QtWidgets.QLineEdit()
            line_edit.setPlaceholderText(placeholder)
            line_edit.setMinimumHeight(65)
            # Câmpurile primesc fundal alb curat pentru a face contrast premium cu fundalul gri al cardului
            line_edit.setStyleSheet("""
                QLineEdit {
                    background-color: #FFFFFF; 
                    border: 2px solid #cbd5e1; 
                    border-radius: 12px; 
                    padding: 10px 15px; 
                    font-size: 26px;
                    color: #1e1b4b;
                }
                QLineEdit:focus {
                    border: 2px solid #1e1b4b;
                }
            """)
            if label_text == "CNP":
                line_edit.setMaxLength(13)

            self.layout.addWidget(line_edit)
            self.inputs[label_text] = line_edit

        self.layout.addStretch()

        # Butonul principal plin (Save and Continue)
        self.btn_complete = QtWidgets.QPushButton("Save and Continue")
        self.btn_complete.setMinimumHeight(85)
        self.btn_complete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_complete.setStyleSheet("""
            QPushButton { 
                background-color: #1e1b4b; 
                color: white; 
                font-size: 28px; 
                font-weight: bold; 
                border-radius: 20px; 
            }
            QPushButton:hover { 
                background-color: #2e2a70; 
            }
        """)

        # Butonul secundar mare (Skip for now) - stilizat în ton cu ferestrele anterioare
        self.btn_skip = QtWidgets.QPushButton("Skip for now")
        self.btn_skip.setMinimumHeight(85)
        self.btn_skip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_skip.setStyleSheet("""
            QPushButton { 
                background-color: #FFFFFF; 
                color: #1e1b4b; 
                font-size: 26px; 
                font-weight: bold; 
                border: 2px solid #cbd5e1;
                border-radius: 20px; 
                text-decoration: none;
            }
            QPushButton:hover { 
                background-color: #f1f5f9; 
                border-color: #1e1b4b;
            }
        """)

        self.layout.addWidget(self.btn_complete)
        self.layout.addWidget(self.btn_skip)
        self.verticalLayout_main.addWidget(self.frame)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("CompleteProfileWindow", "EventHub - Complete Profile"))