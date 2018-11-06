import tkinter as tk
import re
from values.constants import type_list


class AutocompleteType(tk.Entry):

    def __init__(self, master, item, column, width):
        self.master = master
        self.item = item
        self.row = item.row
        self.column = column
        self.width = width
        tk.Entry.__init__(self, self.master, width=width)
        self.selection_list = type_list
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = tk.StringVar()

        self.var.trace('w', self.changed)
        self.bind_control_buttons()
        self.lb_up = False

    def bind_control_buttons(self):
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.bind("<Return>", self.selection)
        self.bind("<Escape>", self.exit)
        self.bind("<Button-1>", self.show_all)

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = tk.Listbox(self.master, height=4, width=self.width)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Return>", self.selection)
                    self.lb.grid(row=self.row, column=self.column + 1, columnspan=4, rowspan=4, padx=1, sticky='W')
                    self.lb_up = True

                self.lb.delete(0, tk.END)
                for w in words:
                    self.lb.insert(tk.END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(tk.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)
            self.item.type_change()

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != tk.END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*', re.I)
        return [w for w in self.selection_list if re.match(pattern, w)]

    def show_all(self, event):
        if not self.lb_up:
            self.lb = tk.Listbox(self.master, height=5, width=self.width)
            self.lb.bind("<Double-Button-1>", self.selection)
            self.lb.bind("<Return>", self.selection)
            self.lb.grid(row=self.row, column=self.column + 1, columnspan=4, rowspan=4, padx=1, sticky='W')
            self.lb_up = True

        self.lb.delete(0, tk.END)
        for w in type_list[1:]:
            self.lb.insert(tk.END, w)

    def exit(self, event):
        if self.lb_up:
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)
