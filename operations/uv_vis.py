from PyQt5 import QtCore, QtGui, QtWidgets

def uv_vis_UV_VIS(root):
    # Create a frame (widget) inside the root window
    # Create the main widget
    widget = QtWidgets.QWidget()
    widget.setWindowTitle("Widget with Buttons")

    # Create a vertical layout
    layout = QtWidgets.QVBoxLayout()

    # Create buttons and add them to the layout
    button1 = QtWidgets.QPushButton("Button 1")
    layout.addWidget(button1)

    button2 = QtWidgets.QPushButton("Button 2")
    layout.addWidget(button2)

    button3 = QtWidgets.QPushButton("Button 3")
    layout.addWidget(button3)

    # Set the layout for the main widget
    widget.setLayout(layout)

    return widget