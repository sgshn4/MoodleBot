# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#v1
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 711, 581))
        self.tableView.setObjectName("tableView")
        self.calibration = QtWidgets.QPushButton(self.centralwidget)
        self.calibration.setGeometry(QtCore.QRect(720, 10, 75, 23))
        self.calibration.setObjectName("calibration")
        self.addSubject = QtWidgets.QPushButton(self.centralwidget)
        self.addSubject.setGeometry(QtCore.QRect(720, 40, 75, 23))
        self.addSubject.setObjectName("addSubject")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(720, 540, 75, 23))
        self.run.setObjectName("run")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MoodleBot"))
        self.calibration.setText(_translate("MainWindow", "Calibration"))
        self.addSubject.setText(_translate("MainWindow", "Add Subject"))
        self.run.setText(_translate("MainWindow", "Run"))


def show():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())