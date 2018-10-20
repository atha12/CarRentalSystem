# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import adminAddCar

import driverSal

import customer

import pending

import prebill


class loginScreen(QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 508)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 441, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.email = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.email.setObjectName("email")
        self.horizontalLayout.addWidget(self.email)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 190, 441, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.password)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 320, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logInButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logInButton.setObjectName("logInButton")
        self.logInButton.clicked.connect(self.toLogin)
        self.verticalLayout.addWidget(self.logInButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        

        # self.role.activated[str].connect()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginScreen"))
        self.label.setText(_translate("MainWindow", "Email:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.logInButton.setText(_translate("MainWindow", "Login"))

    def toLogin(self):
        em = self.email.text()
        pas = self.password.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()
        query = "SELECT `role` FROM `users` WHERE `email`=%s and `password`=%s"
        cur.execute(query, (em,pas))
        result = cur.fetchone()
        if result is None:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # msg.setText("Record doesn't exist in database")
            # msg.setInformativeText("This is additional information")
            # msg.setWindowTitle("Not Found")
            # msg.setDetailedText("The details are as follows:")
            msg.about(self,'Not Found',"Record doesn't exist in database, please sign-up")
        else:
            log= result[0]
            conn.close()
            if log==2:
                self.close()
                self.screen = adminAddCar.adminAddCar(em)
                self.screen.show()
            elif log==3:
                self.close()
                self.screen = driverSal.driverSal(em)
                self.screen.show()
            else:
                conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
                cur = conn.cursor()

                query = "SELECT `id` FROM `users` WHERE `email`=%s"
                cur.execute(query, (em))
                result = cur.fetchone()


                query = "SELECT `approve` FROM `books` WHERE `cu_id`=%s"
                cur.execute(query, result[0])
                result1 = cur.fetchone()
                conn.close()

                if result1[0]=="pending":
                    self.close()
                    self.screen = pending.pending()
                    self.screen.show()
                elif result1[0]=="Yes":
                    self.close()
                    self.screen = prebill.prebill(em)
                    self.screen.show()
                else:
                    self.close()
                    self.screen = customer.customer(em)
                    self.screen.show()

                

        
    
        