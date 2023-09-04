import tkinter as tk
import tkinter.filedialog
import pandas as pd
import sys
from styles.styles import font, font_size
#from widgets.ListBox import Listbox

class Data:
    def __init__(self):
        self.paths = []
        self.dataframe = pd.DataFrame()
        self.active = []
    def add_paths(self, paths):
        self.paths = self.paths + paths
    def rm_data(self, path):
        self.paths.remove(path)
    def show_data(self):
        for path in self.paths:
            print(path)

global data
data = Data()
data.add_paths(['./data_examples/SRDP_1ms.mpt',
                './data_examples/SRDP_2ms.mpt',
                './data_examples/SRDP_3ms.mpt',
                './data_examples/SRDP_4ms.mpt',
                './data_examples/SRDP_5ms.mpt',
                './data_examples/SRDP_6ms.mpt'
                ])

class Listbox(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        # grid layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        tk.Label(self, text='List of files:', anchor='w', font=(font, font_size)).grid(row=0, column=0)
        tk.Button(self, text='Browse file:', command=self.browseFiles, font=(font, font_size)).grid(row=0, column=1)
        self.frame = tk.Frame(self, height=15, background='yellow')
        self.frame.rowconfigure((0, 1), weight=1)
        self.frame.columnconfigure((0, 1, 2), weight=1)
        self.updateEntries()
        self.pack()

    def browseFiles(self):
        # Function to browse files (Windows explorer) to a tuple (1, 2, 3...)
        paths = tkinter.filedialog.askopenfilenames(initialdir="./", title="Select a File", filetypes=((".mpt files", "*.mpt*"), ("All files", "*.*")))
        data.add_paths(list(paths))
        self.updateEntries()

    def updateEntries(self):
        # Clears all items in list and then creates the list one more time :)
        for widget in self.frame.winfo_children():
            widget.destroy()
        for index, path in enumerate(data.paths):
            tk.Checkbutton(self.frame)\
                .grid(row=index + 1, column=0, columnspan=1)
            tk.Label(self.frame, text=path.replace('/', ' ').split()[-1])\
                .grid(row=index + 1, column=1, columnspan=1)
            tk.Button(self.frame, text='X', command=lambda idx=index: self.removeEntry(idx))\
                .grid(row=index + 1, column=2, columnspan=1)
        self.frame.grid()

    def removeEntry(self, index):
        del data.paths[index]
        self.updateEntries()

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        def quit():
            sys.exit(0)

# root window
root = tk.Tk()
root.geometry("800x500")
root.title("AnJ-lizer")

# widgets
MenuBar(root)
Listbox(root)

root.config(menu=MenuBar)

# run
root.mainloop()