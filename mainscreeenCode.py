# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speech.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMainWindow

import loginScreen

import signUpScreen

class mainScreen(QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
	def setupUi(self, MainWindow):
	    MainWindow.setObjectName("MainWindow")
	    MainWindow.resize(569, 468)
	    self.centralwidget = QtWidgets.QWidget(MainWindow)
	    self.centralwidget.setObjectName("centralwidget")
	    self.label = QtWidgets.QLabel(self.centralwidget)
	    self.label.setGeometry(QtCore.QRect(210, 40, 121, 17))
	    self.label.setWordWrap(True)
	    self.label.setObjectName("label")
	    self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
	    self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 160, 160, 221))
	    self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
	    self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
	    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
	    self.verticalLayout.setObjectName("verticalLayout")
	    
	    self.signButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
	    self.signButton.setObjectName("signButton")
	    self.signButton.clicked.connect(self.toSignUpScreen)
	    # self.setDefault(True)
	    # self.setAutoDefault(True)
	    self.verticalLayout.addWidget(self.signButton)
	    self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
	    
	    self.loginButton.setObjectName("loginButton")
	    self.loginButton.clicked.connect(self.toLoginScreen)
	    # self.setDefault(True)
	    # self.setAutoDefault(True)
	    self.verticalLayout.addWidget(self.loginButton)
	    
	    MainWindow.setCentralWidget(self.centralwidget)
	    self.menubar = QtWidgets.QMenuBar(MainWindow)
	    self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 25))
	    self.menubar.setObjectName("menubar")
	    MainWindow.setMenuBar(self.menubar)
	    self.statusbar = QtWidgets.QStatusBar(MainWindow)
	    self.statusbar.setObjectName("statusbar")
	    MainWindow.setStatusBar(self.statusbar)

	    self.retranslateUi(MainWindow)
	    QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
	    _translate = QtCore.QCoreApplication.translate
	    MainWindow.setWindowTitle(_translate("MainWindow", "Home Screen"))
	    self.label.setText(_translate("MainWindow", "LOGIN or SIGNUP"))
	    self.signButton.setText(_translate("MainWindow", "SignUp"))
	    self.loginButton.setText(_translate("MainWindow", "Login"))

	def toLoginScreen(self):
		self.close()
		self.screen = loginScreen.loginScreen()
		self.screen.show()
	def toSignUpScreen(self):
		self.close()
		self.screen = signUpScreen.signUpScreen()
		self.screen.show()

