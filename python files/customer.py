# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

class customer(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.driverList = QtWidgets.QListWidget(self.centralwidget)
        self.driverList.setGeometry(QtCore.QRect(530, 30, 281, 221))
        self.driverList.setObjectName("driverList")
        self.driverList.hide()
        self.driverList.itemActivated.connect(self.driverClick)

        self.carList = QtWidgets.QListWidget(self.centralwidget)
        self.carList.setGeometry(QtCore.QRect(50, 30, 281, 221))
        self.carList.setObjectName("carList")
        self.carList.itemActivated.connect(self.carClick)

        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()
        query = "SELECT `car_id`,`type`,`model`,`rent`,`fine`,`mileage` FROM `cars` WHERE `car_available`=%s"
        cur.execute(query, ('yes'))
        result = cur.fetchall()
        s=""
        for i in result:
            s="Car Id: " + str(i[0])+ "\n" + "Car Type: " + i[1] + "\n" + "Car Model: " + i[2] + "\n" + "Rent: " + str(i[3]) + "\n" + "Fine: " + str(i[4]) + "\n" + "Car Mileage: " + str(i[5]) + "\n"
            self.carList.addItem(s) 
        # print(result)

        query = "SELECT `id`,`fname`,`lname`,`email`,`contact`,`salary` FROM `users` WHERE `role`=%s and `salary` is not NULL"
        cur.execute(query,3)
        result = cur.fetchall()
        s=""
        for i in result:
            s="Driver Id: " + str(i[0])+ "\n" +"Name: " + i[1] + " " + i[2]+ "\n" + "Email: " + i[3] + "\n" + "Contact: " + str(i[4]) + "\n" + "Fee: " + str(i[5]) + "\n" 
            self.driverList.addItem(s) 


        conn.close()

        # self.carList.addItem(s)
        # self.carList.addItem(s)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 290, 501, 200))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked[QDate].connect(self.showDate)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 400, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 390, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 101, 17))
        self.label_3.setObjectName("label_3")
        self.deposit = QtWidgets.QLineEdit(self.centralwidget)
        self.deposit.setGeometry(QtCore.QRect(660, 400, 113, 27))
        self.deposit.setObjectName("deposit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 10, 121, 17))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()

        self.text=a

        self.dat = ""
        self.carVal=""
        self.driverVal=""



# def itemActivated_event(item)
#     print(item.text())

        self.driverBox = QtWidgets.QCheckBox(self.centralwidget)
        self.driverBox.setGeometry(QtCore.QRect(370, 140, 141, 22))
        self.driverBox.setObjectName("driverBox")
        self.driverBox.stateChanged.connect(self.state_changed)

        self.bookCar = QtWidgets.QPushButton(self.centralwidget)
        self.bookCar.setGeometry(QtCore.QRect(240, 530, 99, 27))
        self.bookCar.setObjectName("bookCar")
        self.bookCar.clicked.connect(self.toPending)


        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(410, 530, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.logOut)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Deposit:"))
        self.label_2.setText(_translate("MainWindow", "Book Date:"))
        self.label_3.setText(_translate("MainWindow", "Available Cars"))
        self.label_4.setText(_translate("MainWindow", "Available Drivers"))
        self.driverBox.setText(_translate("MainWindow", "Driver Required"))
        self.bookCar.setText(_translate("MainWindow", "Book Car"))
        self.logout.setText(_translate("MainWindow", "Logout"))

    def state_changed(self):
        if self.driverBox.isChecked():
            self.driverList.show()
            self.label_4.show()
        else:
            self.driverList.hide()
            self.label_4.hide()


    def showDate(self,date):
        self.dat = date.toString("yyyy-MM-dd")

    def driverClick(self,item):
        self.driverVal = item.text()
        print(self.driverVal)

    def carClick(self,item):
        self.carVal = item.text()



    def toPending(self):
        dep = self.deposit.text()
        if self.driverVal != "":
            dId = int((self.driverVal)[11])
            dr = "Yes"
        else:
            dId = -1
            dr= "No"
        cId = int((self.carVal)[8])
        da = self.dat
        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        query = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(query, (self.text))
        result1 = cur.fetchone()

        custId = result1[0]

        query = "SELECT `rent` FROM `cars` WHERE `car_id`=%s"
        cur.execute(query, (cId))
        result1 = cur.fetchone()
        ren = result1[0]

        if dr=="Yes":
            query = "SELECT `salary` FROM `users` WHERE `id`=%s"
            cur.execute(query, (dId))
            result1 = cur.fetchone()
            fe = result1[0]

            query = "UPDATE `users` SET `salary` = NULL WHERE `id`=%s"
            cur.execute(query, (dId))

        else:
            fe=0

        price = ren
        # +fe

        query = "UPDATE `cars` SET `car_available`=%s WHERE `car_id`=%s"
        cur.execute(query, ("No",cId))
    



        query = "insert into `books` (`book_date`,`approve`,`price`,`deposit`,`driver_req`,`cu_id`,`c_id`,`driver_id`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (da,"pending",price,dep,dr,custId,cId,dId))
        conn.commit()
        conn.close()

        msg = QMessageBox()

        msg.about(self,'Car Requested',"Status of your booking is pending.")
        # self.close()
        # self.screen = mainscreeenCode.mainScreen()
        # self.screen.show()

    def logOut(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()




