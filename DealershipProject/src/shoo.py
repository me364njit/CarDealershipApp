from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, QVBoxLayout
import sys
from PyQt5 import QtGui
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Database Connection"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "home.png"

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.btn = QPushButton("DB Connection")
        self.btn.clicked.connect(self.DBConnect)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.show()

    def DBConnect(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'dealership')
            QMessageBox.about(self, "Connection", "Database Connected Successfully")

        except mdb.Error as e:
            QMessageBox.about(self, "Connect", "Failed To Connect Database")
            sys.exit(1)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
