import tkinter as tk

root = tk.Tk()
text = tk.Text(master=root, height=1, width=30, undo=True)
text.grid(row=0, column=0)
root.mainloop()
