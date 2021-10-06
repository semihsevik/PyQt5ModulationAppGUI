"""
************************************
-----> AM Modülasyonu Dosyası <-----
************************************
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from scipy import signal
from am_graph import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np

class AmPage(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        icon = "pencere_icons"
        self.setWindowIcon(QIcon(icon)) #Pencere ikonu

        self.addToolBar(NavigationToolbar(self.ui.MplWidget.canvas, self))

    #Buton bağlantıları
        self.ui.am_messageButton.clicked.connect(self.am_messageFunction)
        self.ui.am_carrierButton.clicked.connect(self.am_carrierFunction)
        self.ui.am_modButton.clicked.connect(self.am_modFunction)

#-----------------------------------------------------------------------------------------------------------------------
#Sinüsoidal dalga fonksiyonları

    def am_indexFunction(self, index):
        self.ma_am = index

    def am_fmFunction(self, freq):
        self.message_f = freq

    def am_fcFunction(self, freq_1):
        self.carrier_f = freq_1

        self.t = np.linspace(0.0, 1.0, 44100)
        self.sig_m = np.sin(2 * np.pi * self.message_f * self.t)  # Fm frekansli bir sinus dalgasi
        self.sig_c = np.sin(2 * np.pi * self.carrier_f * self.t)  # Fc frekansli bir sinus dalgasi
        self.sig_mod = (1 + self.ma_am * self.sig_m) * self.sig_c

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_mod)
        self.ui.MplWidget.canvas.axes.set_title('Genlik Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
#Kare dalga fonksiyonları

    def am_indexFunction_1(self,index):
        self.ma_am = index

    def am_fmFunction_1(self,freq):
        self.message_f = freq

    def am_fcFunction_1(self,freq_1):
        self.carrier_f = freq_1

        self.t = np.linspace(0.0, 1.0, 44100)
        self.sig_m = signal.square(2 * np.pi * self.message_f * self.t)
        self.sig_c = np.sin(2 * np.pi * self.carrier_f * self.t)  # Fc frekansli bir sinus dalgasi
        self.sig_mod = (1 + (self.ma_am * self.sig_m)) * self.sig_c

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_mod)
        self.ui.MplWidget.canvas.axes.set_title('Genlik Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
#Mesaj-kariyer-modüleli sinyal gösterimi

    def am_messageFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t,self.sig_m)
        self.ui.MplWidget.canvas.axes.set_title('Mesaj Sinyali')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

    def am_carrierFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_c)
        self.ui.MplWidget.canvas.axes.set_title('Taşıyıcı Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

    def am_modFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t,self.sig_mod)
        self.ui.MplWidget.canvas.axes.set_title('Genlik Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()
