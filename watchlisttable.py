# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watchlisttable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WatchList(object):
    def setupUi(self, WatchList):
        WatchList.setObjectName("WatchList")
        WatchList.resize(900, 720)
        self.WatchTableWidget = QtWidgets.QTableWidget(WatchList)
        self.WatchTableWidget.setGeometry(QtCore.QRect(30, 90, 841, 541))
        self.WatchTableWidget.setObjectName("WatchTableWidget")
        self.WatchTableWidget.setColumnCount(0)
        self.WatchTableWidget.setRowCount(0)
        self.RefreshButton = QtWidgets.QPushButton(WatchList)
        self.RefreshButton.setGeometry(QtCore.QRect(290, 660, 320, 30))
        self.RefreshButton.setObjectName("RefreshButton")
        self.AddRemoveButton = QtWidgets.QPushButton(WatchList)
        self.AddRemoveButton.setGeometry(QtCore.QRect(770, 20, 101, 41))
        self.AddRemoveButton.setObjectName("AddRemoveButton")

        self.retranslateUi(WatchList)
        QtCore.QMetaObject.connectSlotsByName(WatchList)

    def retranslateUi(self, WatchList):
        _translate = QtCore.QCoreApplication.translate
        WatchList.setWindowTitle(_translate("WatchList", "Form"))
        self.RefreshButton.setText(_translate("WatchList", "Refresh"))
        self.AddRemoveButton.setText(_translate("WatchList", "Add / Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WatchList = QtWidgets.QWidget()
    ui = Ui_WatchList()
    ui.setupUi(WatchList)
    WatchList.show()
    sys.exit(app.exec_())

