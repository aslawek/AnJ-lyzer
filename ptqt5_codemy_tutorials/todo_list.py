# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyqt5_designer\to_do_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 60, 161, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget,  clicked= lambda: self.delete_it())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(180, 60, 171, 41))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget,  clicked= lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(360, 60, 151, 41))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(10, 10, 501, 41))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(10, 110, 501, 331))
        self.myList_listWidget.setObjectName("myList_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add item to list
    def add_it(self):
        # grab text from listbox
        item = self.addItem_lineEdit.text()
        # add item
        self.myList_listWidget.addItem(item)
        # clear the item box
        self.addItem_lineEdit.setText("")
        pass

    # add item to list
    def delete_it(self):
        # grab the selected/current row
        clicked_index = self.myList_listWidget.currentRow()
        self.myList_listWidget.takeItem(clicked_index)

    # add item to list
    def clear_it(self):
        self.myList_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To do list"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Clear the List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
