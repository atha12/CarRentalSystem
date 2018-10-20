# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extends.ui'
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

class extends(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 60, 51, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 310, 81, 17))
        self.label_2.setObjectName("label_2")

        self.extend = QtWidgets.QPushButton(self.centralwidget)
        self.extend.setGeometry(QtCore.QRect(300, 400, 99, 27))
        self.extend.setObjectName("extend")
        self.extend.clicked.connect(self.toExtend)


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 81, 17))
        self.label_3.setObjectName("label_3")

        self.text=a

        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(470, 400, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.logOut)

        self.extendCalender = QtWidgets.QCalendarWidget(self.centralwidget)
        self.extendCalender.setGeometry(QtCore.QRect(140, 160, 501, 200))
        self.extendCalender.setObjectName("extendCalender")
        self.extendCalender.clicked[QDate].connect(self.toDate)


        self.dat = ""





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
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
        self.label.setText(_translate("MainWindow", "Extend"))
        self.label_2.setText(_translate("MainWindow", "Book Date:"))
        self.extend.setText(_translate("MainWindow", "Extend"))
        self.label_3.setText(_translate("MainWindow", "Book Date:"))
        self.logout.setText(_translate("MainWindow", "Logout"))

    def toDate(self,date):
        self.dat = date.toString("yyyy-MM-dd")

    def toExtend(self):
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

            query = "UPDATE `books` SET `return_date`=%s,`extends`=%s,`extend_appr`=%s WHERE `book_id`=%s"
            cur.execute(query, (da,"Yes","pending",result[0]))
        



            # query = "insert into `books` (`book_date`,`approve`,`price`,`deposit`,`driver_req`,`cu_id`,`c_id`,`driver_id`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            # cur.execute(query, (da,"pending",price,dep,dr,custId,cId,dId))
            conn.commit()
            conn.close()

        msg = QMessageBox()

        msg.about(self,'Date Extended',"You have successfully extended the retur date of the car.")

        # self.close()
        # self.screen = bill.bill(self.text)
        # self.screen.show()

    def logOut(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()

