# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prebill.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

import bill

import extends

class prebill(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.billList = QtWidgets.QListWidget(self.centralwidget)
        self.billList.setGeometry(QtCore.QRect(70, 90, 281, 221))
        self.billList.setObjectName("billList")

        self.text=a

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 90, 361, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 110, 361, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 130, 361, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 150, 361, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 170, 361, 21))
        self.label_8.setObjectName("label_8")

        self.returnCalendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.returnCalendarWidget.setGeometry(QtCore.QRect(370, 300, 501, 200))
        self.returnCalendarWidget.setObjectName("returnCalendarWidget")
        self.returnCalendarWidget.clicked[QDate].connect(self.returnDate)
        self.returnCalendarWidget.hide()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 400, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()

        self.returnBox = QtWidgets.QCheckBox(self.centralwidget)
        self.returnBox.setGeometry(QtCore.QRect(520, 240, 141, 22))
        self.returnBox.setObjectName("returnBox")
        self.returnBox.stateChanged.connect(self.state_changed)

        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        query = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(query, (self.text))
        result2 = cur.fetchone()



        query = "SELECT `book_id`,`c_id`,`driver_id`,`cu_id`,`book_date`,`price`,`deposit` FROM `books` WHERE `cu_id`=%s"
        cur.execute(query, (result2[0]))
        result = cur.fetchall()
        s=""
        for i in result:

            query = "SELECT `fname`,`lname` FROM `users` WHERE `id`=%s"
            cur.execute(query, (i[3]))
            result0 = cur.fetchone()

            query = "SELECT `type`,`model` FROM `cars` WHERE `car_id`=%s"
            cur.execute(query, (i[1]))
            result1 = cur.fetchone()

            if i[2]!=-1:
                query = "SELECT `fname`,`lname` FROM `users` WHERE `id`=%s"
                cur.execute(query, (i[2]))
                result2 = cur.fetchone()
                s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Driver: " + result2[0] + " " + result2[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
                self.billList.addItem(s)
            else:
                s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
                self.billList.addItem(s)

        conn.close()







        self.extend = QtWidgets.QPushButton(self.centralwidget)
        self.extend.setGeometry(QtCore.QRect(190, 530, 99, 27))
        self.extend.setObjectName("extend")
        self.extend.clicked.connect(self.toExtend)

        self.bill = QtWidgets.QPushButton(self.centralwidget)
        self.bill.setGeometry(QtCore.QRect(350, 530, 99, 27))
        self.bill.setObjectName("bill")
        self.bill.clicked.connect(self.toBill)


        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(510, 530, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.logOut)



        

        self.dat = ""

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 25))
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
        self.label_3.setText(_translate("MainWindow", "Your Purchase"))
        self.label_4.setText(_translate("MainWindow", "A standard car rent is for 10 days after which if "))
        self.label_5.setText(_translate("MainWindow", "unreturned we start charging a fine."))
        self.label_6.setText(_translate("MainWindow", "If you want to continue then extend your plan."))
        self.label_7.setText(_translate("MainWindow", "Select a date more than 10 days ahead of your book"))
        self.label_8.setText(_translate("MainWindow", "date."))
        self.label_2.setText(_translate("MainWindow", "Return Date:"))
        self.returnBox.setText(_translate("MainWindow", "Return Car"))
        self.extend.setText(_translate("MainWindow", "Extend"))
        self.bill.setText(_translate("MainWindow", "Bill"))
        self.logout.setText(_translate("MainWindow", "Logout"))

    def state_changed(self):
        if self.returnBox.isChecked():
            self.returnCalendarWidget.show()
            self.label_2.show()
        else:
            self.returnCalendarWidget.hide()
            self.label_2.hide()

    def returnDate(self,date):
        self.dat = date.toString("yyyy-MM-dd")

    def toBill(self):
        da = self.dat

        if da!="":
            conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
            cur = conn.cursor()

            query = "SELECT `id` FROM `users` WHERE `email`=%s"
            cur.execute(query, (self.text))
            result1 = cur.fetchone()

            custId = result1[0]

            query = "SELECT `book_id` FROM `books` WHERE `cu_id`=%s"
            cur.execute(query, (custId))
            result = cur.fetchone()

            # if dr=="Yes":
            #     query = "SELECT `salary` FROM `users` WHERE `id`=%s"
            #     cur.execute(query, (dId))
            #     result1 = cur.fetchone()
            #     fe = result1[0]

            #     query = "UPDATE `users` SET `salary` = NULL WHERE `id`=%s"
            #     cur.execute(query, (dId))

            # else:
            #     fe=0

            # price = ren+fe

            query = "UPDATE `books` SET `return_date`=%s WHERE `book_id`=%s"
            cur.execute(query, (da,result[0]))
        



            # query = "insert into `books` (`book_date`,`approve`,`price`,`deposit`,`driver_req`,`cu_id`,`c_id`,`driver_id`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            # cur.execute(query, (da,"pending",price,dep,dr,custId,cId,dId))
            conn.commit()
            conn.close()

        msg = QMessageBox()

        msg.about(self,'Return Date Set',"You have successfully set the retur date of the car.")

        self.close()
        self.screen = bill.bill(self.text)
        self.screen.show()


    def toExtend(self):
        self.close()
        self.screen = extends.extends(self.text)
        self.screen.show()

        # conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        # cur = conn.cursor()

        # query = "SELECT `id` FROM `users` WHERE `email`=%s"
        # cur.execute(query, (self.text))
        # result1 = cur.fetchone()

        # custId = result1[0]

        # query = "SELECT `book_date`,`return_date` FROM `books` WHERE `cu_id`=%s"
        # cur.execute(query, (custId))
        # result = cur.fetchone()

        # query = "SELECT DATEDIFF(%s,%s)"
        # cur.execute(query, (result[1],result[0]))
        # result = cur.fetchone()

        # print(result)

        # conn.close()




    def logOut(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()




