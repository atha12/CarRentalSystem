# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pymysql

import mainscreeenCode


from PyQt5.QtWidgets import QMainWindow


class signUpScreen(QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 100, 81, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 100, 581, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fname.setObjectName("fname")
        self.verticalLayout_2.addWidget(self.fname)
        self.lname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lname.setObjectName("lname")
        self.verticalLayout_2.addWidget(self.lname)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.contact = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.contact.setObjectName("contact")
        self.verticalLayout_2.addWidget(self.contact)
        self.address = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.address.setObjectName("address")
        self.verticalLayout_2.addWidget(self.address)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 20, 91, 20))
        self.label_4.setObjectName("label_4")
        
        self.rolebox = QtWidgets.QComboBox(self.centralwidget)
        self.rolebox.setGeometry(QtCore.QRect(320, 440, 101, 27))
        self.rolebox.setObjectName("rolebox")
        self.rolebox.addItem("Customer")
        self.rolebox.addItem("Driver")
        self.rolebox.activated[str].connect(self.combo_text)
        self.text=""

        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(220, 510, 99, 27))
        self.done.setObjectName("done")
        self.done.clicked.connect(self.toHomeScreenInsert)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 440, 111, 20))
        self.label_5.setObjectName("label_5")

        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(360, 510, 99, 27))
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.cancelled)

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
        self.label.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_3.setText(_translate("MainWindow", "Email:"))
        self.label_8.setText(_translate("MainWindow", "Contact:"))
        self.label_9.setText(_translate("MainWindow", "Address:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Sign Up Form"))
        self.rolebox.setItemText(0, _translate("MainWindow", "Customer"))
        self.rolebox.setItemText(1, _translate("MainWindow", "Driver"))
        self.done.setText(_translate("MainWindow", "Done"))
        self.label_5.setText(_translate("MainWindow", "Select Usecase:"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))

    def combo_text(self,text):
        self.text = self.rolebox.currentText()

    def toHomeScreenInsert(self):
        fn = self.fname.text()
        ln = self.lname.text()
        em = self.email.text()
        con = self.contact.text()
        ad = self.address.text()
        pas = self.password.text()
        if self.text=="Customer":
            rol = 1
        else:
            rol = 3
        conn = pymysql.connect(host="localhost",user="root",password="Athu1998",db="carRental")
        cur = conn.cursor()
        query = "insert into `users` (`fname`,`lname`,`email`,`contact`,`address`,`password`,`role`) values (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (fn,ln,em,con,ad,pas,rol))
        conn.commit()
        conn.close()
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()

    def cancelled(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()



