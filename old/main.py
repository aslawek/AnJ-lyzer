import tkinter as tk
# from tkinter import ttk <- this will be used later for better styling :)
import tkinter.filedialog
from styles.styles import font, font_size


class DataList:
    def __init__(self):
        self.list = []
    def add_data(self, id, filename, path, active):
        self.list.append({
            'id': id,
            'filename': filename,
            'path': path,
            'active': active
        })
    def rm_data(self, path):
        self.list.remove(path)

global data_list
data = DataList()
data.add_data(id=0, filename='filename_1', path='xxx_xxx', active=True)
data.add_data(id=1, filename='filename_2', path='xxx_yyy', active=False)
data.add_data(id=2, filename='filename_3', path='xxx_zzz', active=True)

class MenuBar:
    def __init__(self, root):
        self.root = root
        self.menu_bar = tk.Menu(self.root)
        # Create a "File" menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Import Data", command=self.import_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)
        #file_menu.add_command(label="Quit", command=root.quit)
        # Create a "Help" menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        # Add the menus to the menu bar
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        # Configure the root window to use this menu bar
        self.root.config(menu=self.menu_bar)
    def import_data(self):
        # Function to browse files (Windows explorer) to a tuple (1, 2, 3...)
        paths = tkinter.filedialog.askopenfilenames(initialdir="./", title="Select a File", filetypes=((".mpt files", "*.mpt*"), ("All files", "*.*")))
        for path in paths:
            data.add_data(id=id(path), filename=path.replace('/', ' ').split()[-1], path=path, active=True)
        list_box.updateEntries()
    def show_about(self):
        # Display information about your application
        about_message = "This is an awesome AnJ-lyzer app by Andrzej Sławek."
        tk.messagebox.showinfo("About", about_message)

class Listbox:
    def __init__(self, root):
        #self.root = root
        # grid layout
        self.frame = tk.Frame(root, bg='green')
        self.frame.grid(row=0, column=1, sticky='wens')
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.label = tk.Label(self.frame, text='List of files:', font=(font, font_size))
        self.add_btn = tk.Button(self.frame, text='+', command=self.browseFiles, font=(font, font_size))
        self.entry_frame = tk.Frame(self.frame, bg='pink')
        self.label.grid(row=0, column=0, sticky='wens')
        self.add_btn.grid(row=0, column=2)
        self.entry_frame.grid(row=1, column=0)
        self.updateEntries()
    def browseFiles(self):
        # Function to browse files (Windows explorer) to a tuple (1, 2, 3...)
        paths = tkinter.filedialog.askopenfilenames(initialdir="./", title="Select a File", filetypes=((".mpt files", "*.mpt*"), ("All files", "*.*")))
        for path in paths:
            data.add_data(id=id(path), filename=path.replace('/', ' ').split()[-1], path=path, active=True)
        self.updateEntries()
    def updateEntries(self):
        # Clears all items in list and then creates the list one more time :)
        for widget in self.entry_frame.winfo_children():
            widget.destroy()
        for index, item in enumerate(data.list):
            def on_check():
                pass # here needs to be a function that will localise THE checkbox and change its variable
            item['id'] = tk.BooleanVar(value=item['active'])
            self.chck_btn = tk.Checkbutton(self.entry_frame, onvalue=True, offvalue=False, variable=item['id'], command=on_check)
            self.name_lbl = tk.Label(self.entry_frame, text=item['path'].replace('/', ' ').split()[-1])
            self.rm_btn = tk.Button(self.entry_frame, text='X', command=lambda idx=index: self.removeEntry(idx))
            self.chck_btn.grid(row=index + 2, column=0, columnspan=1)
            self.name_lbl.grid(row=index + 2, column=1, columnspan=1)
            self.rm_btn.grid(row=index + 2, column=2, columnspan=1)

    def removeEntry(self, index):
        del data.list[index]
        self.updateEntries()

# root window
root = tk.Tk()
root.geometry("800x500")
root.title("AnJ-lizer")
root.iconphoto(False, tk.PhotoImage(file='graphics/logo_AnJ.png'))
# frames to create grid layout
#root.columnconfigure((0, 1), weight=1)
root.rowconfigure((0, 1), weight=1)
root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(1, weight=1)
#root.grid_rowconfigure(0, weight=1)
#root.grid_rowconfigure(1, weight=1)
# right row
frame_info_box = tk.Frame(root, bg='pink')
frame_prev_box = tk.Frame(root, bg='yellow')
frame_info_box.grid(column=0, row=0, sticky='wens', padx=(5, 2.5), pady=(5, 2.5))
frame_prev_box.grid(column=0, row=1, sticky='wens', padx=(5, 2.5), pady=(2.5, 5))
# right row
frame_list_box = tk.Frame(root, bg='azure')
frame_plot_box = tk.Frame(root, bg='coral')
frame_list_box.grid(column=1, row=0, sticky='wn', padx=(2.5, 5), pady=(5, 2.5))
frame_plot_box.grid(column=1, row=1, sticky='wens', padx=(2.5, 5), pady=(2.5, 5))

# widgets
menu_bar = MenuBar(root)
list_box = Listbox(frame_list_box)

#root.config(menu=MenuBar)

# run
root.mainloop()

