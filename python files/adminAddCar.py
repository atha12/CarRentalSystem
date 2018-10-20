# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminAddCar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

import requests


class adminAddCar(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 20, 101, 20))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 80, 90, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 80, 581, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.carType = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.carType.setObjectName("carType")
        self.verticalLayout_2.addWidget(self.carType)
        self.carModel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.carModel.setObjectName("carModel")
        self.verticalLayout_2.addWidget(self.carModel)
        self.rent = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.rent.setObjectName("rent")
        self.verticalLayout_2.addWidget(self.rent)
        self.fine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fine.setObjectName("fine")
        self.verticalLayout_2.addWidget(self.fine)
        self.carMileage = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.carMileage.setObjectName("carMileage")
        self.verticalLayout_2.addWidget(self.carMileage)
        self.available = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.available.setObjectName("available")
        self.verticalLayout_2.addWidget(self.available)

        self.text=a

        self.request = QtWidgets.QPushButton(self.centralwidget)
        self.request.setGeometry(QtCore.QRect(380, 470, 131, 27))
        self.request.setObjectName("request")
        self.request.clicked.connect(self.toRequest)

        self.addCar = QtWidgets.QPushButton(self.centralwidget)
        self.addCar.setGeometry(QtCore.QRect(220, 470, 99, 27))
        self.addCar.setObjectName("addCar")
        self.addCar.clicked.connect(self.toAddCar)


        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(570, 470, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.toHomeScreen)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 25))
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
        self.label.setText(_translate("MainWindow", "Admin Add Cars"))
        self.label_2.setText(_translate("MainWindow", "Car Type:"))
        self.label_3.setText(_translate("MainWindow", "Car Model:"))
        self.label_4.setText(_translate("MainWindow", "Rent:"))
        self.label_8.setText(_translate("MainWindow", "Fine:"))
        self.label_9.setText(_translate("MainWindow", "Car Mileage:"))
        self.label_6.setText(_translate("MainWindow", "Car Availabe:"))
        self.request.setText(_translate("MainWindow", "Pending Requests"))
        self.addCar.setText(_translate("MainWindow", "Add Car"))
        self.logout.setText(_translate("MainWindow", "Logout"))


    def toAddCar(self):
        ct = self.carType.text()
        cm = self.carModel.text()
        re = self.rent.text()
        fi = self.fine.text()
        cmil = self.carMileage.text()
        av = self.available.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        query = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(query, (self.text))
        result1 = cur.fetchone()

        id1=result1[0]

        query = "insert into `cars` (`type`,`model`,`rent`,`fine`,`mileage`,`car_available`,`admin_id`) values (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (ct,cm,re,fi,cmil,av,id1))
        conn.commit()
        conn.close()

        msg = QMessageBox()

        msg.about(self,'Successfully Added',"New Car Added.")

        # self.close()
        # self.screen = mainscreeenCode.mainScreen()
        # self.screen.show()
        # print(self.text)

    def toRequest(self):
        self.close()
        self.screen = requests.requests(self.text)
        self.screen.show()


    def toHomeScreen(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()




