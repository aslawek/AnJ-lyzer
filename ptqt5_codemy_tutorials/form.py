import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello! Pick something from the list")

        # Set form layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # add stuff to form layout
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont('Arial', 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # add rows to app
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Press me",
                                           clicked=lambda : press_it()))

        # show the app
        self.show()

        def press_it():
            label_1.setText(f'You clicked the button, {f_name.text()}!')

app = qtw.QApplication([])
mw = MainWindow()

# run app:
app.exec_()