import sys
import MySQLdb as mc
import ast
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QTableWidgetItem, QMessageBox,QLineEdit, QPushButton
from PyQt5.uic import loadUi
import pyrebase

# from login import Ui_Dialog

firebaseConfig = {
    'apiKey': "AIzaSyDRpAf2Fijy56moNzZEh681bKOhomdBRD0",
    'authDomain': "authdemo-ee6e5.firebaseapp.com",
    'databaseURL': "https://authdemo-ee6e5.firebaseio.com",
    'projectId': "authdemo-ee6e5",
    'storageBucket': "authdemo-ee6e5.appspot.com",
    'messagingSenderId': "10717464976",
    'appId': "1:10717464976:web:70f145eedcf93d9683cb15",
    'measurementId': "G-473Y5Z445Y"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("dealership.ui", self)
        # self.Push.clicked.connect(self.gotoScreen2)
        self.login.clicked.connect(self.loginScreen)
        self.dataButton.clicked.connect(self.dataWindow)
        self.CarData.clicked.connect(self.NewCarWindow)

    # def gotoScreen2(self):
    #    screen2 = Request()
    #    widget.addWidget(screen2)
    #    widget.setFixedHeight(500)
    #    widget.setFixedWidth(700)
    #    widget.setCurrentIndex(widget.currentIndex()+1)

    def loginScreen(self):
        screen5 = login()
        widget.addWidget(screen5)
        widget.setFixedHeight(500)
        widget.setFixedWidth(600)
        widget.setCurrentIndex(widget.currentIndex()+1)
    # def openWindow(self):
    #    self.window = QtWidgets.QDialog()
    #    self.ui = Ui_Dialog()
    #    self.ui.setupUi(self.window)
    #    self.window.show()

    def dataWindow(self):
        screen3 = Data()
        widget.addWidget(screen3)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def NewCarWindow(self):
        screen4 = New()
        widget.addWidget(screen4)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Request(QDialog):
    def __init__(self):
        super(Request, self).__init__()
        loadUi("Request.ui", self)
        self.pushButton.clicked.connect(self.goBack)
        self.submit.clicked.connect(self.InsertData)

    def InsertData(self):
        con = mc.connect(host='localhost', user='root',
                              password='', database='dealerservices')
        with con:
            cur = con.cursor()

            cur.execute('''INSERT INTO servicing(name, email, service)
                           VALUES(%s, %s, %s)''', (''.join(self.name.text()),
                                                   ''.join(self.email.text()),
                                                   ''.join(self.service.text())))

            QMessageBox.about(self, 'Connection', 'Request Submitted Successfully')
            self.close

    def goBack(self):
        main = MainWindow2()
        widget.addWidget(main)
        widget.setFixedHeight(900)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()+1)


class New(QDialog):
    def __init__(self):
        super(New, self).__init__()
        loadUi("Models.ui", self)
        self.BMWButton.clicked.connect(self.loadBmw)
        self.backButton.clicked.connect(self.goBack)
        self.AudiButton.clicked.connect(self.loadAudi)
        self.CadillacButton.clicked.connect(self.loadCadillac)
        self.BenzButton.clicked.connect(self.loadBenz)
        self.toyButton.clicked.connect(self.loadYota)
        self.AcuraButton.clicked.connect(self.loadAcura)
        self.DodgeButton.clicked.connect(self.loadDodge)
        self.HondaButton.clicked.connect(self.loadHonda)
        self.LexusButton.clicked.connect(self.loadLexus)
        self.NissanButton.clicked.connect(self.loadNissan)
        self.FordButton.clicked.connect(self.loadFord)
        self.wagenButton.clicked.connect(self.loadWagen)

    def loadBmw(self):
        screen1 = BMW()
        widget.addWidget(screen1)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadAudi(self):
        screen2 = Audi()
        widget.addWidget(screen2)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadCadillac(self):
        screen3 = Cadillac()
        widget.addWidget(screen3)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadBenz(self):
        screen4 = Benz()
        widget.addWidget(screen4)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadYota(self):
        screen5 = Yota()
        widget.addWidget(screen5)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadAcura(self):
        screen6 = Acura()
        widget.addWidget(screen6)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadDodge(self):
        screen7 = Dodge()
        widget.addWidget(screen7)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadHonda(self):
        screen8 = Honda()
        widget.addWidget(screen8)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadLexus(self):
        screen9 = Lexus()
        widget.addWidget(screen9)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNissan(self):
        screen10 = Nissan()
        widget.addWidget(screen10)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadFord(self):
        screen11 = Ford()
        widget.addWidget(screen11)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadWagen(self):
        screen12 = Wagen()
        widget.addWidget(screen12)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goBack(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setFixedHeight(900)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()+1)


class BMW(QDialog):
    def __init__(self):
        super(BMW, self).__init__()
        loadUi("BMW.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'BMW' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'BMW' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Audi(QDialog):
    def __init__(self):
        super(Audi, self).__init__()
        loadUi("Audi.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Audi' and CarCondition = 'New'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Audi' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Cadillac(QDialog):
    def __init__(self):
        super(Cadillac, self).__init__()
        loadUi("Cadillac.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Cadillac' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Cadillac' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Benz(QDialog):
    def __init__(self):
        super(Benz, self).__init__()
        loadUi("Benz.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Mercedes-Benz' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Mercedes-Benz' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Yota(QDialog):
    def __init__(self):
        super(Yota, self).__init__()
        loadUi("yota.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Toyota' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Toyota' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Acura(QDialog):
    def __init__(self):
        super(Acura, self).__init__()
        loadUi("Acura.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Acura' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Acura' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Dodge(QDialog):
    def __init__(self):
        super(Dodge, self).__init__()
        loadUi("Dodge.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Dodge' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Dodge' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Honda(QDialog):
    def __init__(self):
        super(Honda, self).__init__()
        loadUi("Honda.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Honda' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Honda' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Lexus(QDialog):
    def __init__(self):
        super(Lexus, self).__init__()
        loadUi("Lexus.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Lexus' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Lexus' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Nissan(QDialog):
    def __init__(self):
        super(Nissan, self).__init__()
        loadUi("Nissan.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Nissan' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Nissan' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Ford(QDialog):
    def __init__(self):
        super(Ford, self).__init__()
        loadUi("Ford.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Ford' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Ford' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Wagen(QDialog):
    def __init__(self):
        super(Wagen, self).__init__()
        loadUi("Wagen.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.loadNewButton.clicked.connect(self.loadNewData)
        self.loadOldButton.clicked.connect(self.loadOldData)
        self.rqButton.clicked.connect(self.requestPage)

    def requestPage(self):
        main = carRequest()
        widget.addWidget(main)
        widget.setFixedHeight(400)
        widget.setFixedWidth(500)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loadNewData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Volkswagen' and CarCondition = 'new'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def loadOldData(self):
        try:

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("select * from cars where make = 'Volkswagen' and CarCondition = 'used'")

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Data(QDialog):
    def __init__(self):
        super(Data, self).__init__()
        loadUi("cardata.ui", self)
        self.ShowData.clicked.connect(self.loadData)
        self.BackButton.clicked.connect(self.goBack)

    def loadData(self):
        try:
            # dbname = self.lineEditDBName.text()
            # tableName = self.lineEditTableName.text()

            mydb = mc.connect(host='localhost', user='root',
                              password='', database='dealership')

            mycursor = mydb.cursor()
            mycursor.execute("Select * From cars") # .format(tableName))
            # where make = 'bmw'
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as E:
            print(E, "Error occured")

    def goBack(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setFixedHeight(900)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()+1)


class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        loadUi("login.ui",self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.createAcc.clicked.connect(self.loadAccount)
        self.backButton.clicked.connect(self.goBack)
        self.InvalidE.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            main = MainWindow2()
            widget.addWidget(main)
            widget.setFixedHeight(900)
            widget.setFixedWidth(800)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
           self.InvalidE.setVisible(True)

    def loadAccount(self):
        screen = CreateAccount()
        widget.addWidget(screen)
        widget.setFixedHeight(500)
        widget.setFixedWidth(600)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goBack(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setFixedHeight(900)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("CreateAccount.ui", self)
        self.signupButton.clicked.connect(self.createAccFunction)
        self.InvalidLabel.setVisible(False)
        self.InvalidPass.setVisible(False)
        self.backButton.clicked.connect(self.goBack)

    def createAccFunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                main = MainWindow()
                widget.addWidget(main)
                widget.setFixedHeight(900)
                widget.setFixedWidth(800)
                widget.setCurrentIndex(widget.currentIndex()+1)
            except:
                print("Invalid Email")
                self.InvalidLabel.setVisible(True)
        else:
            self.InvalidPass.setVisible(True)

    def goBack(self):
        main = login()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(600)
        widget.setCurrentIndex(widget.currentIndex()+1)


class carRequest(QDialog):
    def __init__(self):
        super(carRequest, self).__init__()
        loadUi("CarRequest.ui", self)
        self.backButton.clicked.connect(self.goBack)
        self.submit.clicked.connect(self.InsertData)

    def InsertData(self):
        con = mc.connect(host='localhost', user='root',
                              password='', database='dealerservices')
        with con:
            cur = con.cursor()

            cur.execute('''INSERT INTO CarRequest(name, email, carID)
                           VALUES(%s, %s, %s)''', (''.join(self.name.text()),
                                                   ''.join(self.email.text()),
                                                   ''.join(self.carID.text())))

            QMessageBox.about(self, 'Connection', 'Request Submitted Successfully')
            self.close

    def goBack(self):
        main = New()
        widget.addWidget(main)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1100)
        widget.setCurrentIndex(widget.currentIndex()+1)


class MainWindow2(QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        loadUi("dealership2.ui", self)
        self.Push.clicked.connect(self.gotoScreen2)
        # self.profile.clicked.connect(self.loginScreen)
        self.dataButton.clicked.connect(self.dataWindow)
        self.CarData.clicked.connect(self.NewCarWindow)

    def gotoScreen2(self):
        screen2 = Request()
        widget.addWidget(screen2)
        widget.setFixedHeight(500)
        widget.setFixedWidth(700)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # def loginScreen(self):
    #    screen5 = login()
    #    widget.addWidget(screen5)
    #    widget.setFixedHeight(500)
    #    widget.setFixedWidth(600)
    #    widget.setCurrentIndex(widget.currentIndex()+1)
    # def openWindow(self):
    #    self.window = QtWidgets.QDialog()
    #    self.ui = Ui_Dialog()
    #    self.ui.setupUi(self.window)
    #    self.window.show()

    def dataWindow(self):
        screen3 = Data()
        widget.addWidget(screen3)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1400)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def NewCarWindow(self):
        screen4 = New()
        widget.addWidget(screen4)
        widget.setFixedHeight(500)
        widget.setFixedWidth(1000)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(900)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except sys.error as e:
    print(e, "EXiting")
