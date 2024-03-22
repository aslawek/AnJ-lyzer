import tkinter as tk
from styles.styles import font, font_size

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
        for path in paths:
            data.add_data(id=id(path), filename=path.replace('/', ' ').split()[-1], path=path, active=True)
        self.updateEntries()

    def updateEntries(self):
        # Clears all items in list and then creates the list one more time :)
        for widget in self.frame.winfo_children():
            widget.destroy()
        for index, item in enumerate(data.list):
            def on_check():
                pass # here needs to be a function that will localise THE checkbox and change its variable
            item['id'] = tk.BooleanVar(value=item['active'])
            tk.Checkbutton(self.frame, onvalue=True, offvalue=False, variable=item['id'], command=on_check)\
                .grid(row=index + 1, column=0, columnspan=1)
            tk.Label(self.frame, text=item['path'].replace('/', ' ').split()[-1])\
                .grid(row=index + 1, column=1, columnspan=1)
            tk.Button(self.frame, text='X', command=lambda idx=index: self.removeEntry(idx))\
                .grid(row=index + 1, column=2, columnspan=1)
        self.frame.grid()

    def removeEntry(self, index):
        del data.list[index]
        self.updateEntries()