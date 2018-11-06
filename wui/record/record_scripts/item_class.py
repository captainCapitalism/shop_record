import tkinter as tk
import values.constants as const
from wui.record.record_scripts.autocomplete_name_class import AutocompleteName
from wui.record.record_scripts.autocomplete_type_class import AutocompleteType


# TODO CLOSE LISTBOXES WHEN CLICKED SOMEWHERE
class Item:

    def __init__(self, master, row, database_container, item_id=0):
        self.database_container = database_container
        self.item_id = item_id
        self.variable_container = {}
        self.widget_container = {}
        self.master = master
        self.row = row
        self.create_entries()

    def create_entries(self):
        self.variable_container.update({
            "code_text": tk.StringVar(),
            "count_text": tk.DoubleVar(),
            "def_price_text": tk.DoubleVar(),
            "price_text": tk.DoubleVar(),
            "hint_text": tk.StringVar(),
            "disc_price_text": tk.DoubleVar()
        })

        self.widget_container.update({
            "code_entry": tk.Entry(
                master=self.master,
                width=const.ITEM_WIDGET_CONFIG_VALUES["CODE_ENTRY"]["width"],
                textvariable=self.variable_container["code_text"]),
            "name_entry": AutocompleteName(
                master=self.master, item=self,
                database_container=self.database_container,
                column=const.ITEM_WIDGET_CONFIG_VALUES["NAME_ENTRY"]["column"],
                width=const.ITEM_WIDGET_CONFIG_VALUES["NAME_ENTRY"]["width"]),
            "type_entry": AutocompleteType(
                master=self.master, item=self,
                column=const.ITEM_WIDGET_CONFIG_VALUES["TYPE_ENTRY"]["column"],
                width=const.ITEM_WIDGET_CONFIG_VALUES["TYPE_ENTRY"]["width"]),
            "count_entry": tk.Entry(
                master=self.master, width=const.ITEM_WIDGET_CONFIG_VALUES["COUNT_ENTRY"]["width"],
                textvariable=self.variable_container["count_text"]),
            "def_price_entry": tk.Entry(
                master=self.master, width=const.ITEM_WIDGET_CONFIG_VALUES["DEF_PRICE_ENTRY"]["width"],
                textvariable=self.variable_container["def_price_text"]),
            "price_entry": tk.Entry(
                master=self.master, width=const.ITEM_WIDGET_CONFIG_VALUES["PRICE_ENTRY"]["width"],
                textvariable=self.variable_container["price_text"]),
            "disc_price_entry": tk.Entry(
                master=self.master, width=const.ITEM_WIDGET_CONFIG_VALUES["DISC_PRICE_ENTRY"]["width"],
                textvariable=self.variable_container["disc_price_text"]),
            "hint_entry": tk.Entry(
                master=self.master, width=const.ITEM_WIDGET_CONFIG_VALUES["HINT_ENTRY"]["width"],
                textvariable=self.variable_container["hint_text"])
        })

        self.widget_container["code_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["CODE_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["CODE_ENTRY"]["padx"])
        self.widget_container["name_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["NAME_ENTRY"]["column"],
            columnspan=const.ITEM_WIDGET_CONFIG_VALUES["NAME_ENTRY"]["columnspan"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["NAME_ENTRY"]["padx"])
        self.widget_container["type_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["TYPE_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["TYPE_ENTRY"]["padx"])
        self.widget_container["count_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["COUNT_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["COUNT_ENTRY"]["padx"])
        self.widget_container["def_price_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["DEF_PRICE_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["DEF_PRICE_ENTRY"]["padx"])
        self.widget_container["price_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["PRICE_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["PRICE_ENTRY"]["padx"])
        self.widget_container["disc_price_entry"].grid(
            row=self.row,
            column=const.ITEM_WIDGET_CONFIG_VALUES["DISC_PRICE_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["DISC_PRICE_ENTRY"]["padx"])
        self.widget_container["hint_entry"].grid(
            row=self.row, column=const.ITEM_WIDGET_CONFIG_VALUES["HINT_ENTRY"]["column"],
            padx=const.ITEM_WIDGET_CONFIG_VALUES["HINT_ENTRY"]["padx"])
        # TODO CHANGE TRACING?
        self.variable_container["def_price_text"].trace('w', self.def_price_change)
        self.variable_container["disc_price_text"].trace('w', self.discounted_price_change)
        self.variable_container["count_text"].trace('w', self.count_change)

        for value in self.widget_container.values():
            value.bind('<Control-KeyRelease-a>', self.select_all_in_entry)

        self.master.update()

        if self.item_id != 0:
            self.name_change

    def click(self):
        print("CHUJ")

    def name_change(self):
        """
        This method determines whether
        item should be inserted or edited
        :return:
        """
        if self.item_id == 0:
            self.initialize_item_in_database()
        else:
            self.update_item_in_database()

    def initialize_item_in_database(self):
        """
        This method initializes item in database
        for a first time and invokes methods used to
        write values necessary for user to work
        :return:
        """
        position_dictionary = self.database_container.menu.select_by_name(
            self.widget_container["name_entry"].var.get())
        position_id = position_dictionary["positionID"]
        item_type = self.widget_container["type_entry"].var.get()
        if item_type == "":
            self.widget_container["type_entry"].var.set("sztuka")
            self.widget_container["type_entry"].lb.destroy()
            self.widget_container["type_entry"].lb_up = False

            item_type = self.widget_container["type_entry"].var.get()

        self.database_container.items.insert_item_into_database(
            self.master.id_order, position_id,
            self.variable_container["count_text"].get(), item_type)

        self.item_id = self.database_container.items.cursor.lastrowid
        self.set_values_from_database(position_dictionary)

    def update_item_in_database(self):
        """
        This method updates values in case of change of name
        :return:
        """
        new_name = self.widget_container["name_entry"].var.get()
        if new_name == "":
            self.remove_item_from_database()

        else:
            result = self.database_container.menu.select_by_name(new_name)
            self.database_container.items.update_ordered_item_value(
                self.item_id, self.database_container.items.column_names[2],
                result["positionID"])
            self.set_values_from_database(result)

    def remove_item_from_database(self):
        """
        This method removes ordered item from record
        :return:
        """
        self.database_container.items.delete_item(self.item_id)
        self.item_id = 0
        self.variable_container["code_text"].set("")
        self.variable_container["price_text"].set("")
        self.variable_container["disc_price_text"].set("")
        self.variable_container["def_price_text"].set("")

    def set_values_from_database(self, position_dictionary):
        """
        This method initializes values needed for user to
        compute ordered item
        :param position_dictionary:
        :return:
        """
        if self.variable_container["count_text"].get() == 0:
            self.variable_container["count_text"].set(1)

        self.variable_container["code_text"].set(position_dictionary["positionCode"])

        self.set_default_price()

    def select_all_in_entry(self, event):
        """
        This method selects string in entry
        for easier edition
        :param event:
        :return:
        """
        # select text
        event.widget.select_range(0, tk.END)
        # move cursor to the end
        event.widget.icursor(tk.END)

    def set_default_price(self):
        """
        This method connects to databases
        and calculates default price for item
        for given id and type
        later invokes methods for
        setting price
        and setting discoutned price
        :return:
        """
        order_values = self.database_container.orders.get_order_values_from_id(self.master.id_order)
        item_values = self.database_container.items.select_item_from_order(self.item_id)
        self.variable_container["def_price_text"].set(
            self.database_container.menu.select_position_price(
                item_values["positionID"],
                item_values["type"],
                order_values["discount"],
                order_values["discountForSale"]
            )[0]
        )

        self.set_price()
        self.set_discounted_price()

    def set_price(self):
        """
        This method calculates price
        based on default price and
        number of items ordered
        :return:
        """
        self.variable_container["price_text"].set(
            self.variable_container["def_price_text"].get() * self.variable_container["count_text"].get()
        )

    def set_discounted_price(self):
        """
        This method calculates discounted price
        based on values in order
        :return:
        """
        order_values = self.database_container.orders.get_order_values_from_id(self.master.id_order)
        item_values = self.database_container.items.select_item_from_order(self.item_id)
        self.variable_container["disc_price_text"].set(
            item_values["count"] *
            self.database_container.menu.select_position_price(
                item_values["positionID"],
                item_values["type"],
                order_values["discount"],
                order_values["discountForSale"]
            )[1]
        )

    def count_change(self, name, index, mode):
        """
        This method recalculates prices when count is changed by user
        :param name:
        :param index:
        :param mode:
        :return:
        """
        count = self.variable_container["count_text"].get()
        count_column_name = self.database_container.items.column_names[3]

        self.database_container.items.update_ordered_item_value(
            self.item_id, count_column_name, count)
        self.set_price()
        self.set_discounted_price()

    def def_price_change(self, name, index, mode):
        """
        This event is recalculating prices when event of changing default price occurs
        :param name:
        :param index:
        :param mode:
        :return:
        """
        self.set_price()
        self.set_discounted_price()

    def type_change(self):
        """
        This method is invoked when a user changes type of ordered item
        :return:
        """
        new_type = self.widget_container["type_entry"].var.get()
        type_column_name = self.database_container.items.column_names[4]
        self.database_container.items.update_ordered_item_value(
            self.item_id, type_column_name, new_type)
        self.set_default_price()

    def discounted_price_change(self, name, index, mode):
        """
        This method invokes calculating prices on event of changing discounted price
        :param name:
        :param index:
        :param mode:
        :return:
        """
        self.master.set_prices()
