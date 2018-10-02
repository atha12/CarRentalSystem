from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMainWindow
import sys
import mainscreeenCode

if __name__ == '__main__':
	app = QApplication(sys.argv)
	screen = mainscreeenCode.mainScreen()
	screen.show()
	sys.exit(app.exec_())