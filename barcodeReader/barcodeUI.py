# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barcodeUI.ui'
#
# Created: Sun Aug 03 19:03:16 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_barcodeUI(object):
    def setupUi(self, barcodeUI):
        barcodeUI.setObjectName("barcodeUI")
        barcodeUI.resize(450, 185)
        self.centralwidget = QtWidgets.QWidget(barcodeUI)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 91))
        self.widget.setObjectName("widget")
        self.play = QtWidgets.QPushButton(self.widget)
        self.play.setGeometry(QtCore.QRect(310, 10, 121, 51))
        self.play.setObjectName("play")
        self.barcode = QtWidgets.QLineEdit(self.widget)
        self.barcode.setGeometry(QtCore.QRect(10, 10, 291, 51))
        self.barcode.setObjectName("barcode")
        barcodeUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(barcodeUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 47))
        self.menubar.setObjectName("menubar")
        barcodeUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(barcodeUI)
        self.statusbar.setObjectName("statusbar")
        barcodeUI.setStatusBar(self.statusbar)

        self.retranslateUi(barcodeUI)
        QtCore.QMetaObject.connectSlotsByName(barcodeUI)

    def retranslateUi(self, barcodeUI):
        _translate = QtCore.QCoreApplication.translate
        barcodeUI.setWindowTitle(_translate("barcodeUI", "Barcode scanner"))
        self.play.setText(_translate("barcodeUI", "Play"))

