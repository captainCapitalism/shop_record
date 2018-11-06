import tkinter as tk


def callback(event):
    # select text after 50ms
    root.after(10, select_all, event.widget)


def select_all(widget):
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')


root = tk.Tk()
x = tk.StringVar
e = tk.Entry(root, textvariable=x)
e.pack()
e.bind('<Control-a>', callback)

root.mainloop()
