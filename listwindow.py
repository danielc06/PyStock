# This file contains the code for the gui layout



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainList = QtWidgets.QListWidget(self.centralwidget)
        self.MainList.setGeometry(QtCore.QRect(40, 20, 251, 381))
        self.MainList.setObjectName("HomeWindow")
        self.UserList = QtWidgets.QListWidget(self.centralwidget)
        self.UserList.setGeometry(QtCore.QRect(510, 20, 251, 381))
        self.UserList.setObjectName("UserList")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(340, 160, 121, 23))
        self.AddButton.setObjectName("AddButton")
        self.RemoveButton = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveButton.setGeometry(QtCore.QRect(340, 200, 121, 23))
        self.RemoveButton.setObjectName("RemoveButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(310, 480, 181, 23))
        self.SaveButton.setObjectName("SaveButton")
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "HomeWindow"))
        self.AddButton.setText(_translate("HomeWindow", ">     Add     >"))
        self.RemoveButton.setText(_translate("HomeWindow", "<  Remove  <"))
        self.SaveButton.setText(_translate("HomeWindow", "Save and Exit"))


# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

