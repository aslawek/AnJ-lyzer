import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello! What's your name?")

        # Set verticle layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label, change font size
        my_label = qtw.QLabel('Hello world!')
        my_label.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(my_label)

        # create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('Name field')
        my_entry.setText('')
        self.layout().addWidget(my_entry)

        # create button
        my_button = qtw.QPushButton('Benjamin Button :)',
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()

# run app:
app.exec_()