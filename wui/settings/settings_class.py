import tkinter as tk
import values.constants as const
from sql.database_scripts.menu_database_class import MenuDatabase
from sql.database_scripts.orders_database_class import OrdersDatabase
from sql.database_scripts.ordered_items_database_class import OrderedItems
from sql.database_scripts.database_class import Database


class Settings(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.widget_container = {}
        self.create_panel()

    def create_panel(self):
        self.widget_container["setup_databases"] = tk.Button(
            master=self,
            command=lambda: self.create_databases(),
            text=const.SETTINGS_WIDGET_CONFIG_VALUES["SETUP_DATABASES"]["text"],
            width=const.SETTINGS_WIDGET_CONFIG_VALUES["SETUP_DATABASES"]["width"],
            height=const.SETTINGS_WIDGET_CONFIG_VALUES["SETUP_DATABASES"]["height"])
        self.widget_container["setup_databases"].grid(
            row=const.SETTINGS_WIDGET_CONFIG_VALUES["SETUP_DATABASES"]["row"],
            column=const.SETTINGS_WIDGET_CONFIG_VALUES["SETUP_DATABASES"]["column"])

        self.widget_container["clear_orders"] = tk.Button(
            master=self,
            command=lambda: self.clear_orders(),
            text=const.SETTINGS_WIDGET_CONFIG_VALUES["CLEAR_ORDERS"]["text"],
            width=const.SETTINGS_WIDGET_CONFIG_VALUES["CLEAR_ORDERS"]["width"],
            height=const.SETTINGS_WIDGET_CONFIG_VALUES["CLEAR_ORDERS"]["height"])
        self.widget_container["clear_orders"].grid(
            row=const.SETTINGS_WIDGET_CONFIG_VALUES["CLEAR_ORDERS"]["row"],
            column=const.SETTINGS_WIDGET_CONFIG_VALUES["CLEAR_ORDERS"]["column"])

    def create_databases(self):
        Database.create_database(Database)
        menu_db = MenuDatabase()
        orders_db = OrdersDatabase()
        items_db = OrderedItems()
        menu_db.reset_table()
        orders_db.reset_table()
        items_db.reset_table()

    def clear_orders(self):
        orders_db = OrdersDatabase()
        items_db = OrderedItems()
        orders_db.reset_table()
        items_db.reset_table()
