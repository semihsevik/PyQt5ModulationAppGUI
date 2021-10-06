# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
*****************************************************
-----> Ana Pencere Qt Designer Tasarım Dosyası <-----
*****************************************************
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 519))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Modulation.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(17, 17))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_am = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_am.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_am.setFont(font)
        self.groupBox_am.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(18, 30, 200);\n"
"")
        self.groupBox_am.setObjectName("groupBox_am")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_am)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.am_selectText = QtWidgets.QLabel(self.groupBox_am)
        self.am_selectText.setObjectName("am_selectText")
        self.horizontalLayout.addWidget(self.am_selectText)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.am_squareWave = QtWidgets.QRadioButton(self.groupBox_am)
        self.am_squareWave.setObjectName("am_squareWave")
        self.horizontalLayout_2.addWidget(self.am_squareWave)
        self.am_sinWave = QtWidgets.QRadioButton(self.groupBox_am)
        self.am_sinWave.setObjectName("am_sinWave")
        self.horizontalLayout_2.addWidget(self.am_sinWave)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(194, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.am_modulationIndex_text = QtWidgets.QLabel(self.groupBox_am)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.am_modulationIndex_text.setFont(font)
        self.am_modulationIndex_text.setStyleSheet("color: rgb(18, 30, 200);")
        self.am_modulationIndex_text.setObjectName("am_modulationIndex_text")
        self.verticalLayout.addWidget(self.am_modulationIndex_text)
        self.am_modulationIndex = QtWidgets.QDoubleSpinBox(self.groupBox_am)
        self.am_modulationIndex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.am_modulationIndex.setMaximum(4.0)
        self.am_modulationIndex.setSingleStep(0.25)
        self.am_modulationIndex.setProperty("value", 1.0)
        self.am_modulationIndex.setObjectName("am_modulationIndex")
        self.verticalLayout.addWidget(self.am_modulationIndex)
        self.am_messagFrequency_text = QtWidgets.QLabel(self.groupBox_am)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.am_messagFrequency_text.setFont(font)
        self.am_messagFrequency_text.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(18, 30, 200);\n"
"")
        self.am_messagFrequency_text.setObjectName("am_messagFrequency_text")
        self.verticalLayout.addWidget(self.am_messagFrequency_text)
        self.am_messageSlider = QtWidgets.QSlider(self.groupBox_am)
        self.am_messageSlider.setStyleSheet("")
        self.am_messageSlider.setMaximum(2000)
        self.am_messageSlider.setProperty("value", 10)
        self.am_messageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.am_messageSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.am_messageSlider.setTickInterval(20)
        self.am_messageSlider.setObjectName("am_messageSlider")
        self.verticalLayout.addWidget(self.am_messageSlider)
        self.am_messageFrequency = QtWidgets.QSpinBox(self.groupBox_am)
        self.am_messageFrequency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.am_messageFrequency.setMinimum(1)
        self.am_messageFrequency.setMaximum(3000)
        self.am_messageFrequency.setSingleStep(100)
        self.am_messageFrequency.setProperty("value", 10)
        self.am_messageFrequency.setObjectName("am_messageFrequency")
        self.verticalLayout.addWidget(self.am_messageFrequency)
        self.am_carrierFrequency_text = QtWidgets.QLabel(self.groupBox_am)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.am_carrierFrequency_text.setFont(font)
        self.am_carrierFrequency_text.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(18, 30, 200);\n"
"")
        self.am_carrierFrequency_text.setObjectName("am_carrierFrequency_text")
        self.verticalLayout.addWidget(self.am_carrierFrequency_text)
        self.am_carrierSlider = QtWidgets.QSlider(self.groupBox_am)
        self.am_carrierSlider.setStyleSheet("")
        self.am_carrierSlider.setMaximum(10000)
        self.am_carrierSlider.setProperty("value", 100)
        self.am_carrierSlider.setOrientation(QtCore.Qt.Horizontal)
        self.am_carrierSlider.setInvertedAppearance(False)
        self.am_carrierSlider.setInvertedControls(False)
        self.am_carrierSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.am_carrierSlider.setTickInterval(100)
        self.am_carrierSlider.setObjectName("am_carrierSlider")
        self.verticalLayout.addWidget(self.am_carrierSlider)
        self.am_carrierFrequency = QtWidgets.QSpinBox(self.groupBox_am)
        self.am_carrierFrequency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.am_carrierFrequency.setMinimum(1)
        self.am_carrierFrequency.setMaximum(20000)
        self.am_carrierFrequency.setSingleStep(1000)
        self.am_carrierFrequency.setProperty("value", 100)
        self.am_carrierFrequency.setObjectName("am_carrierFrequency")
        self.verticalLayout.addWidget(self.am_carrierFrequency)
        self.am_plotButton = QtWidgets.QPushButton(self.groupBox_am)
        self.am_plotButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/pencil_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.am_plotButton.setIcon(icon1)
        self.am_plotButton.setObjectName("am_plotButton")
        self.verticalLayout.addWidget(self.am_plotButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_5.addWidget(self.groupBox_am)
        self.groupBox_fm = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_fm.setFont(font)
        self.groupBox_fm.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(18, 30, 200);\n"
"")
        self.groupBox_fm.setObjectName("groupBox_fm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_fm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.fm_selectText = QtWidgets.QLabel(self.groupBox_fm)
        self.fm_selectText.setObjectName("fm_selectText")
        self.horizontalLayout_3.addWidget(self.fm_selectText)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.fm_squareWave = QtWidgets.QRadioButton(self.groupBox_fm)
        self.fm_squareWave.setObjectName("fm_squareWave")
        self.horizontalLayout_4.addWidget(self.fm_squareWave)
        self.fm_sinWave = QtWidgets.QRadioButton(self.groupBox_fm)
        self.fm_sinWave.setObjectName("fm_sinWave")
        self.horizontalLayout_4.addWidget(self.fm_sinWave)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.fm_modulationIndex_text = QtWidgets.QLabel(self.groupBox_fm)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fm_modulationIndex_text.setFont(font)
        self.fm_modulationIndex_text.setStyleSheet("color: rgb(18, 30, 200);\n"
"")
        self.fm_modulationIndex_text.setObjectName("fm_modulationIndex_text")
        self.verticalLayout_2.addWidget(self.fm_modulationIndex_text)
        self.fm_modulationIndex = QtWidgets.QDoubleSpinBox(self.groupBox_fm)
        self.fm_modulationIndex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fm_modulationIndex.setMaximum(4.0)
        self.fm_modulationIndex.setSingleStep(0.25)
        self.fm_modulationIndex.setProperty("value", 2.0)
        self.fm_modulationIndex.setObjectName("fm_modulationIndex")
        self.verticalLayout_2.addWidget(self.fm_modulationIndex)
        self.fm_messageFrequency_text = QtWidgets.QLabel(self.groupBox_fm)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fm_messageFrequency_text.setFont(font)
        self.fm_messageFrequency_text.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"  
"color: rgb(18, 30, 200);")
        self.fm_messageFrequency_text.setObjectName("fm_messageFrequency_text")
        self.verticalLayout_2.addWidget(self.fm_messageFrequency_text)
        self.fm_messageSlider = QtWidgets.QSlider(self.groupBox_fm)
        self.fm_messageSlider.setMinimum(1)
        self.fm_messageSlider.setMaximum(2000)
        self.fm_messageSlider.setProperty("value", 5)
        self.fm_messageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fm_messageSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.fm_messageSlider.setTickInterval(20)
        self.fm_messageSlider.setObjectName("fm_messageSlider")
        self.verticalLayout_2.addWidget(self.fm_messageSlider)
        self.fm_messageFrequency = QtWidgets.QSpinBox(self.groupBox_fm)
        self.fm_messageFrequency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fm_messageFrequency.setMinimum(1)
        self.fm_messageFrequency.setMaximum(3000)
        self.fm_messageFrequency.setSingleStep(100)
        self.fm_messageFrequency.setProperty("value", 5)
        self.fm_messageFrequency.setObjectName("fm_messageFrequency")
        self.verticalLayout_2.addWidget(self.fm_messageFrequency)
        self.fm_carrierFrequency_text = QtWidgets.QLabel(self.groupBox_fm)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fm_carrierFrequency_text.setFont(font)
        self.fm_carrierFrequency_text.setStyleSheet("color: rgb(18, 30, 200);")
        self.fm_carrierFrequency_text.setObjectName("fm_carrierFrequency_text")
        self.verticalLayout_2.addWidget(self.fm_carrierFrequency_text)
        self.fm_carrierSlider = QtWidgets.QSlider(self.groupBox_fm)
        self.fm_carrierSlider.setMaximum(10000)
        self.fm_carrierSlider.setProperty("value", 30)
        self.fm_carrierSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fm_carrierSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.fm_carrierSlider.setTickInterval(100)
        self.fm_carrierSlider.setObjectName("fm_carrierSlider")
        self.verticalLayout_2.addWidget(self.fm_carrierSlider)
        self.fm_carrierFrequency = QtWidgets.QSpinBox(self.groupBox_fm)
        self.fm_carrierFrequency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fm_carrierFrequency.setMinimum(1)
        self.fm_carrierFrequency.setMaximum(20000)
        self.fm_carrierFrequency.setSingleStep(1000)
        self.fm_carrierFrequency.setProperty("value", 30)
        self.fm_carrierFrequency.setObjectName("fm_carrierFrequency")
        self.verticalLayout_2.addWidget(self.fm_carrierFrequency)
        self.fm_plotButton = QtWidgets.QPushButton(self.groupBox_fm)
        self.fm_plotButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.fm_plotButton.setIcon(icon1)
        self.fm_plotButton.setObjectName("fm_plotButton")
        self.verticalLayout_2.addWidget(self.fm_plotButton)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.horizontalLayout_5.addWidget(self.groupBox_fm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/red_repicthousebase_1484336386-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/icons/koü.jpg"))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(18, 30, 200);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(18, 30, 200);")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(18, 30, 200);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/books-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon3)
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_5.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab_4)
        self.commandLinkButton_2.setIcon(icon3)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout_5.addWidget(self.commandLinkButton_2)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.tab_4)
        self.commandLinkButton_3.setIcon(icon3)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout_5.addWidget(self.commandLinkButton_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/info-31211_960_720.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modülasyon Uygulaması "))
        self.groupBox_am.setTitle(_translate("MainWindow", "GENLİK MODÜLASYONU"))
        self.am_selectText.setText(_translate("MainWindow", "Mesaj Sinyalinin Tipini Seçin"))
        self.am_squareWave.setText(_translate("MainWindow", "Kare"))
        self.am_sinWave.setText(_translate("MainWindow", "Sinüsoidal "))
        self.am_modulationIndex_text.setText(_translate("MainWindow", "Modülasyon İndeksi:"))
        self.am_messagFrequency_text.setText(_translate("MainWindow", "Mesaj Frekansı:"))
        self.am_carrierFrequency_text.setText(_translate("MainWindow", "Taşıyıcı Frekansı:"))
        self.am_plotButton.setText(_translate("MainWindow", "GRAFİK"))
        self.groupBox_fm.setTitle(_translate("MainWindow", "FREKANS MODÜLASYONU"))
        self.fm_selectText.setText(_translate("MainWindow", "Mesaj Sinyalinin Tipini Seçin"))
        self.fm_squareWave.setText(_translate("MainWindow", "Kare"))
        self.fm_sinWave.setText(_translate("MainWindow", "Sinüsoidal "))
        self.fm_modulationIndex_text.setText(_translate("MainWindow", "Modülasyon İndeksi:"))
        self.fm_messageFrequency_text.setText(_translate("MainWindow", "Mesaj Frekansı:"))
        self.fm_carrierFrequency_text.setText(_translate("MainWindow", "Taşıyıcı Frekans:"))
        self.fm_plotButton.setText(_translate("MainWindow", "GRAFİK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Ana Sayfa"))
        self.label_4.setText(_translate("MainWindow", "  Modülasyon Uygulaması"))
        self.label.setText(_translate("MainWindow", "Tasarlayan - Semih ŞEVİK"))
        self.label_2.setText(_translate("MainWindow", "Kaynaklar:"))
        self.commandLinkButton.setText(_translate("MainWindow", "Yapayzekalabs Blog"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "PyQt5 Dökümanları"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Qt Dökümanları"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Hakkında"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

