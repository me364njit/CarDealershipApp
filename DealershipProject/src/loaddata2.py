# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loaddata2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1680, 639)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.verticalLayout_2.addWidget(self.lineEditDBName)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.verticalLayout_3.addWidget(self.lineEditTableName)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.ShowData = QtWidgets.QPushButton(Dialog)
        self.ShowData.setObjectName("ShowData")
        self.ShowData.clicked.connect(self.selectData)
        self.verticalLayout.addWidget(self.ShowData)
        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def selectData(self):
        try:
            dbname = self.lineEditDBName.text()
            tableName = self.lineEditTableName.text()

            mydb = mc.connect(host='localhost', user='root',
                              password='Alexandria0!', database=dbname)

            mycursor = mydb.cursor()
            mycursor.execute("Select * From {} ".format(tableName))
            # where make = 'bmw'
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,
                                             QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e, "Error occured")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter DB name:"))
        self.label_2.setText(_translate("Dialog", "Enter Table name:"))
        self.ShowData.setText(_translate("Dialog", "Show Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
