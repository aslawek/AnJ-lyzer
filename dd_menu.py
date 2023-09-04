import tkinter as tk
#import styles/styles

# This is for top drop-down menu
root = tk.Tk()

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn_File = tk.Button(frame, text="File", font=15)
btn_Plot = tk.Button(frame, text="Plot", font=15)
btn_Help = tk.Button(frame, text="Help", font=15)

btn_File.grid(column=0, row=0, sticky=tk.W+tk.E)
btn_Plot.grid(column=1, row=0, sticky=tk.W+tk.E)
btn_Help.grid(column=2, row=0, sticky=tk.W+tk.E)

frame.pack(fill='x', padx=5, pady=5)

root.mainloop()