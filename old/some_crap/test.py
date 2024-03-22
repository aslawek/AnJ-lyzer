import tkinter as tk
from tkinter import ttk


class MyWidget:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=1, sticky="nsew")  # Place in column 1, row 0 and expand to fill space

        # Create three labels with the same width
        self.label1 = ttk.Label(self.frame, text="Label 1")
        self.label2 = ttk.Label(self.frame, text="Label 2")
        self.label3 = ttk.Label(self.frame, text="Label 3")

        # Configure the labels to have the same width
        self.label1.grid(row=0, column=0, sticky="wens")
        self.label2.grid(row=0, column=1, sticky="wens")
        self.label3.grid(row=0, column=2, sticky="wens")

        # Make the labels expand to fill their respective rows
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)


# Create the main application window
root = tk.Tk()
root.geometry("800x500")
root.title("3 Labels in MyWidget")

# Create a 2x2 grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create an instance of MyWidget and place it in column 1, row 0
my_widget = MyWidget(root)

# Add more widgets to the grid if needed

# Start the tkinter main loop
root.mainloop()