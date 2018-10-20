# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driverSal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

class driverSal(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 240, 131, 21))
        self.label_2.setObjectName("label_2")
        self.salary = QtWidgets.QLineEdit(self.centralwidget)
        self.salary.setGeometry(QtCore.QRect(250, 240, 301, 27))
        self.salary.setObjectName("salary")

        self.updateSal = QtWidgets.QPushButton(self.centralwidget)
        self.updateSal.setGeometry(QtCore.QRect(210, 350, 101, 27))
        self.updateSal.setObjectName("updateSal")
        self.updateSal.clicked.connect(self.toAddSal)

        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(390, 350, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.toHomeScreen)

        self.text=a

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
        self.label.setText(_translate("MainWindow", "Driver Page"))
        self.label_2.setText(_translate("MainWindow", "Enter your salary:"))
        self.updateSal.setText(_translate("MainWindow", "Update Salary"))
        self.logout.setText(_translate("MainWindow", "Logout"))

    def toAddSal(self):
        sal = self.salary.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()
        query = "SELECT `id` FROM `users` WHERE `email`=%s"
        cur.execute(query, (self.text))
        result1 = cur.fetchone()

        id1=result1[0]

        query = "update `users` set `salary`=%s where `id`=%s"
        cur.execute(query, (sal,id1))
        conn.commit()
        conn.close()

        msg = QMessageBox()

        msg.about(self,'Successfully Updated',"Your Salary has been updated/added.") 

    def toHomeScreen(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()




