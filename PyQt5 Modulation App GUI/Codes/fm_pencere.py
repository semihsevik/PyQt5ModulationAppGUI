"""
************************************
-----> FM Modülasyonu Dosyası <-----
************************************
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from scipy import signal
from fm_graph import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np

class FmPage(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    
        icon = "pencere_icons"
        self.setWindowIcon(QIcon(icon))  #Pencere ikonu

        self.addToolBar(NavigationToolbar(self.ui.MplWidget.canvas, self))

    #Buton bağlantıları
        self.ui.fm_messageButton.clicked.connect(self.fm_messageFunction)
        self.ui.fm_carrierButton.clicked.connect(self.fm_carrierFunction)
        self.ui.fm_modButton.clicked.connect(self.fm_modFunction)

#-----------------------------------------------------------------------------------------------------------------------
#Sinüsoidal dalga fonksiyonları

    def fm_indexFunction(self,index):
        self.ma_fm = index

    def fm_fmFunction(self,freq):
        self.message_f = freq

    def fm_fcFunction(self,freq_1):
        self.carrier_f = freq_1
        self.t = np.arange(0., 1., 1. / 44100.0)
        self.sig_fm = np.sin(2. * np.pi * self.message_f * self.t) 
        self.sig_fc = np.sin(2. * np.pi * self.carrier_f * self.t)
        self.sig_fmod = np.sin(2. * np.pi * self.carrier_f * self.t + self.ma_fm * self.sig_fm)

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_fmod,"red")
        self.ui.MplWidget.canvas.axes.set_title('Frekans Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()
        
#-----------------------------------------------------------------------------------------------------------------------
#Kare dalga fonksiyonları

    def fm_indexFunction_1(self,index):
        self.ma_fm = index

    def fm_fmFunction_1(self,freq):
        self.message_f = freq

    def fm_fcFunction_1(self,freq_1):
        self.carrier_f = freq_1

        self.t = np.arange(0., 1., 1. / 44100.0)
        self.sig_fm = (signal.square(2 * np.pi * self.message_f * self.t))
        self.sig_fc = np.sin(2. * np.pi * self.carrier_f * self.t)
        self.sig_fmod = np.sin(2. * np.pi * self.carrier_f * self.t + self.ma_fm * self.sig_fm)

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_fmod, "red")
        self.ui.MplWidget.canvas.axes.set_title('Frekans Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
#Mesaj-kariyer-modüleli sinyal gösterimi

    def fm_messageFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t,self.sig_fm,"red")
        self.ui.MplWidget.canvas.axes.set_title('Mesaj Sinyali')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

    def fm_carrierFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t, self.sig_fc,"red")
        self.ui.MplWidget.canvas.axes.set_title('Taşıyıcı Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

    def fm_modFunction(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.t,self.sig_fmod,"red")
        self.ui.MplWidget.canvas.axes.set_title('Frekans Modüleli Sinyal')
        self.ui.MplWidget.canvas.axes.set_xlabel('t')
        self.ui.MplWidget.canvas.axes.set_ylabel('Genlik')
        self.ui.MplWidget.canvas.draw()

