from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("clicked!")

def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 500, 500)
    window.setWindowTitle('AnJ-lyzer')

    label = QtWidgets.QLabel(window)
    label.setText('DUPA')
    label.move(50, 50)

    btn_1 = QtWidgets.QPushButton(window)
    btn_1.setText("Click!")
    btn_1.clicked.connect(clicked)

    window.show()
    sys.exit(app.exec_())

window()