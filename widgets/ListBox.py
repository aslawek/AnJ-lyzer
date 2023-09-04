import tkinter as tk
from styles.styles import font, font_size

class Listbox(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)
        tk.Label(self, text = 'List of files:', anchor='w', font=(font, font_size)).grid(row=0, column=0)
        tk.Text(self).grid(row=1, column=0)

        self.pack()