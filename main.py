from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
from io import StringIO
import pickle
from datetime import datetime
#matplotlib.use('TkAgg')
#matplotlib.use('Qt5Agg')

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("mainui.ui", self)
        self.newProject_pushButton.clicked.connect(self.new_project)
        self.saveProject_pushButton.clicked.connect(self.save_project)
        self.saveAsProject_pushButton.clicked.connect(self.save_project_as)
        self.openProject_pushButton.clicked.connect(self.open_project)
        self.reloadMarked_pushButton.clicked.connect(self.reload_marked_data)
        self.reloadAll_pushButton.clicked.connect(self.reload_all_data)
        self.importRawData_pushButton.clicked.connect(self.import_raw_data)
        self.clearAll_pushButton.clicked.connect(self.clear_all_fileList)
        self.inverseMark_pushButton.clicked.connect(self.inverse_mark_fileList)
        self.clearMarked_pushButton.clicked.connect(self.clear_marked_fileList)
        self.clearSelected_pushButton.clicked.connect(self.clear_selected_fileList)
        self.markAll_pushButton.clicked.connect(self.mark_all_fileList)
        self.filelist_listWidget.itemSelectionChanged.connect(self.handle_filelist_item_selection)
        self.previewHeader_pushButton.clicked.connect(self.data_preview)
        self.okVariables_pushButton.clicked.connect(self.ok_variables)
        self.removeVariables_pushButton.clicked.connect(self.rm_variables)

        # To handle that only one checkbox is checked
        self.skipNRows_checkBox.stateChanged.connect(self.handle_checkboxes_for_import_options)
        self.definedIn_checkBox.stateChanged.connect(self.handle_checkboxes_for_import_options)
        self.findHeader_checkBox.stateChanged.connect(self.handle_checkboxes_for_import_options)

        # Plotting buttons
        self.plotSelected2DXY_pushButton.clicked.connect(self.plot_selected_2D_XY)
        self.plotMarked2DXY_pushButton.clicked.connect(self.plot_marked_2D_XY)

        # Create blank project to initialize self.current_data
        self.create_blank_project()

    def create_blank_project(self):
        self.print_to_terminal("Let's Get Ready To Rumble!")
        self.current_project = {
            "name": "",
            "path": "",
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
                "name": project_name,
                "path": file_name,
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
            self.print_to_terminal(f"New project {project_name} created and saved in {file_name}")
            # Save data as pickle
            with open(file_name, 'wb') as file:
                pickle.dump(self.current_project, file)
            self.update_preload_options()
            self.projectName_lineEdit.setText(self.current_project["name"])
            self.projectSize_textBrowser.setText(self.get_size(self.current_project))
            self.preview_textBrowser.clear()
            print(self.current_project)

    def open_project(self):
        default_project_path = os.path.join(os.path.dirname(__file__), "projects")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        options |= QtWidgets.QFileDialog.DontResolveSymlinks
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open Project", default_project_path,
                                                             "Project Files (*.pkl)", options=options)
        if file_name:
            # Load data from the .pkl file
            with open(file_name, 'rb') as file:
                self.current_project = pickle.load(file)

            self.print_to_terminal(f'Opening project {self.current_project["name"]} from {self.current_project["path"]}')
            # Process the loaded data (e.g., display, analyze, etc.)
            self.projectSize_textBrowser.setText(self.get_size(self.current_project))
            self.projectName_lineEdit.setText(self.current_project["name"])
            self.update_preload_options()
            self.update_filelist()
            # Selects the last item
            self.filelist_listWidget.setCurrentRow(self.filelist_listWidget.count() - 1)

    def save_project(self):
        # gets preload options and updates current project dict
        self.preload_options_to_current_data()
        # Save data as pickle
        with open(self.current_project["path"], 'wb') as file:
            pickle.dump(self.current_project, file)
        self.print_to_terminal(f"Project {self.current_project['name']} saved in {self.current_project['path']}")
        self.update_preload_options()
        self.projectSize_textBrowser.setText(self.get_size(self.current_project))

    def save_project_as(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Project As...", "projects",
                                                             "Project Files (*.pkl);;All Files (*)", options=options)
        if file_path:
            self.preload_options_to_current_data()
            # Append ".pkl" extension if not already present
            if not file_path.endswith(".pkl"):
                file_path += ".pkl"
            self.current_project["path"] = file_path
            self.current_project["name"] = os.path.splitext(os.path.basename(file_path))[0]
            # Process the selected file_name
            self.print_to_terminal(f"Project {self.current_project['name']} saved as in {self.current_project['path']}")
            # Save data as pickle
            with open(file_path, 'wb') as file:
                pickle.dump(self.current_project, file)
            self.projectSize_textBrowser.setText(self.get_size(self.current_project))
            self.projectName_lineEdit.setText(self.current_project["name"])
            self.update_preload_options()

    def import_raw_data(self):
        self.print_to_terminal("Importing raw data...")
        # Open a file dialog to select multiple files
        file_dialog = QtWidgets.QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(None, "Select Files", "data_examples", "All Files (*)")
        if file_paths:
            # Add each file to the list widget
            for file_path in file_paths:
                data_name = os.path.splitext(os.path.basename(file_path))[0]
                with open(file_path, 'r') as file:
                    data = file.read()
                self.current_project["list_data"].append({"name": data_name, "path": file_path, "data": data})
                if self.current_project["preload"]["reload_automatically"]:
                    self.data_to_dataframe()
            self.update_filelist()
        self.filelist_listWidget.setCurrentRow(self.filelist_listWidget.count() - 1)

    def update_filelist(self):
        self.filelist_listWidget.clear()
        for data in self.current_project["list_data"]:
            item = QtWidgets.QListWidgetItem()
            item.setText(data["name"])
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.filelist_listWidget.addItem(item)

    def update_variables_list(self, data):
        self.variables_listWidget.clear()
        if self.check_panda(data):
            for variable in list(data.columns):
                item = QtWidgets.QListWidgetItem()
                item.setText(variable)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.variables_listWidget.addItem(item)
            self.update_plot_combo_boxes()

    # Functions to remove variables
    def rm_variables(self):
        variables_indexes_to_remove = []
        for index in range(self.variables_listWidget.count()):
            item = self.variables_listWidget.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                variables_indexes_to_remove.append(index)
                item.setCheckState(QtCore.Qt.Unchecked)
        print(variables_indexes_to_remove)
        for index in variables_indexes_to_remove:
            self.variables_listWidget.takeItem(index)
        for data in self.current_project["list_data"]:
            data['data'].drop(data['data'].columns[variables_indexes_to_remove], axis=1, inplace=True)
            self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data['data']))
        self.update_plot_combo_boxes()

    def ok_variables(self):
        variables_indexes_to_remove = []
        for index in range(self.variables_listWidget.count()):
            item = self.variables_listWidget.item(index)
            if item.checkState() != QtCore.Qt.Checked:
                variables_indexes_to_remove.append(index)
        for index in reversed(variables_indexes_to_remove):
            self.variables_listWidget.takeItem(index)
        # Remove unchecked columns from each DataFrame in the list_data
        for data in self.current_project["list_data"]:
            unchecked_columns = [data['data'].columns[index] for index in variables_indexes_to_remove]
            data['data'].drop(columns=unchecked_columns, inplace=True)
            self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data['data']))
        # Uncheck all items
        for index in range(self.variables_listWidget.count()):
            item = self.variables_listWidget.item(index)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.update_plot_combo_boxes()

    def reload_all_data(self):
        self.preload_options_to_current_data()
        for data in self.current_project["list_data"]:
            data["data"] = self.data_to_dataframe(data)
        self.update_plot_combo_boxes()

    def reload_marked_data(self):
        self.preload_options_to_current_data()
        data_to_reload = []
        for index in range(self.filelist_listWidget.count()):
            item = self.filelist_listWidget.item(index)
            current_state = item.checkState()
            if current_state == QtCore.Qt.Checked:
                data_to_reload.append(index)
            item.setCheckState(QtCore.Qt.Unchecked)
        for index in data_to_reload:
            self.current_project["list_data"][index]["data"] = self.data_to_dataframe(self.current_project["list_data"][index])
        self.update_plot_combo_boxes()

    def data_preview(self):
        # Function just to preview loading data. Does not overwrite anything
        self.preload_options_to_current_data()
        selected_index = self.filelist_listWidget.currentRow()
        data_to_show = self.data_to_dataframe(self.current_project["list_data"][selected_index])
        self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data_to_show))
        self.check_panda(data_to_show)
        self.update_variables_list(data_to_show)

    def data_to_dataframe(self, data):
        preload = self.current_project["preload"]
        decimal_separator = preload["decimal_separator"]
        if preload["delimiter"] == "Tab":
            delimiter = '\t'
        elif preload['delimiter'] == "Space":
            delimiter = " "
            print("delimiter is space")
        else:
            delimiter = '\t'

        if preload['skip_rows'] == True:
            n_rows_to_skip = preload["skip_rows_number"]
            print(f'Loading data, skipping {n_rows_to_skip} rows')
            try:
                # Attempt to load the data as pandas DataFrame
                dataframe = pd.read_csv(data['path'], encoding="ISO-8859-1", skiprows=int(n_rows_to_skip), sep=delimiter)
            except:
                print(f'I could not make pandas DafaFrame. I just cut your data by {n_rows_to_skip} rows')
                dataframe = data['data'].split('\n',int(preload["skip_rows_number"]))[-1]
                self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(data['data'].split('\n', int(preload["skip_rows_number"]))[-1]))

        elif preload["find_header"] == True:
            phrase = preload["find_header_phrase"]
            print(f'Looking for the phrase "{phrase}" included in header')

            # Try to find and split the data based on the phrase
            if phrase in data['data']:
                data_from_header = phrase + '\n'.join(data['data'].split(phrase)[1:])
                try:
                    dataframe = pd.read_csv(StringIO(data_from_header), encoding="ISO-8859-1", sep=delimiter)
                except:
                    print('Could not make pandas DataFrame')
                    dataframe = data['data']
            else:
                print(f"Phrase {phrase} not found :(")
                dataframe = data['data']

        elif preload["defined_in"] == True:
            defined_in_row = preload["defined_in_row"]
            defined_in_column = preload["defined_in_column"]

        else:
            print('ELSE!')
            dataframe = pd.read_csv(data['path'], encoding="ISO-8859-1", delim_whitespace=True)
            # dataframe = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']})

        if preload["add_header"] == True:
            new_header = preload["add_header_text"]
            print(f"Adding header to the file: {new_header}")

        self.check_panda(dataframe)
        print(dataframe.columns)
        return dataframe

    def handle_filelist_item_selection(self):
        selected_index = self.filelist_listWidget.currentRow()
        selected_data = self.current_project["list_data"][selected_index]
        self.preview_textBrowser.setText(self.df_to_text_or_add_line_numbers(selected_data['data']))
        self.filePath_textBrowser.setText(selected_data['path'])
        self.fileSize_textBrowser.setText(self.get_size(selected_data['data']))
        self.check_panda(selected_data['data'])
        self.update_variables_list(self.current_project["list_data"][selected_index]['data'])

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

    def update_plot_combo_boxes(self):
        selected_index = self.filelist_listWidget.currentRow()
        selected_data = self.current_project["list_data"][selected_index]['data']
        variables_list = selected_data.columns.tolist()
        list_combo_boxes = [self.X2DXY_comboBox, self.Y2DXY_comboBox, self.X2DXYZ_comboBox, self.Y2DXYZ_comboBox, self.Z2DXYZ_comboBox, self.X3D_comboBox, self.Y3D_comboBox, self.Z3D_comboBox]
        for combo_box in list_combo_boxes:
            combo_box.clear()
            for variable in variables_list:
                combo_box.addItem(variable)

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
        selected_index = self.filelist_listWidget.currentRow()
        selected_item = self.filelist_listWidget.currentItem()
        if selected_item:
            self.filelist_listWidget.takeItem(self.filelist_listWidget.row(selected_item))
            del self.current_project["list_data"][selected_index]

    def clear_marked_fileList(self):
        items_indexes_to_remove = []
        for index in range(self.filelist_listWidget.count()):
            item = self.filelist_listWidget.item(index)
            current_state = item.checkState()
            if current_state == QtCore.Qt.Checked:
                items_indexes_to_remove.append(index)
            item.setCheckState(QtCore.Qt.Unchecked)
        for index in items_indexes_to_remove:
            self.filelist_listWidget.takeItem(index)

    def clear_all_fileList(self):
        self.current_project['list_data'] = []
        self.filelist_listWidget.clear()
        print(self.current_project['list_data'])

    def get_size(self, sth):
        # Calculate size of self.current_data (from path), or pandas DataFrame or plain string.
        def format_bytes(size_bytes):
            # Define suffixes for different sizes
            suffixes = ['B', 'kB', 'MB', 'GB', 'TB']
            suffix_index = 0
            while size_bytes >= 1024 and suffix_index < len(suffixes) - 1:
                size_bytes /= 1024
                suffix_index += 1
            # Return the size with the appropriate suffix
            return "{:.2f} {}".format(size_bytes, suffixes[suffix_index])

        if isinstance(sth, dict):
            print(sth['path'])
            sth_size = os.path.getsize(sth['path'])
        elif isinstance(sth, pd.DataFrame):
            sth_size = sth.memory_usage(deep=True).sum()
        elif isinstance(sth, str):
            sth_size = sys.getsizeof(sth)
        else:
            print('Some wrong format in get_size() function')
            sth_size = 0

        return format_bytes(sth_size)

    def df_to_text_or_add_line_numbers(self, text):
        # Checks if data is already pandas dataframe
        if self.check_panda(text):
            text = text.head(100).to_csv(index=True, header=True, sep='\t', index_label=False)
            #numbered_lines
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
        formatted_text = f'<span style="color: blue;"><b>{current_datetime}</b></span> {text}'
        self.terminal_textBrowser.append(formatted_text)

    def handle_checkboxes_for_import_options(self, state):
        checkboxes = [self.skipNRows_checkBox, self.definedIn_checkBox, self.findHeader_checkBox]
        if state == 2:  # If the checkbox is checked
            sender = self.sender()
            for checkbox in checkboxes:
                 checkbox.setChecked(checkbox is sender)

    def check_panda(self, text):
        if isinstance(text, pd.DataFrame):
            if text.columns[0].isnumeric():
                self.print_to_terminal('Your dataframe needs header. Use "add header" option.')
                pixmap = QtGui.QPixmap("icons/panda_headless.png")
            else:
                self.print_to_terminal("All good, panda is happy!")
                pixmap = QtGui.QPixmap("icons/panda.png")
            self.panda_label.setPixmap(pixmap)
            self.panda_label.setScaledContents(True)
            return True
        else:
            self.panda_label.clear()
            return False

    def plot_selected_2D_XY(self):
        selected_index = self.filelist_listWidget.currentRow()
        selected_data = self.current_project["list_data"][selected_index]
        x = self.X2DXY_comboBox.currentText()
        y = self.Y2DXY_comboBox.currentText()
        try:
            plt.plot(selected_data['data'][x], selected_data['data'][y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(selected_data['name'])
            plt.grid(True)
            plt.show()
        except:
            self.print_to_terminal('Something is wrong with the format of your variables :(')

    def plot_marked_2D_XY(self):
        data_to_plot = []
        x = self.X2DXY_comboBox.currentText()
        y = self.Y2DXY_comboBox.currentText()
        try:
            for index in range(self.filelist_listWidget.count()):
                item = self.filelist_listWidget.item(index)
                current_state = item.checkState()
                if current_state == QtCore.Qt.Checked:
                    data_to_plot.append(index)
            for index in data_to_plot:
                data = self.current_project["list_data"][index]
                plt.plot(data['data'][x], data['data'][y], label=data['name'])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend()
            # plt.title(data['name'])
            plt.grid(True)
            plt.show()
        except:
            self.print_to_terminal('Something is wrong with the format of your variables :(')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
