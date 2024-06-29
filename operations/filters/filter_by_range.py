from PyQt5 import QtCore, QtGui, QtWidgets

class FilterByRange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FilterByRange, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("FilterByRange")
        self.setGeometry(QtCore.QRect(0, 0, 410, 65))

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 131, 25))
        self.comboBox.setObjectName("comboBox")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(230, 30, 81, 25))
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 30, 81, 25))
        self.textEdit_2.setObjectName("textEdit_2")

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(16, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Filter"))
        self.label_2.setText(_translate("Form", "From"))
        self.label_3.setText(_translate("Form", "To"))

    def get_data(self):
        # Example method to retrieve data from the widget
        filter_text = self.label.text()
        from_text = self.label_2.text()
        to_text = self.label_3.text()
        return filter_text, from_text, to_text