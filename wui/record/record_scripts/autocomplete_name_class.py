import tkinter as tk


class AutocompleteName(tk.Entry):

    def __init__(self, master, item, database_container, column, width):
        self.master = master
        self.item = item
        self.row = item.row
        self.column = column
        self.width = width
        self.database_container = database_container

        tk.Entry.__init__(self, self.master, width=width)
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

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
            self.item.remove_item_from_database()
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = tk.Listbox(self.master, height=6, width=self.width)
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
            #            self.master.items[self.row - 2].set_default_price()
            self.item.name_change()

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
        found = self.database_container.menu.search_for_position(self.var.get())
        return found

    def exit(self, event):
        if self.lb_up:
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)
