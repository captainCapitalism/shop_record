"""
This module contains Order class and it's methods
"""
import tkinter as tk
from wui.record.record_scripts.item_class import Item
from language.language import *
import values.constants as const


class Order(tk.Frame):
    """
    This class is container of widgets representing order variables
    """

    def __init__(self, master, database_container, order_id=0):
        self.databases = database_container
        super().__init__(master=master.container_widgets["orders_container"])
        # create "borders" of frame
        self.configure(highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
        self.scrolling_canvas = master.container_widgets["order_canvas"]
        self.items = []
        self.language = get_language_id('pl')
        self.variables = {}
        self.widgets = {}
        if order_id == 0:
            self.databases.orders.create_empty_order()
            self.id_order = self.databases.orders.cursor.lastrowid
            self.create_ui()

        else:
            self.id_order = order_id
            self.set_order_values()

    def create_ui(self):
        """
        This method creates the interface of an order
        :return:
        """
        self.create_widgets()
        self.create_labels()
        self.create_sum()

        for x in range(const.ORDER_DEFAULT_ITEM_COUNT):
            self.create_item()

    def set_order_values(self):
        self.create_widgets()
        self.create_labels()
        self.create_sum()
        values = self.databases.orders.get_order_values_from_id(self.id_order)
        ordered_items = self.databases.items.select_all_items_from_order(self.id_order)
        self.variables["discount_text"].set(values["discount"])
        self.variables["table_text"].set(values["orderTable"])
        self.variables["bulk_discount"].set(values["discountForSale"])
        x = 0
        for item in ordered_items:
            item_data = self.databases.menu.select_by_id(item["positionID"])
            self.create_item(item["itemID"])
            self.items[x].widget_container["type_entry"].var.set(item["type"])
            self.items[x].variable_container["count_text"]
            self.items[x].widget_container["name_entry"].var.set(
                self.databases.menu.select_by_id(item["positionID"])["positionName"])
            self.items[x].widget_container["type_entry"].lb.destroy()
            self.items[x].widget_container["type_entry"].lb_up = False

            self.items[x].widget_container["name_entry"].lb.destroy()
            self.items[x].widget_container["name_entry"].lb_up = False

            self.items[x].name_change()
            x += 1

    def create_labels(self):
        """
        This method is responsible for creating labels for future widgets
        and positioning them on grid
        :return:
        """
        self.widgets.update({
            "code_label": tk.Label(master=self,
                                   text=const.ORDER_WIDGET_CONFIG_VALUES["CODE_LABEL"]["text"]),
            "name_label": tk.Label(master=self,
                                   text=const.ORDER_WIDGET_CONFIG_VALUES["NAME_LABEL"]["text"]),
            "type_label": tk.Label(master=self,
                                   text=const.ORDER_WIDGET_CONFIG_VALUES["TYPE_LABEL"]["text"]),
            "count_label": tk.Label(master=self,
                                    text=const.ORDER_WIDGET_CONFIG_VALUES["COUNT_LABEL"]["text"]),
            "def_price_label": tk.Label(master=self,
                                        text=const.ORDER_WIDGET_CONFIG_VALUES["DEF_PRICE_LABEL"]["text"]),
            "price_label": tk.Label(master=self,
                                    text=const.ORDER_WIDGET_CONFIG_VALUES["PRICE_LABEL"]["text"]),
            "disc_price_label": tk.Label(master=self,
                                         text=const.ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE_LABEL"]["text"]),
            "hint_label": tk.Label(master=self,
                                   text=const.ORDER_WIDGET_CONFIG_VALUES["HINT_LABEL"]["text"])
        })

        self.widgets["code_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["CODE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["CODE_LABEL"]["column"])
        self.widgets["name_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["NAME_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["NAME_LABEL"]["column"])
        self.widgets["type_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["TYPE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["TYPE_LABEL"]["column"])
        self.widgets["count_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["COUNT_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["COUNT_LABEL"]["column"])
        self.widgets["def_price_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DEF_PRICE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DEF_PRICE_LABEL"]["column"])
        self.widgets["price_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["PRICE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["PRICE_LABEL"]["column"])
        self.widgets["disc_price_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE_LABEL"]["column"])
        self.widgets["hint_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["HINT_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["HINT_LABEL"]["column"])

    def create_widgets(self):
        """

        :return:
        """
        self.create_labels()

        self.variables.update({
            "table_text": tk.StringVar(),
            "discount_text": tk.IntVar(),
            "bulk_discount": tk.BooleanVar()
        })
        self.widgets.update({
            "delete_button": tk.Button(
                master=self,
                command=lambda: self.delete_order(),
                text=const.ORDER_WIDGET_CONFIG_VALUES["DELETE_BUTTON"]["text"],
                width=const.ORDER_WIDGET_CONFIG_VALUES["DELETE_BUTTON"]["width"],
                height=const.ORDER_WIDGET_CONFIG_VALUES["DELETE_BUTTON"]["height"]),
            "transfer_button": tk.Button(
                master=self,
                command=lambda: self.complete_order(),
                text=const.ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BUTTON"]["text"],
                width=const.ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BUTTON"]["width"],
                height=const.ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BUTTON"]["height"]
            ),
            "table_label": tk.Label(
                master=self,
                text=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_LABEL"]["text"]),
            "table_entry": tk.Entry(
                master=self,
                textvariable=self.variables["table_text"],
                width=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_ENTRY"]["width"]),
            "discount_label": tk.Label(
                master=self,
                text=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_LABEL"]["text"]),
            "discount_entry": tk.Entry(
                master=self,
                width=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_ENTRY"]["width"],
                textvariable=self.variables["discount_text"]),
            "bulk_discount_entry": tk.Checkbutton(
                master=self,
                text=const.ORDER_WIDGET_CONFIG_VALUES["BULK_DISCOUNT_BUTTON"]["text"],
                variable=self.variables["bulk_discount"]),
            "add_item_button": tk.Button(
                master=self,
                text=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["text"],
                width=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["width"],
                height=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["height"],
                command=lambda: self.create_item())
        })
        self.variables["discount_text"].trace('w', self.discount_change)
        self.variables["bulk_discount"].trace('w', self.discount_change)

        self.widgets["delete_button"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DELETE_BUTTON"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DELETE_BUTTON"]["column"])
        self.widgets["transfer_button"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BUTTON"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BUTTON"]["column"])
        self.widgets["table_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_LABEL"]["column"])
        self.widgets["discount_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_LABEL"]["column"])
        self.widgets["discount_entry"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_ENTRY"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DISCOUNT_ENTRY"]["column"])
        self.widgets["table_entry"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_ENTRY"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["TABLE_ENTRY"]["column"])
        self.widgets["bulk_discount_entry"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["BULK_DISCOUNT_BUTTON"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["BULK_DISCOUNT_BUTTON"]["column"],
            columnspan=const.ORDER_WIDGET_CONFIG_VALUES["BULK_DISCOUNT_BUTTON"]["columnspan"])
        self.widgets["add_item_button"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["column"],
            sticky=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["sticky"],
            rowspan=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["rowspan"],
            padx=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["padx"],
            pady=const.ORDER_WIDGET_CONFIG_VALUES["ADD_ITEM_BUTTON"]["pady"])

    def create_item(self, item_id=0):
        """

        :return:
        """
        self.items += [Item(self, len(self.items) +
                            const.ORDER_ITEM_STARTING_ROW, self.databases, item_id)]

        sums_row = self.widgets["sum_label"].grid_info()['row']
        self.widgets["sum_label"].grid(row=1 + sums_row)
        self.widgets["sum_entry"].grid(row=1 + sums_row)
        self.widgets["disc_sum_label"].grid(row=1 + sums_row)
        self.widgets["disc_sum_entry"].grid(row=1 + sums_row)
        self.master.update_idletasks()
        self.scrolling_canvas.config(scrollregion=self.scrolling_canvas.bbox("all"))

    def create_sum(self):
        """

        :return:
        """
        self.variables["sum_text"] = tk.DoubleVar()
        self.variables["disc_sum_text"] = tk.DoubleVar()

        self.widgets.update({
            "sum_label": tk.Label(master=self,
                                  text=const.ORDER_WIDGET_CONFIG_VALUES["SUM_LABEL"]["text"]),
            "sum_entry": tk.Entry(master=self,
                                  width=const.ORDER_WIDGET_CONFIG_VALUES["SUM_ENTRY"]["width"],
                                  textvariable=self.variables["sum_text"]),
            "disc_sum_label": tk.Label(master=self,
                                       text=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_LABEL"]["text"]),
            "disc_sum_entry": tk.Entry(master=self,
                                       width=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_ENTRY"]["width"],
                                       textvariable=self.variables["disc_sum_text"])
        })

        self.widgets["sum_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["SUM_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["SUM_LABEL"]["column"])
        self.widgets["sum_entry"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["SUM_ENTRY"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["SUM_ENTRY"]["column"])
        self.widgets["disc_sum_label"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_LABEL"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_LABEL"]["column"])
        self.widgets["disc_sum_entry"].grid(
            row=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_ENTRY"]["row"],
            column=const.ORDER_WIDGET_CONFIG_VALUES["DISC_SUM_ENTRY"]["column"])

    def discount_change(self, name, index, mode):
        """

        :param name:
        :param index:
        :param mode:
        :return:
        """
        discount_column = self.databases.orders.column_names[3]
        bulk_discount_column = self.databases.orders.column_names[4]

        self.databases.orders.update_order_value(
            self.id_order,
            discount_column,
            self.variables["discount_text"].get()
        )
        self.databases.orders.update_order_value(
            self.id_order,
            bulk_discount_column,
            self.variables["bulk_discount"].get()
        )

        for item in self.items:
            if item.item_id != 0:
                item.set_discounted_price()

    def set_prices(self):
        [price, discounted_price] = self.databases.orders.calculate_sum(
            self.id_order,
            self.databases.items,
            self.databases.menu
        )

        self.variables["sum_text"].set(price)
        self.variables["disc_sum_text"].set(discounted_price)

    def delete_order(self):
        self.databases.orders.delete_order(
            self.id_order,
            self.databases.items
        )
        self.destroy()

    def complete_order(self):
        if self.variables["disc_sum_text"].get() != 0:
            self.databases.orders.update_order_value(
                self.id_order, self.databases.orders.column_names[1], 1
            )
            self.destroy()
