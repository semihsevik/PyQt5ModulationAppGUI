"""
*********************************
-----> Ana Pencere Dosyası <-----
*********************************
"""

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon,QPixmap
from project_design import Ui_MainWindow
from fm_pencere import FmPage
from am_pencere import AmPage


class Modulation(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #Tasarım ikonlar 
    #-------------------------------------------------------------------------------------------------------------------
        icon = "Modulation.jpg"
        self.setWindowIcon(QIcon(icon))

        icon_1 = "plotButtons_icon.png"
        self.ui.fm_plotButton.setIcon(QIcon(icon_1))
        self.ui.am_plotButton.setIcon(QIcon(icon_1))

        icon_2 = "kaynak_icon.png"
        self.ui.commandLinkButton.setIcon(QIcon(icon_2))
        self.ui.commandLinkButton_2.setIcon(QIcon(icon_2))
        self.ui.commandLinkButton_3.setIcon(QIcon(icon_2))

        icon2 = QIcon()
        icon2.addPixmap(QPixmap("main_tab.png"), QIcon.Normal, QIcon.Off)
        self.ui.tabWidget.addTab(self.ui.tab_3, icon2, "Ana Sayfa")
        

        icon4 = QIcon()
        icon4.addPixmap(QPixmap("about_tab.png"), QIcon.Normal, QIcon.Off)
        self.ui.tabWidget.addTab(self.ui.tab_4, icon4, "Hakkında")

        self.ui.label_3 = QLabel(self.ui.tab_4)
        self.ui.label_3.setText("")
        self.ui.label_3.setPixmap(QPixmap("koü.jpg"))
        self.ui.label_3.setObjectName("label_3")
        self.ui.verticalLayout_4.addWidget(self.ui.label_3)
    #-------------------------------------------------------------------------------------------------------------------

    #Kaynakça butonları bağlantısı
        self.ui.commandLinkButton.clicked.connect(self.open_browser)
        self.ui.commandLinkButton_2.clicked.connect(self.open_browser_1)
        self.ui.commandLinkButton_3.clicked.connect(self.open_browser_2)
    
    #-------------------------------------------------------------------------------------------------------------------

    #FM slider-spinbox bağlantıları

        self.ui.fm_messageSlider.valueChanged.connect(self.ui.fm_messageFrequency.setValue)
        self.ui.fm_messageFrequency.valueChanged.connect(self.ui.fm_messageSlider.setValue)
        self.ui.fm_carrierSlider.valueChanged.connect(self.ui.fm_carrierFrequency.setValue)
        self.ui.fm_carrierFrequency.valueChanged.connect(self.ui.fm_carrierSlider.setValue)

    #AM slider-spinbox bağlantıları

        self.ui.am_messageSlider.valueChanged.connect(self.ui.am_messageFrequency.setValue)
        self.ui.am_messageFrequency.valueChanged.connect(self.ui.am_messageSlider.setValue)
        self.ui.am_carrierSlider.valueChanged.connect(self.ui.am_carrierFrequency.setValue)
        self.ui.am_carrierFrequency.valueChanged.connect(self.ui.am_carrierSlider.setValue)

    #2. ve 3. sayfaların nesneleri

        self.fm_plot = FmPage()
        self.am_plot = AmPage()

    #Plot butonlarının bağlantısı

        self.ui.am_plotButton.clicked.connect(self.open_amPage)
        self.ui.fm_plotButton.clicked.connect(self.open_fmPage)

    #FM sayfası fonksiyonu

    def open_fmPage (self):

        if self.ui.fm_sinWave.isChecked(): # Sinüsoidal butonu seçildiğinde

            self.fm_plot.show()
            fm_ma = self.ui.fm_modulationIndex.value()
            self.fm_plot.fm_indexFunction(fm_ma)
            fm_fm = self.ui.fm_messageFrequency.value()
            self.fm_plot.fm_fmFunction(fm_fm)
            fm_fc = self.ui.fm_carrierFrequency.value()
            self.fm_plot.fm_fcFunction(fm_fc)

        elif self.ui.fm_squareWave.isChecked(): #Square butonu seçildiğinde

            self.fm_plot.show()
            fm_ma_1 = self.ui.fm_modulationIndex.value()
            self.fm_plot.fm_indexFunction_1(fm_ma_1)
            fm_fm_1 = self.ui.fm_messageFrequency.value()
            self.fm_plot.fm_fmFunction_1(fm_fm_1)
            fm_fc_1 = self.ui.fm_carrierFrequency.value()
            self.fm_plot.fm_fcFunction_1(fm_fc_1)

        else: #Herhangi bir seçim yapılmadığında

            QMessageBox.warning(self,"Uyarı","Lütfen mesaj sinyalinin tipini seçin !")
            self.fm_plot.close()
        


    #AM sayfası fonksiyonu

    def open_amPage(self):
        

        if self.ui.am_sinWave.isChecked(): #Sinüsoidal butonu seçildiğinde
            self.am_plot.show()
            am_ma = self.ui.am_modulationIndex.value()
            self.am_plot.am_indexFunction(am_ma)
            am_fm = self.ui.am_messageFrequency.value()
            self.am_plot.am_fmFunction(am_fm)
            am_fc = self.ui.am_carrierFrequency.value()
            self.am_plot.am_fcFunction(am_fc)

        elif self.ui.am_squareWave.isChecked(): #Square butonu seçildiğinde
            self.am_plot.show()
            am_ma_1 = self.ui.am_modulationIndex.value()
            self.am_plot.am_indexFunction_1(am_ma_1)
            am_fm_1 = self.ui.am_messageFrequency.value()
            self.am_plot.am_fmFunction_1(am_fm_1)
            am_fc_1 = self.ui.am_carrierFrequency.value()
            self.am_plot.am_fcFunction_1(am_fc_1)

        else: #Herhangi bir seçim yapılmadığında
            QMessageBox.warning(self,"Uyarı","Lütfen mesaj sinyalinin tipini seçin !")
            self.am_plot.close()

#Kaynakların web bağlantı fonksiyonları
#---------------------------------------------------------------------------------------------------------------------------
    def open_browser(self):
        self.browser = QWebEngineView()
        self.browser.load(QUrl('http://yapayzekalabs.blogspot.com/'))
        icon_3 = 'search_icon.png'
        self.browser.setWindowIcon(QIcon(icon_3))

        self.browser.show()

    def open_browser_1(self):
        self.browser_1 = QWebEngineView()
        self.browser_1.load(QUrl('https://doc.bccnsoft.com/docs/PyQt5/'))
        icon_3 = 'search_icon.png'
        self.browser_1.setWindowIcon(QIcon(icon_3))
        self.browser_1.show()

    def open_browser_2(self):
        self.browser_2 = QWebEngineView()
        self.browser_2.load(QUrl('https://doc.qt.io/'))
        icon_3 = 'search_icon.png'
        self.browser_2.setWindowIcon(QIcon(icon_3))
        self.browser_2.show()
        



