from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QTextEdit


class FilterByRange(QWidget):
    def __init__(self, parent=None):
        super(FilterByRange, self).__init__(parent)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Option 1", "Option 2", "Option 3"])

        self.textEdit1 = QTextEdit(self)
        self.textEdit2 = QTextEdit(self)

        layout = QVBoxLayout()
        #layout.addWidget(self.comboBox)
        #layout.addWidget(self.textEdit1)
        #layout.addWidget(self.textEdit2)

        self.setLayout(layout)

    def function(self):
        pass