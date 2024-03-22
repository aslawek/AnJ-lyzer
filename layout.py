from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XXX')
        self.setGeometry(100, 100, 1000, 800)

        box_left = QtWidgets.QGroupBox()
        box_right = QtWidgets.QGroupBox()

        box_left.setStyleSheet("background-color: lightgreen")
        box_right.setStyleSheet("background-color: lightblue")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(box_left, 0)
        layout.addWidget(box_right, 0)
        self.setLayout(layout)

        list_box = QtWidgets.QListWidget(box_right)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())



