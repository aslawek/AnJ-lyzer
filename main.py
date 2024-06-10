from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
import os
import pandas as pd
import pickle
from datetime import datetime

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("mainui.ui", self)
        self.newProject_pushButton.clicked.connect(self.new_project)
        self.saveProject_pushButton.clicked.connect(self.save_project)
        self.saveAsProject_pushButton.clicked.connect(self.save_project_as)
        self.openProject_pushButton.clicked.connect(self.open_project)
        self.openProject_pushButton.clicked.connect(self.open_project)
        self.newProject_pushButton.clicked.connect(self.new_project)
        self.reloadData_pushButton.clicked.connect(self.data_to_dataframe)
        self.importRawData_pushButton.clicked.connect(self.import_raw_data)
        self.clearAll_pushButton.clicked.connect(self.clear_all_fileList)
        self.inverseMark_pushButton.clicked.connect(self.inverse_mark_fileList)
        self.clearMarked_pushButton.clicked.connect(self.clear_marked_fileList)
        self.clearSelected_pushButton.clicked.connect(self.clear_selected_fileList)
        self.markAll_pushButton.clicked.connect(self.mark_all_fileList)

        # Create blank project to initialize self.current_data
        self.create_blank_project()

    def create_blank_project(self):
        self.current_project = {
            "project_name": "",
            "project_path": "",
            "preload": {
                "reload_automatically": False,
                "skip_rows": False,
                "skip_rows_number": "",
                "find_header": False,
                "find_header_phrase": "",
                "defined_in": False,
                "defined_in_row": "",
                "defined_in_column": "",
                "add_header": False,
                "add_header_text": "",
                "decimal_separator": ".",
                "delimiter": "Tab"
            },
            "list_variables": [],
            "list_data": []
        }

    def new_project(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Create New Project", "projects",
                                                             "Project Files (*.pkl);;All Files (*)", options=options)
        if file_name:
            # Get project name from path
            project_name = os.path.splitext(os.path.basename(file_name))[0]
            # Append ".pkl" extension if not already present
            if not file_name.endswith(".pkl"):
                file_name += ".pkl"
            # A dict containing empty project
            self.current_project = {
                "project_name": project_name,
                "project_path": file_name,
                "preload": {
                    "reload_automatically": False,
                    "skip_rows": False,
                    "skip_rows_number": "",
                    "find_header": False,
                    "find_header_phrase": "",
                    "defined_in": False,
                    "defined_in_row": "",
                    "defined_in_column": "",
                    "add_header": False,
                    "add_header_text": "",
                    "decimal_separator": ".",
                    "delimiter": "Tab"
                },
                "list_data": []
            }
            # Process the selected file_name
            self.print_to_terminal(f"New project created: {project_name}, saved in {file_name}")
            # Save data as pickle
            with open(file_name, 'wb') as file:
                pickle.dump(self.current_project, file)
            print("Data saved as pickle.")
            self.update_preload_options()
            self.projectName_lineEdit.setText(self.current_project["project_name"])
            self.projectSize_textBrowser.setText(self.get_size(self.current_project))
            print(self.current_project)

    def save_project(self):
        # gets preload options and updates current project dict
        self.preload_options_to_current_data()
        # Save data as pickle
        with open(self.current_project["project_path"], 'wb') as file:
            pickle.dump(self.current_project, file)
        print("Data saved as pickle.")
        self.update_preload_options()
        self.projectSize_textBrowser.setText(self.get_size(self.current_project))

    def save_project_as(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Project As...", "projects",
                                                             "Project Files (*.pkl);;All Files (*)", options=options)
        if file_name:
            self.preload_options_to_current_data()
            # Append ".pkl" extension if not already present
            if not file_name.endswith(".pkl"):
                file_name += ".pkl"
            # Process the selected file_name
            print("New project file created:", file_name)
            # Save data as pickle
            with open(file_name, 'wb') as file:
                pickle.dump(self.current_project, file)
            print("Data saved as pickle.")
            self.update_preload_options()
            print(self.current_project)

    def open_project(self):
        default_project_path = os.path.join(os.path.dirname(__file__), "projects")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open Project", default_project_path,
                                                             "Project Files (*.pkl)", options=options)
        if file_name:
            # Process the selected file_name
            print("Opening project file:", file_name)

            # Load data from the .pkl file
            with open(file_name, 'rb') as file:
                self.current_project = pickle.load(file)

            # Process the loaded data (e.g., display, analyze, etc.)
            print(f'Data loaded from project: {self.current_project["project_name"]}')
            self.projectSize_textBrowser.setText(self.get_size(self.current_project))
            self.projectName_lineEdit.setText(self.current_project["project_name"])
            self.update_preload_options()

    def import_raw_data(self):
        print("Importing raw data...")
        # Open a file dialog to select multiple files
        file_dialog = QtWidgets.QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(None, "Select Files", "", "All Files (*)")
        if file_paths:
            # Add each file to the list widget
            for file_path in file_paths:
                data_name = os.path.splitext(os.path.basename(file_path))[0]
                with open(file_path, 'r') as file:
                    data = file.read()
                self.current_project["list_data"].append({"name": data_name, "path": file_path, "data": data})
                self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data))
                item = QtWidgets.QListWidgetItem()
                item.setText(file_path)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.filelist_listWidget.addItem(item)
                if self.current_project["preload"]["reload_automatically"]:
                    self.data_to_dataframe()

    def updata_filelist(self):
        file_paths = self.current_project["list_data"]['path']
        for file_path in file_paths:
            item = QtWidgets.QListWidgetItem()
            item.setText(file_path)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.filelist_listWidget.addItem(item)

    def data_to_dataframe(self):
        preload = self.current_project["preload"]
        decimal_separator = preload["decimal_separator"]
        if preload["delimiter"] == "Tab":
            delimiter = '\t'
        else:
            delimiter = '\t'

        if preload['skip_rows'] == True:
            n_rows_to_skip = preload["skip_rows_number"]
            print(f'Loading data, skipping {n_rows_to_skip} rows')
            for data in self.current_project['list_data']:
                data['data'] = pd.read_csv(data["path"], encoding="ISO-8859-1", skiprows=int(n_rows_to_skip),
                                           sep=delimiter)
                self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data['data']))
        elif preload["find_header"] == True:
            header_phrase = preload["find_header_phrase"]
            print(f'Looking for the phrase {header_phrase} included in header')
        elif preload["defined_in"] == True:
            defined_in_row = preload["defined_in_row"]
            defined_in_column = preload["defined_in_column"]

        if preload["add_header"] == True:
            new_header = preload["add_header_text"]
            print(f"Adding header to the file: {new_header}")

    def data_preview(self):
        pass

        # data = pd.read_csv(f'{file_path}', encoding="ISO-8859-1", skiprows=65, sep='\t')
        # data = pd.read_csv(f'{file_path}', encoding="ISO-8859-1", skiprows=rows_to_skip, sep='\t')[
        #    ['time/s', 'control/V', 'Ewe/V', label_I]] \
        #    .rename(columns={'<I>/mA': 'I/mA'})

        # Change '.' for "," for all columns (if needed):
        # for column in data:
        #    if data[column].dtype == object:
        #        data[column] = data[column].str.replace(',', '.').astype(float)
        # return data
        # pass
        # Functions for preloading data import settings

    def load_preload(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDirectory('./preload/')
        file_path, _ = file_dialog.getOpenFileNames(None, "Select Preload File", "preload", "All Files (*)")
        with open(file_path[0], 'rb') as file:
            preload = pickle.load(file)
            self.current_project["preload"] = preload
        print(self.current_project['preload'])
        self.update_preload_options()

    def save_preload(self):
        # Gets the preload values from import options window
        preload = {
            "reload_automatically": self.reloadAutomatically_checkBox.isChecked(),
            "skip_rows": self.skipNRows_checkBox.isChecked(),
            "skip_rows_number": self.skipNRows_textEdit.toPlainText(),
            "find_header": self.findHeader_checkBox.isChecked(),
            "find_header_phrase": self.findHeader_textEdit.toPlainText(),
            "defined_in": self.definedIn_checkBox.isChecked(),
            "defined_in_row": self.rowDefinedIn_textEdit.toPlainText(),
            "defined_in_column": self.columnDefinedIn_textEdit.toPlainText(),
            "add_header": self.addHeader_checkBox.isChecked(),
            "add_header_text": self.addHeader_textEdit.toPlainText(),
            "decimal_separator": self.decimalSeparator_textEdit.toPlainText(),
            "delimiter": self.delimiter_comboBox.currentText()
        }
        # Opens window for saving preload
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDirectory('./preload/')
        file_path, _ = file_dialog.getSaveFileName(None, "Save Preload", "", "Pickle files (*.pkl)")
        # Check if a file path is selected
        if file_path:
            # Save the dictionary to a file in Pickle format
            with open(file_path, 'wb') as f:
                pickle.dump(preload, f)

    def update_preload_options(self):
        self.reloadAutomatically_checkBox.setChecked(self.current_project["preload"]["reload_automatically"])
        self.skipNRows_checkBox.setChecked(self.current_project["preload"]["skip_rows"])
        self.skipNRows_textEdit.setText(str(self.current_project["preload"]["skip_rows_number"]))
        self.findHeader_checkBox.setChecked(self.current_project["preload"]["find_header"])
        self.findHeader_textEdit.setText(str(self.current_project["preload"]["find_header_phrase"]))
        self.definedIn_checkBox.setChecked(self.current_project["preload"]["defined_in"])
        self.rowDefinedIn_textEdit.setText(str(self.current_project["preload"]["defined_in_row"]))
        self.columnDefinedIn_textEdit.setText(str(self.current_project["preload"]["defined_in_column"]))
        self.addHeader_checkBox.setChecked(self.current_project["preload"]["add_header"])
        self.addHeader_textEdit.setText(str(self.current_project["preload"]["add_header_text"]))
        self.decimalSeparator_textEdit.setText(str(self.current_project["preload"]["decimal_separator"]))
        self.delimiter_comboBox.setCurrentText(str(self.current_project["preload"]["delimiter"]))

    def preload_options_to_current_data(self):
        preload = {
            "reload_automatically": self.reloadAutomatically_checkBox.isChecked(),
            "skip_rows": self.skipNRows_checkBox.isChecked(),
            "skip_rows_number": self.skipNRows_textEdit.toPlainText(),
            "find_header": self.findHeader_checkBox.isChecked(),
            "find_header_phrase": self.findHeader_textEdit.toPlainText(),
            "defined_in": self.definedIn_checkBox.isChecked(),
            "defined_in_row": self.rowDefinedIn_textEdit.toPlainText(),
            "defined_in_column": self.columnDefinedIn_textEdit.toPlainText(),
            "add_header": self.addHeader_checkBox.isChecked(),
            "add_header_text": self.addHeader_textEdit.toPlainText(),
            "decimal_separator": self.decimalSeparator_textEdit.toPlainText(),
            "delimiter": self.delimiter_comboBox.currentText()
        }
        self.current_project["preload"] = preload

    # Functions for Mark buttons (all/none/inverse)
    def mark_all_fileList(self):
        all_checked = True
        for index in range(self.filelist_listWidget.count()):
            item = self.filelist_listWidget.item(index)
            if item.checkState() != QtCore.Qt.Checked:
                all_checked = False
                break
        if all_checked:
            for index in range(self.filelist_listWidget.count()):
                item = self.filelist_listWidget.item(index)
                item.setCheckState(QtCore.Qt.Unchecked)
        else:
            for index in range(self.filelist_listWidget.count()):
                item = self.filelist_listWidget.item(index)
                item.setCheckState(QtCore.Qt.Checked)

    def inverse_mark_fileList(self):
        for index in range(self.filelist_listWidget.count()):
            item = self.filelist_listWidget.item(index)
            current_state = item.checkState()
            if current_state == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            elif current_state == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)
        # Functions for Clear buttons (selected/marked/all)

    def clear_selected_fileList(self):
        selected_item = self.filelist_listWidget.currentItem()
        if selected_item:
            self.filelist_listWidget.takeItem(self.filelist_listWidget.row(selected_item))

    def clear_marked_fileList(self):
        checked_items = []
        for index in range(self.filelist_listWidget.count()):
            item = self.filelist_listWidget.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                checked_items.append(item)
        for item in checked_items:
            self.filelist_listWidget.takeItem(self.filelist_listWidget.row(item))

    def clear_all_fileList(self):
        self.filelist_listWidget.clear()

    def get_size(self, dict):
        size = len(dict)
        size_bytes = size * 8
        print(f'File size is: {size_bytes} B')
        # Define suffixes for different sizes
        suffixes = ['B', 'kB', 'MB', 'GB', 'TB']
        # Find the appropriate suffix
        suffix_index = 0
        while size_bytes >= 1024 and suffix_index < len(suffixes) - 1:
            size_bytes /= 1024
            suffix_index += 1
        # Return the size with the appropriate suffix
        return "{:.2f} {}".format(size_bytes, suffixes[suffix_index])

    def df_to_text_or_add_line_numbers(self, text):
        # Checks if data is already pandas dataframe
        if isinstance(text, pd.DataFrame):
            text = text.head(100).to_csv(index=True, header=True, sep='\t')
            return text
        else:
            # Modifies plain data, gets first 100 lines, adds number of line
            lines = text.split('\n')[:100]  # Limit to the first 100 lines
            numbered_lines = [f'<font color="red">{i + 1}:</font>\t{line}' for i, line in enumerate(lines)]
            numbered_text = '<br>'.join(numbered_lines)
            return numbered_text

    def print_to_terminal(self, text):
        # Get the current date and time and format it
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        #self.terminal_textBrowser.setText(" HELLO ! ")
        #self.terminal_textBrowser.append(f'{current_datetime} {text}')
        formatted_text = f'<span style="color: blue;"><b>{current_datetime}</b></span> {text}'
        self.terminal_textBrowser.append(formatted_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
