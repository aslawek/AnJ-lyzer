import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
s.configure('frame_info_box.TFrame', background='pink')
s.configure('frame_prev_box.TFrame', background='yellow')
s.configure('frame_info_box.TFrame', background='azure')
s.configure('frame_list_box.TFrame', background='coral')
s.configure('frame_plot_box.TFrame', background='pink')
s.configure('frame_list_box_2.TFrame', background='black')
s.configure('random_1.TFrame', background='blue')
s.configure('random_2.TFrame', background='magenta')
s.configure('random_3.TFrame', background='cyan')

# root window
root.geometry("800x500")
root.title("AnJ-lizer")

# widgets
#root.rowconfigure((0, 1), weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
# right row
frame_info_box = ttk.Frame(root, style='frame_info_box.TFrame')
frame_prev_box = ttk.Frame(root, style='frame_prev_box.TFrame')
frame_info_box.grid(column=0, row=0, sticky='wens', padx=(5, 2.5), pady=(5, 2.5))
frame_prev_box.grid(column=0, row=1, sticky='wens', padx=(5, 2.5), pady=(2.5, 5))
# right row
frame_list_box = ttk.Frame(root, style='frame_list_box.TFrame')
frame_plot_box = ttk.Frame(root, style='frame_plot_box.TFrame')
frame_list_box.grid(column=1, row=0, sticky='wens', padx=(2.5, 5), pady=(5, 2.5))
frame_plot_box.grid(column=1, row=1, sticky='wens', padx=(2.5, 5), pady=(2.5, 5))

frame_list_box.columnconfigure(0, weight=1)
frame_list_box.columnconfigure(1, weight=2)
frame_list_box.columnconfigure(2, weight=1)
frame_list_box.rowconfigure(0, weight=1)
frame_list_box_1 = ttk.Frame(frame_list_box, style='random_1.TFrame')
frame_list_box_2 = ttk.Frame(frame_list_box, style='random_2.TFrame')
frame_list_box_3 = ttk.Frame(frame_list_box, style='random_3.TFrame')
frame_list_box_1.grid(column=0, row=-0, sticky='wens')
frame_list_box_2.grid(column=1, row=-0, sticky='wens')
frame_list_box_3.grid(column=2, row=-0, sticky='wens')

label1 = tk.Label(frame_list_box_1, text='Label 1', padx=10, pady=10)
label2 = tk.Label(frame_list_box_2, text='Label 2', padx=5, pady=5)
label3 = tk.Label(frame_list_box_3, text='Label 3')
label1.grid(column=0, row=0, sticky='wens')
label2.grid(column=1, row=0, sticky='wens')
label3.grid(column=2, row=0, sticky='wens')

# run
root.mainloop()