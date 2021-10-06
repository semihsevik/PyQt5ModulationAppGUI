# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'am_graph.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
********************************************************
-----> AM Modülasyonu Qt Designer Tasarım Dosyası <-----
********************************************************
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.am_messageButton = QtWidgets.QPushButton(self.centralwidget)
        self.am_messageButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.am_messageButton.setObjectName("am_messageButton")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.am_messageButton.setFont(font)
        self.gridLayout.addWidget(self.am_messageButton, 0, 0, 1, 1)
        self.am_modButton = QtWidgets.QPushButton(self.centralwidget)
        self.am_modButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.am_modButton.setObjectName("am_modButton")
        self.am_modButton.setFont(font)
        self.gridLayout.addWidget(self.am_modButton, 0, 2, 1, 1)
        self.am_carrierButton = QtWidgets.QPushButton(self.centralwidget)
        self.am_carrierButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.am_carrierButton.setObjectName("am_carrierButton")
        self.am_carrierButton.setFont(font)
        self.gridLayout.addWidget(self.am_carrierButton, 0, 1, 1, 1)
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout.addWidget(self.MplWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genlik Modülasyonu"))
        self.am_messageButton.setText(_translate("MainWindow", "Mesaj Sinyalini Göster"))
        self.am_modButton.setText(_translate("MainWindow", "Genlik Modüleli Sinyali Göster"))
        self.am_carrierButton.setText(_translate("MainWindow", "Taşıyıcı Sinyali Göster"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

