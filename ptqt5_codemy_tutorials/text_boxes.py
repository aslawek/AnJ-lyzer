import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello! Pick something from the list")

        # Set verticle layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label, change font size
        my_label = qtw.QLabel('Type something in the box below!')
        my_label.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(my_label)

        # create text box
        my_text = qtw.QTextEdit(self,
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText='Placeholder text!',
                                readOnly=False)
        self.layout().addWidget(my_text)

        # create button
        my_button = qtw.QPushButton('Benjamin Button :)',
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            my_label.setText(f'You typed {my_text.toPlainText()}')
            my_text.setPlainText("You pressed the button!")

app = qtw.QApplication([])
mw = MainWindow()

# run app:
app.exec_()