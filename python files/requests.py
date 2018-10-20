# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requests.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QMainWindow,QMessageBox

import pymysql

import mainscreeenCode

class requests(QMainWindow):
    def __init__(self,a):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self,a)
    def setupUi(self, MainWindow,a):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 131, 17))
        self.label.setObjectName("label")

        self.request = QtWidgets.QListWidget(self.centralwidget)
        self.request.setGeometry(QtCore.QRect(70, 110, 281, 221))
        self.request.setObjectName("request")
        self.request.itemActivated.connect(self.requestClick)


        self.acceptRequests = QtWidgets.QPushButton(self.centralwidget)
        self.acceptRequests.setGeometry(QtCore.QRect(208, 440, 121, 27))
        self.acceptRequests.setObjectName("acceptRequests")
        self.acceptRequests.clicked.connect(self.toAccept)

        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(500, 440, 99, 27))
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(self.logOut)

        self.extendRequest = QtWidgets.QListWidget(self.centralwidget)
        self.extendRequest.setGeometry(QtCore.QRect(430, 110, 281, 221))
        self.extendRequest.setObjectName("extendRequest")
        self.extendRequest.itemActivated.connect(self.extendClick)



        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        # query="CREATE view f_view as SELECT `book_id`,`c_id`,`driver_id`,`cu_id`,`book_date`,`price`,`deposit` FROM `books` WHERE `approve`=%s"
        # cur.execute(query, ('pending'))
        # result = cur.fetchall()

        query="select * from f_view;"
        cur.execute(query)
        result = cur.fetchall()


        # query = "SELECT `book_id`,`c_id`,`driver_id`,`cu_id`,`book_date`,`price`,`deposit` FROM `books` WHERE `approve`=%s"
        # cur.execute(query, ('pending'))
        # result = cur.fetchall()
        print(result)
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
                self.request.addItem(s)
            else:
                s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
                self.request.addItem(s) 
        # print(result)

        query = "SELECT `book_id`,`c_id`,`driver_id`,`cu_id`,`book_date`,`price`,`deposit` FROM `books` WHERE `approve`=%s and `extend_appr`=%s"
        cur.execute(query, ('Yes','pending'))
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
                self.extendRequest.addItem(s)
            else:
                s="Book Id: " + str(i[0])+ "\n" + "Car Type: " + result1[0] + "\n" + "Car Model: " + result1[1] + "\n" + "Customer: " + result0[0] + " " + result0[1] + "\n" + "Book Date: " + str(i[4]) + "\n" + "Price: " + str(i[5]) + "\n" + "Deposit: " + str(i[6]) + "\n" 
                self.extendRequest.addItem(s)

        # query = "SELECT `id`,`fname`,`lname`,`email`,`contact`,`salary` FROM `users` WHERE `role`=%s and `salary` is not NULL"
        # cur.execute(query,3)
        # result = cur.fetchall()
        # s=""
        # for i in result:
        #     s="Driver Id: " + str(i[0])+ "\n" +"Name: " + i[1] + " " + i[2]+ "\n" + "Email: " + i[3] + "\n" + "Contact: " + str(i[4]) + "\n" + "Fee: " + str(i[5]) + "\n" 
        #     self.driverList.addItem(s) 


        conn.close()
        




        self.text=a

        # self.dat = ""
        self.acceptVal=[]
        self.extendVal=[]

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 111, 20))
        self.label_2.setObjectName("label_2")
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
        self.label.setText(_translate("MainWindow", "Pending Requests"))
        self.acceptRequests.setText(_translate("MainWindow", "Accept Requests"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.label_2.setText(_translate("MainWindow", "Extend Request"))

    def requestClick(self,item):
        self.acceptVal.append(int(item.text()[9]))
        print(self.acceptVal)

    def extendClick(self,item):
        self.extendVal.append(int(item.text()[9]))
        print(self.extendVal)


    def toAccept(self):
        conn = pymysql.connect(host="localhost",user="root",password="",db="carRental")
        cur = conn.cursor()

        for i in self.acceptVal:

            # query = "SELECT `book_date` FROM `books` WHERE `book_id`=%s"
            # cur.execute(query, i)
            # result1 = cur.fetchone()
            # ren = result1[1]

            # print(ren)

            query = "UPDATE `books` SET `approve`=%s WHERE `book_id`=%s"
            cur.execute(query, ("Yes",i))

            # query = "SELECT `DATEADD(day,2,ren)` FROM `books` WHERE `book_id`=%s"
            # cur.execute(query, (i))
            # result1 = cur.fetchone()
            # ren = result1[0]

            # print(ren)

            # query = "UPDATE `books` SET `return_date`=%s WHERE `book_id`=%s"
            # cur.execute(query, (DATEADD(day,2,ren),i))



        for i in self.extendVal:
            query = "UPDATE `books` SET `extend_appr`=%s WHERE `book_id`=%s"
            cur.execute(query, ("Yes",i))

        # custId = result1[0]

        # query = "SELECT `rent` FROM `cars` WHERE `car_id`=%s"
        # cur.execute(query, (cId))
        # result1 = cur.fetchone()
        # ren = result1[0]

        # if dr=="Yes":
        #     query = "SELECT `salary` FROM `users` WHERE `id`=%s"
        #     cur.execute(query, (dId))
        #     result1 = cur.fetchone()
        #     fe = result1[0]

            

        # else:
        #     fe=0

        # price = ren+fe

        # query = "UPDATE `cars` SET `car_available`=%s WHERE `car_id`=%s"
        # cur.execute(query, ("No",cId))
    



        # query = "insert into `books` (`book_date`,`approve`,`price`,`deposit`,`driver_req`,`cu_id`,`c_id`,`driver_id`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        # cur.execute(query, (da,"pending",price,dep,dr,custId,cId,dId))
        conn.commit()
        conn.close()

        msg = QMessageBox()

        msg.about(self,'Requests Approved',"Cars have been approved for rent.")

    def logOut(self):
        self.close()
        self.screen = mainscreeenCode.mainScreen()
        self.screen.show()


        

    


