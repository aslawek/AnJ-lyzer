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
        my_label = qtw.QLabel('Hello world!')
        my_label.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(my_label)

        # create spin box (QDoubleSpinBox for non-integers)
        my_spin = qtw.QSpinBox(self,
                               value=10,
                               maximum=100,
                               minimum=0,
                               singleStep=5,
                               prefix='#',
                               suffix=' kocik')
        my_spin.setFont(qtg.QFont('Arial', 14))
        self.layout().addWidget(my_spin)

        # create button
        my_button = qtw.QPushButton('Benjamin Button :)',
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            my_label.setText(f'You picked {my_spin.value()}')

app = qtw.QApplication([])
mw = MainWindow()

# run app:
app.exec_()