"""
This module contains Record class and it's methods
"""

import tkinter as tk
from wui.record.record_scripts.order_class import Order
import values.constants as const
from wui.record.menu_scripts.menu_window_class import MenuWindow
from wui.record.archive_scripts.archive_class import Archive
from sql.database_scripts.menu_database_class import MenuDatabase
from sql.database_scripts.orders_database_class import OrdersDatabase
from sql.database_scripts.ordered_items_database_class import OrderedItems
from sql.database_scripts.database_container_class import DatabaseContainer


# TODO OPEN NOT CLOSED ORDERS
# TODO BASIA-TASKS
# TODO RESERVATIONS
# TODO SELECT TABLE
# TODO TABLE SORTING
class Record(tk.Toplevel):
    """
    This class acts as Tk object for application
    contains other crucial tk objects like frames and canvas for proper functioning
    """

    def __init__(self):
        super().__init__()
        self.title(const.RECORD_WIDGET_CONFIG_VALUES["RECORD_WINDOW"]["title"])
        self.databases = DatabaseContainer(
            menu=MenuDatabase(),
            orders=OrdersDatabase(),
            items=OrderedItems())
        self.orders = []
        self.container_widgets = {}
        self.panel_widgets = {}

        self.create_widgets()
        # self.restore_open_orders()

    def create_widgets(self):
        """
        This method runs methods responsible for initializing interface
        :return:
        """
        self.create_containers()
        self.setup_containers()
        self.create_panel_widgets()
        self.setup_scrollbar()

    def create_containers(self):
        """
        This method initializes frames, canvas and scrollbar
        and stores them in container_widgets dictionary
        :return:
        """
        self.container_widgets.update({
            "main_frame": tk.Frame(master=self)})
        self.container_widgets.update({
            "panel_frame": tk.Frame(master=self.container_widgets["main_frame"]),
            "order_frame": tk.Frame(master=self.container_widgets["main_frame"],
                                    width=const.ORDER_FRAME_SIZE["width"],
                                    height=const.ORDER_FRAME_SIZE["height"])})
        self.container_widgets.update({
            "order_canvas": tk.Canvas(master=self.container_widgets["order_frame"])})
        self.container_widgets.update({
            "orders_container": tk.Frame(master=self.container_widgets["order_canvas"]),
            "orders_scrollbar": tk.Scrollbar(master=self.container_widgets["order_frame"],
                                             orient="vertical",
                                             command=self.container_widgets["order_canvas"].yview)
        })

    def setup_containers(self):
        """
        This method sets up main window with necessary functions
        :return:
        """
        self.container_widgets["main_frame"].grid(row=0, column=0, sticky='news')
        self.container_widgets["panel_frame"].grid(row=0, column=0)
        self.container_widgets["order_frame"].grid(row=1, column=0, sticky='nw')
        self.container_widgets["order_frame"].grid_rowconfigure(0, weight=5)
        self.container_widgets["order_frame"].grid_columnconfigure(0, weight=5)
        self.container_widgets["order_canvas"].grid(row=0, column=0, sticky='news')
        self.container_widgets["orders_container"].grid(column=0, row=0)

    def create_order(self, order_id=0):
        """
        Invoking this method creates new order in window
        :return:
        """
        # add new order to list container
        self.orders += [
            Order(self,
                  self.databases, order_id)]

        # set up grid of lastly created object and update scrollbar range
        self.orders[-1].grid(row=len(self.orders),
                             column=const.ORDER_FRAME_COLUMN)

        self.container_widgets["orders_container"].update_idletasks()
        self.container_widgets["order_canvas"].config(
            scrollregion=self.container_widgets["order_canvas"].bbox("all"))

    def setup_scrollbar(self):
        """
        This method sets up scrollbar to allow scrolling
        :return:
        """
        self.container_widgets["order_frame"].grid_propagate(False)
        self.container_widgets["orders_scrollbar"].grid(row=0, column=1, sticky='ns')
        self.container_widgets["order_canvas"].bind_all("<Button-4>", self.on_mousewheel)  # TODO not working
        self.container_widgets["order_canvas"].bind_all("<Button-5>", self.on_mousewheel)  # TODO not working
        self.container_widgets["order_canvas"].config(
            yscrollcommand=self.container_widgets["orders_scrollbar"].set)
        self.container_widgets["order_canvas"].config(
            scrollregion=self.container_widgets["order_canvas"].bbox("all"))
        self.container_widgets["order_canvas"].create_window(
            (0, 0),
            window=self.container_widgets["orders_container"],
            anchor='nw')
        # TODO change width
        self.container_widgets["order_canvas"].config(
            width=600 + self.container_widgets["orders_scrollbar"].winfo_width())

    def create_panel_widgets(self):
        """
        This method creates top panel objects
        :return:
        """
        self.panel_widgets["create_order_button"] = tk.Button(
            master=self.container_widgets["panel_frame"],
            command=lambda: self.create_order(),
            text=const.RECORD_WIDGET_CONFIG_VALUES["CREATE_ORDER_BUTTON"]["text"],
            width=const.RECORD_WIDGET_CONFIG_VALUES["CREATE_ORDER_BUTTON"]["width"],
            height=const.RECORD_WIDGET_CONFIG_VALUES["CREATE_ORDER_BUTTON"]["height"])
        self.panel_widgets["create_order_button"].grid(
            row=const.RECORD_WIDGET_CONFIG_VALUES["CREATE_ORDER_BUTTON"]["row"],
            column=const.RECORD_WIDGET_CONFIG_VALUES["CREATE_ORDER_BUTTON"]["column"])

        self.panel_widgets["show_menu_button"] = tk.Button(
            self.container_widgets["panel_frame"],
            command=lambda: MenuWindow(self.databases.menu),
            text=const.RECORD_WIDGET_CONFIG_VALUES["SHOW_MENU_BUTTON"]["text"],
            width=const.RECORD_WIDGET_CONFIG_VALUES["SHOW_MENU_BUTTON"]["width"],
            height=const.RECORD_WIDGET_CONFIG_VALUES["SHOW_MENU_BUTTON"]["height"])
        self.panel_widgets["show_menu_button"].grid(
            row=const.RECORD_WIDGET_CONFIG_VALUES["SHOW_MENU_BUTTON"]["row"],
            column=const.RECORD_WIDGET_CONFIG_VALUES["SHOW_MENU_BUTTON"]["column"])

        self.panel_widgets["show_orders_button"] = tk.Button(
            self.container_widgets["panel_frame"],
            command=lambda: self.open_archive(),
            text=const.RECORD_WIDGET_CONFIG_VALUES["OPEN_ARCHIVE_BUTTON"]["text"],
            width=const.RECORD_WIDGET_CONFIG_VALUES["OPEN_ARCHIVE_BUTTON"]["width"],
            height=const.RECORD_WIDGET_CONFIG_VALUES["OPEN_ARCHIVE_BUTTON"]["height"])

        self.panel_widgets["show_orders_button"].grid(
            row=const.RECORD_WIDGET_CONFIG_VALUES["OPEN_ARCHIVE_BUTTON"]["row"],
            column=const.RECORD_WIDGET_CONFIG_VALUES["OPEN_ARCHIVE_BUTTON"]["column"])

        self.panel_widgets["restore_orders_button"] = tk.Button(
            self.container_widgets["panel_frame"],
            command=lambda: self.restore_open_orders(),
            text=const.RECORD_WIDGET_CONFIG_VALUES["RESTORE_ORDERS_BUTTON"]["text"],
            width=const.RECORD_WIDGET_CONFIG_VALUES["RESTORE_ORDERS_BUTTON"]["width"],
            height=const.RECORD_WIDGET_CONFIG_VALUES["RESTORE_ORDERS_BUTTON"]["height"])

        self.panel_widgets["restore_orders_button"].grid(
            row=const.RECORD_WIDGET_CONFIG_VALUES["RESTORE_ORDERS_BUTTON"]["row"],
            column=const.RECORD_WIDGET_CONFIG_VALUES["RESTORE_ORDERS_BUTTON"]["column"])

    def open_archive(self):
        Archive(self.databases)

    def on_mousewheel(self, event):
        """
        This method allows scrolling with mousewheel/touchpad
        :param event:
        :return:
        """
        self.container_widgets["order_canvas"].yview_scroll(-1 * int(event.delta / 120), "units")
        # TODO FIX SCROLLING

    def restore_open_orders(self):
        ids = self.databases.orders.find_open_orders()
        for item in ids:
            self.create_order(item)
