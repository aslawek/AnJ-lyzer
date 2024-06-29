import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Parent Widget')

        self.child_widget = ChildWidget(self)
        self.child_widget.setGeometry(50, 50, 300, 200)

        self.show()

class ChildWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.label = QLabel('This is a child widget', self)
        self.label.setGeometry(50, 50, 200, 30)

        self.button = QPushButton('Click Me', self)
        self.button.setGeometry(50, 100, 100, 30)
        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.label.setText('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    parent = ParentWidget()
    sys.exit(app.exec_())