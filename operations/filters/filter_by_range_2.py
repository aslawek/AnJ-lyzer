from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class FilterByRange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FilterByRange, self).__init__(parent)
        loadUi("./ui/filterui.ui", self)

    def get_data(self):
        pass