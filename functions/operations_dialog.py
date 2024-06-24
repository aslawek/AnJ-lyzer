import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QTreeView, QVBoxLayout, QListWidget, QListWidgetItem, QFileSystemModel, QHeaderView, QDialogButtonBox
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtCore import QModelIndex, pyqtSignal

class OperationsDialog(QDialog):
    accepted = pyqtSignal(list)  # Define a signal to pass list_operations

    def __init__(self, list_operations=None, parent=None):
        super(OperationsDialog, self).__init__(parent)
        loadUi("./ui/operations_dialog.ui", self)
        self.setWindowTitle("Operations Dialog")
        operations_directory = os.path.join(os.getcwd(), 'operations')

        # Initialize the QTreeView and QFileSystemModel
        self.operations_treeView.setHeaderHidden(True)  # Hide default header
        self.model = QFileSystemModel()
        self.model.setRootPath(operations_directory)  # Set the root path to the directory containing the file
        self.operations_treeView.setModel(self.model)
        self.operations_treeView.setRootIndex(self.model.index(operations_directory))

        # Add button handlers
        self.operations_buttonBox.accepted.connect(self.accept)
        self.operations_buttonBox.rejected.connect(self.reject)

        # Set the width of the first column
        header = self.operations_treeView.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Connect double-click event to a slot
        self.operations_treeView.doubleClicked.connect(self.on_tree_double_clicked)

        if list_operations:
            self.list_operations = list_operations
        else:
            self.list_operations = []

        # Make a list from list_operations
        self.operations_listWidget.clear()
        for operation in list_operations:
            item = QListWidgetItem()
            item.setText(operation)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.operations_listWidget.addItem(item)

    def on_tree_double_clicked(self, index: QModelIndex):
        # Check if the item is a directory
        if self.model.isDir(index):
            pass
        else:
            # Get file path of the double-clicked item
            item_path = self.model.filePath(index)
            # Get name of the double-clicked thing (not only file)
            item_sth = self.model.fileName(index)
            # Get names from path
            operations_name = os.path.basename(os.path.dirname(item_path))
            item_name = os.path.basename(item_path)
            # Add item name to QListWidget

            item = QListWidgetItem()
            item.setText(f'{operations_name}\t{item_name}')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.operations_listWidget.addItem(item)

            self.list_operations.append(item)

    def accept(self):
        # Handle OK button click
        self.accepted.emit(self.list_operations)  # Emit accepted signal with list_operations
        self.close()

    def reject(self):
        # Handle Cancel button click
        self.close()

    def closeEvent(self, event):
        # Override closeEvent to handle dialog closure
        self.accepted.emit(self.list_operations)  # Emit accepted signal with list_operations
        event.accept()  # Accept the close event

