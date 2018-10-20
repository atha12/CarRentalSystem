# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bill.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

class bill(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 90, 81, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 230, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 270, 81, 17))
        self.label_4.setObjectName("label_4")

        self.text=a

        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(300, 190, 113, 27))
        self.price.setObjectName("price")

        self.fine = QtWidgets.QLineEdit(self.centralwidget)
        self.fine.setGeometry(QtCore.QRect(300, 230, 113, 27))
        self.fine.setObjectName("fine")

        self.days = QtWidgets.QLineEdit(self.centralwidget)
        self.days.setGeometry(QtCore.QRect(300, 270, 113, 27))
        self.days.setObjectName("days")


        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        query = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(query, (self.text))
        result2 = cur.fetchone()



        query = "SELECT `book_id`,`c_id`,`return_date`,`book_date`,`price`,`deposit`,`extends` FROM `books` WHERE `cu_id`=%s"
        cur.execute(query, (result2[0]))
        result = cur.fetchone()

        # query = "CREATE FUNCTION dates(ret date,ori date) RETURNS VARCHAR(10) DETERMINISTIC RETURN DATEDIFF(ret,ori);"

        # cur.execute(query)











        query ="SELECT dates(%s,%s)"
        cur.execute(query, (result[2],result[3]))
        result1 = cur.fetchone()

        query = "SELECT `fine` FROM `cars` WHERE `car_id`=%s"
        cur.execute(query, (result[1]))
        result3 = cur.fetchone()

        fine=result3[0]



        day=result1[0]

        day=int(day)


        if result[6]=="Yes":
            self.fine.setText("-")
            self.days.setText(str(day))

            self.price.setText(str((result[4]*day)-result[5]))
        else:
            self.days.setText(str(day))
            if day>10:
                self.fine.setText(str(fine*(day-10)))
                self.price.setText(str(result[4]*10+(result[4]+fine)*(day-10)-result[5]))
                self.days.setText(str(day))
            else:
                self.fine.setText("-")
                self.days.setText(str(day))

                self.price.setText(str((result[4]*day)-result[5]))





        # s=""
        # for i in result:

        #     query = "SELECT `fname`,`lname` FROM `users` WHERE `id`=%s"
        #     cur.execute(query, (i[3]))
        #     result0 = cur.fetchone()

        #     query = "SELECT `type`,`model` FROM `cars` WHERE `car_id`=%s"
        #     cur.execute(query, (i[1]))
        #     result1 = cur.fetchone()

        #     if i[2]!=-1:
        #         query = "SELECT `fname`,`lname` FROM `users` WHERE `id`=%s"
        #         cur.execute(query, (i[2]))
        #         result2 = cur.fetchone()
        #         s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Driver: " + result2[0] + " " + result2[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
        #         self.billList.addItem(s)
        #     else:
        #         s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
        #         self.billList.addItem(s)

        conn.close()









        self.pay = QtWidgets.QPushButton(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(280, 390, 99, 27))
        self.pay.setObjectName("pay")
        self.pay.clicked.connect(self.topay)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 25))
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
        self.label.setText(_translate("MainWindow", "TOTAL BILL"))
        self.label_2.setText(_translate("MainWindow", "Total Price:"))
        self.label_3.setText(_translate("MainWindow", "Fine :"))
        self.label_4.setText(_translate("MainWindow", "Days:"))
        self.pay.setText(_translate("MainWindow", "Pay"))

    def topay(self):
        msg = QMessageBox()

        msg.about(self,'Successfully Paid',"Thank you for paying. Have a good day.")

        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()




