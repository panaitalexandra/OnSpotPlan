from PyQt5 import QtWidgets, QtCore, QtGui

class BaseFramelessWindow(QtWidgets.QDialog):
    back_requested = QtCore.pyqtSignal()
    forward_requested = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1000, 1200)

        self.master_layout = QtWidgets.QVBoxLayout(self)
        self.master_layout.setContentsMargins(0, 0, 0, 0)
        self.master_layout.setSpacing(0)
        self.master_layout.setSpacing(0)

        self.title_bar = QtWidgets.QWidget()
        self.title_bar.setFixedHeight(60)
        self.title_bar.setStyleSheet("""
            QWidget {
                background-color: #1e1b4b; 
                border-top-left-radius: 20px; 
                border-top-right-radius: 20px;
            }
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
            }
            #btn_close:hover {
                background-color: #e74c3c;
            }
        """)

        self.title_layout = QtWidgets.QHBoxLayout(self.title_bar)
        # css trbl vs pyqt5 ltrb
        self.title_layout.setContentsMargins(20, 0, 20, 0)

        self.btn_close = QtWidgets.QPushButton("✕")
        self.btn_close.setObjectName("btn_close")

        self.title_layout.addStretch()
        self.title_layout.addWidget(self.btn_close)

        self.master_layout.addWidget(self.title_bar)

        self.body_widget = QtWidgets.QWidget()
        self.body_widget.setObjectName("body_widget")
        self.body_widget.setStyleSheet("""
            #body_widget {
                background-color: #f3f4f6; 
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
            }
        """)

        self.main_layout = QtWidgets.QVBoxLayout(self.body_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.master_layout.addWidget(self.body_widget)

        self.btn_close.clicked.connect(QtWidgets.QApplication.instance().quit)

    # pt label-urile de switch between log in - sign up
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'old_pos'):
            delta = QtCore.QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()