import tkinter as tk
import values.constants as const


class ArchivedItem:
    def __init__(self, master, row, item_id, order_data, database_container):
        self.databases = database_container
        self.widgets = {}
        self.master = master
        self.row = row
        self.item_id = item_id
        self.order_data = order_data
        self.variables = {}
        self.menu_position_variables = {}
        self.get_item_data()
        self.create_product_entries()

    def get_item_data(self):
        self.variables = self.databases.items.select_item_from_order(
            self.item_id)
        self.menu_position_variables = self.databases.menu.select_by_id(self.variables["positionID"])

    def create_product_entries(self):
        item_price = self.databases.menu.select_position_price(self.variables["positionID"],
                                                               self.variables["type"], self.order_data["discount"],
                                                               self.order_data["discountForSale"])[1]
        self.widgets.update({
            "name": tk.Label(
                master=self.master,
                text=self.menu_position_variables["positionName"],
                width=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["width"],
                anchor=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["anchor"]),
            "type": tk.Label(
                master=self.master, text=self.variables["type"],
                width=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["width"],
                anchor=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["anchor"]),
            "count": tk.Label(
                master=self.master, text=self.variables["count"],
                width=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["width"],
                anchor=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["anchor"]),
            "price": tk.Label(
                master=self.master, text=item_price,
                width=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["width"],
                anchor=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["anchor"])
            # TODO PRICE GREAT AGAIN
        })

        self.widgets["name"].grid(
            row=self.row,
            column=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["column"],
            padx=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["padx"],
            pady=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["pady"],
            sticky=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["NAME"]["sticky"])
        self.widgets["type"].grid(
            row=self.row,
            column=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["column"],
            padx=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["padx"],
            pady=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["pady"],
            sticky=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["TYPE"]["sticky"])
        self.widgets["count"].grid(
            row=self.row,
            column=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["column"],
            padx=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["padx"],
            pady=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["pady"],
            sticky=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["COUNT"]["sticky"])
        self.widgets["price"].grid(
            row=self.row,
            column=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["column"],
            padx=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["padx"],
            pady=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["pady"],
            sticky=const.ARCHIVED_ITEM_WIDGET_CONFIG_VALUES["PRICE"]["sticky"])
