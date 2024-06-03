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

        # create combo box
        my_combo = qtw.QComboBox(self,
                                 editable = True,
                                 insertPolicy = qtw.QComboBox.InsertAtBottom)
        # add items to combo
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushrom", qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["One", "Two", "Three"])
        my_combo.insertItem(2, "Third Thing")
        self.layout().addWidget(my_combo)

        # create button
        my_button = qtw.QPushButton('Benjamin Button :)',
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            my_label.setText(f'You picked {my_combo.currentText()}')

app = qtw.QApplication([])
mw = MainWindow()

# run app:
app.exec_()