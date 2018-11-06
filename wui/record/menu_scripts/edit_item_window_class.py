import tkinter as tk

#TODO CLEAN UP HERE
class Edit(tk.Toplevel):
    def __init__(self, menu, menu_window, item_id=0):
        super().__init__()
        self.menu = menu
        self.item_id = item_id
        self.item_data = self.get_data_from_server()
        self.variables = {}
        self.widgets = {}
        self.menu_window = menu_window
        self.create_labels()
        self.create_widgets()
        self.create_buttons()

    def get_data_from_server(self):
        variables = self.menu.select_by_id(self.item_id)
        return variables

    def create_labels(self):
        self.widgets.update({
            "id_label": tk.Label(self, text="id", width=3),
            "name_label": tk.Label(self, text="nazwa", width=30),
            "code_label": tk.Label(self, text="kod", width=8),
            "price0_label": tk.Label(self, text="sztuka", width=8),
            "price1_label": tk.Label(self, text="gaiwan", width=8),
            "price2_label": tk.Label(self, text="opakowanie", width=8),
            "price3_label": tk.Label(self, text="na wagę", width=8)
        })
        self.widgets["id_label"].grid(row=0, column=0, pady=1)
        self.widgets["name_label"].grid(row=0, column=1, pady=1)
        self.widgets["code_label"].grid(row=0, column=2, pady=1)
        self.widgets["price0_label"].grid(row=0, column=3, pady=1)
        self.widgets["price1_label"].grid(row=0, column=4, pady=1)
        self.widgets["price2_label"].grid(row=0, column=5, pady=1)
        self.widgets["price3_label"].grid(row=0, column=6, pady=1)

    def create_widgets(self):
        self.variables = {
            "name": tk.StringVar(),
            "code": tk.StringVar(),
            "price0": tk.DoubleVar(),
            "price1": tk.DoubleVar(),
            "price2": tk.DoubleVar(),
            "price3": tk.DoubleVar()
        }
        if self.item_id != 0:
            self.variables["name"].set(self.item_data["positionName"])
            self.variables["code"].set(self.item_data["positionCode"])
            self.variables["price0"].set(self.item_data["priceDefault"])
            self.variables["price1"].set(self.item_data["priceGaiwan"])
            self.variables["price2"].set(self.item_data["pricePackage"])
            self.variables["price3"].set(self.item_data["priceBulk"])
            self.widgets.update({
                "id": tk.Label(self, text=self.item_data["positionID"], width=3)})
        else:
            self.widgets.update({"id": tk.Label(self, text=0, width=3)})

        self.widgets.update({
            "name": tk.Entry(self,
                             text=self.variables["name"], width=30),
            "code": tk.Entry(self,
                             text=self.variables["code"], width=8),
            "price0": tk.Entry(self,
                               text=self.variables["price0"], width=8),
            "price1": tk.Entry(self,
                               text=self.variables["price1"], width=8),
            "price2": tk.Entry(self,
                               text=self.variables["price2"], width=8),
            "price3": tk.Entry(self,
                               text=self.variables["price3"], width=8),
        })

        self.widgets["id"].grid(row=1, column=0, pady=1)
        self.widgets["name"].grid(row=1, column=1, pady=1)
        self.widgets["code"].grid(row=1, column=2, pady=1)
        self.widgets["price0"].grid(row=1, column=3, pady=1)
        self.widgets["price1"].grid(row=1, column=4, pady=1)
        self.widgets["price2"].grid(row=1, column=5, pady=1)
        self.widgets["price2"].grid(row=1, column=5, pady=1)
        self.widgets["price3"].grid(row=1, column=6, pady=1)

        self.update_idletasks()

    def create_buttons(self):
        self.widgets.update({"exit_button": tk.Button(self, text="odrzuć zmiany", command=lambda: self.destroy())})
        self.widgets.update(
            {"save_button": tk.Button(self, text="zapisz zmiany", command=lambda: self.save_changes())})
        self.widgets.update(
            {"delete_button": tk.Button(self, text="usuń pozycję", command=lambda: self.delete_entry())})

        self.widgets["exit_button"].grid(row=2, column=1)
        self.widgets["save_button"].grid(row=2, column=2, columnspan=2)
        self.widgets["delete_button"].grid(row=2, column=4, columnspan=2)

    def save_changes(self):
        if self.item_id != 0:
            new_values = [self.widgets["id"].cget("text"), self.variables["name"].get(),
                          self.variables["code"].get(), self.variables["price0"].get(),
                          self.variables["price1"].get(), self.variables["price2"].get(),
                          self.variables["price3"].get()]

            self.menu.update_entry(new_values)
            self.menu_window.refresh_window()
        else:
            new_values = [self.variables["name"].get(),
                          self.variables["code"].get(), self.variables["price0"].get(),
                          self.variables["price1"].get(), self.variables["price2"].get(),
                          self.variables["price3"].get()]
            self.menu.insert_into_menu(new_values)
            self.menu_window.destroy()
        self.destroy()

    def delete_entry(self):
        if self.item_id == 0:
            pass
        else:
            self.menu.delete_item(self.item_id)
            self.menu_window.destroy()
        self.destroy()
