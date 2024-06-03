import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Custom QListWidgetItem Example")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.listWidget = QListWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.listWidget)

        self.addButton = QPushButton("Add Items", self.centralwidget)
        self.addButton.clicked.connect(self.add_custom_items)
        self.verticalLayout.addWidget(self.addButton)

    def add_custom_items(self):
        for i in range(3):
            # Create a custom widget containing a QHBoxLayout
            custom_widget = QWidget()
            layout = QHBoxLayout(custom_widget)
            layout.setContentsMargins(0, 0, 0, 0)

            # Add a checkbox
            checkbox = QCheckBox()
            layout.addWidget(checkbox)

            # Add a QLabel to display text
            label = QLabel(f"Item {i+1}")
            label.setAlignment(Qt.AlignLeft)
            layout.addWidget(label)

            # Add a QPushButton as a remove button
            remove_button = QPushButton("X")
            remove_button.setFixedSize(25, 25)  # Set fixed size to make it square
            remove_button.clicked.connect(self.remove_item)
            layout.addWidget(remove_button)

            # Create a QListWidgetItem and set the custom widget as its item widget
            item = QListWidgetItem()
            item.setSizeHint(custom_widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, custom_widget)

    def remove_item(self):
        button = self.sender()
        item_widget = button.parentWidget()
        item = self.listWidget.itemAt(item_widget.pos())
        if item:
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.setGeometry(300, 150, 400, 300)
    window.show()
    sys.exit(app.exec_())