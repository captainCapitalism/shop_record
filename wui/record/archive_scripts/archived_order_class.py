import tkinter as tk
from wui.record.archive_scripts.archived_item_class import ArchivedItem
import values.constants as const


# TODO SEND BACK TARGET ORDER

class ArchivedOrder(tk.Frame):
    def __init__(self, master, database_container, order_id):
        super().__init__(master=master)
        self.databases = database_container
        self.order_id = order_id
        self.labels = {}
        self.order_values = {}
        self.item_container = []
        self.widgets = {}
        self.create_labels()
        self.create_items()
        self.create_order_widgets()

    def create_labels(self):
        """
        This method is responsible for creating labels for future widgets
        and positioning them on grid
        :return:
        """
        self.labels.update({
            "name": tk.Label(
                master=self,
                text=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["text"],
                font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["font"],
                width=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["width"],
                anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["anchor"]),
            "type": tk.Label(
                master=self,
                text=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["text"],
                font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["font"],
                width=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["width"],
                anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["anchor"]),
            "count": tk.Label(
                master=self,
                text=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["text"],
                font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["font"],
                width=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["width"],
                anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["anchor"]),
            "disc_price": tk.Label(
                master=self,
                text=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["text"],
                font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["font"],
                width=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["width"],
                anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["anchor"])
        })

        self.labels["name"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["NAME"]["pady"])
        self.labels["type"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TYPE"]["pady"])
        self.labels["count"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["COUNT"]["pady"])
        self.labels["disc_price"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISC_PRICE"]["pady"])

    def create_items(self):
        self.widgets["item_frame"] = tk.Frame(master=self)
        self.widgets["item_frame"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["ITEM_FRAME"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["ITEM_FRAME"]["column"],
            columnspan=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["ITEM_FRAME"]["columnspan"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["ITEM_FRAME"]["sticky"])
        self.order_values = self.databases.orders.get_order_values_from_id(self.order_id)
        ordered_items_ids = self.databases.items.select_all_items_from_order(self.order_id)
        x = 0
        for item in ordered_items_ids:
            self.item_container += [ArchivedItem(master=self.widgets["item_frame"], row=x, item_id=item["itemID"],
                                                 order_data=self.order_values, database_container=self.databases)]
            x += 1

    def create_order_widgets(self):
        opening_var = const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["text"] + \
                      str(self.order_values["openingTime"])
        self.widgets["opening_time"] = tk.Label(
            master=self,
            text=opening_var,
            font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["font"],
            anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["anchor"])
        self.widgets["opening_time"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["OPENING_TIME"]["pady"])

        discount_var = const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["text"] + \
                       str(self.order_values["discount"]) + "%"
        self.widgets["discount"] = tk.Label(
            master=self,
            text=discount_var,
            font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["font"],
            anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["anchor"])
        self.widgets["discount"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["column"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["DISCOUNT"]["pady"])

        sum_var = const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["text"] + \
                  str(self.order_values["priceSum"])
        self.widgets["price_sum"] = tk.Label(
            master=self,
            text=sum_var,
            font=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["font"],
            anchor=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["anchor"])
        self.widgets["price_sum"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["column"],
            columnspan=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["columnspan"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["PRICE_SUM"]["pady"])

        self.widgets["transfer_back_button"] = tk.Button(
            master=self,
            text=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["text"],
            width=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["width"],
            command=lambda: self.revoke_from_archive())
        self.widgets["transfer_back_button"].grid(
            row=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["row"],
            column=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["column"],
            columnspan=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["columnspan"],
            padx=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["padx"],
            sticky=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["sticky"],
            pady=const.ARCHIVED_ORDER_WIDGET_CONFIG_VALUES["TRANSFER_BACK_BUTTON"]["pady"])

    def revoke_from_archive(self):
        # TODO CHANGE VARIABLE_NAME
        self.databases.orders.update_order_value(order_id=self.order_id, variable_name="status", variable_value=0)
