"""
************************************************
-----> Projenin Çalıştırılacağı Ana Dosya <-----
************************************************
"""

from PyQt5.QtWidgets import QApplication
from ana_pencere import Modulation

app = QApplication([])
window = Modulation()
window.show()
app.exec_()