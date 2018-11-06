import tkinter as tk
from wui.record.archive_scripts.archived_order_class import ArchivedOrder
import values.constants as const
import datetime


# TODO sum of day; clear window


class Archive(tk.Toplevel):
    def __init__(self, database_container):
        super().__init__()
        self.databases = database_container
        self.orders = []
        self.date = self.get_today()
        self.date_string = tk.StringVar()

        self.date_string.set(self.date.strftime("%Y-%m-%d"))
        self.containers = {}
        self.widgets = {}
        self.setup()

    def setup(self):
        self.create_containers()
        self.setup_containers()
        self.setup_scrollbar()
        self.create_widgets()
        day_ids = self.get_orders_id_from(self.date)
        for i in day_ids:
            self.create_order(i)

    def create_containers(self):
        """
        This method initializes frames, canvas and scrollbar
        and stores them in container_widgets dictionary
        :return:
        """
        self.containers.update({
            "main_frame": tk.Frame(master=self)})
        self.containers.update({
            "panel_frame": tk.Frame(master=self.containers["main_frame"]),
            "order_frame": tk.Frame(master=self.containers["main_frame"],
                                    width=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"]["width"],
                                    height=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"]["height"])})
        self.containers.update({
            "order_canvas": tk.Canvas(master=self.containers["order_frame"])})
        self.containers.update({
            "orders_container": tk.Frame(master=self.containers["order_canvas"]),
            "orders_scrollbar": tk.Scrollbar(master=self.containers["order_frame"],
                                             orient=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_SCROLLBAR"]["orient"],
                                             command=self.containers["order_canvas"].yview)
        })

    def setup_containers(self):
        """
        This method sets up main window with necessary functions
        :return:
        """
        self.containers["main_frame"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["row"],
                                           column=const.ARCHIVE_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["column"],
                                           sticky=const.ARCHIVE_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["sticky"])
        self.containers["panel_frame"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["PANEL_FRAME"]["row"],
                                            column=const.ARCHIVE_WIDGET_CONFIG_VALUES["PANEL_FRAME"]["column"])
        self.containers["order_frame"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"]["row"],
                                            column=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"]["column"],
                                            sticky=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"]["sticky"])
        self.containers["order_frame"].grid_rowconfigure(0, weight=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"][
            "weight"])
        self.containers["order_frame"].grid_columnconfigure(0, weight=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_FRAME"][
            "weight"])
        self.containers["order_canvas"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_CANVAS"]["row"],
                                             column=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_CANVAS"]["column"],
                                             sticky=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_CANVAS"]["sticky"])
        self.containers["orders_container"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_CONTAINER"]["row"],
                                                 column=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_CONTAINER"][
                                                     "column"])

    def setup_scrollbar(self):
        """
        This method sets up scrollbar to allow scrolling
        :return:
        """
        self.containers["order_frame"].grid_propagate(False)
        self.containers["orders_scrollbar"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_SCROLLBAR"]["row"],
                                                 column=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_SCROLLBAR"][
                                                     "column"],
                                                 sticky=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDERS_SCROLLBAR"][
                                                     "sticky"])
        # self.container_widgets["order_canvas"].bind_all("<Button-4>", self.on_mousewheel)  # TODO not working
        # self.container_widgets["order_canvas"].bind_all("<Button-5>", self.on_mousewheel)  # TODO not working
        self.containers["order_canvas"].config(yscrollcommand=
                                               self.containers["orders_scrollbar"].set)
        self.containers["order_canvas"].config(scrollregion=
                                               self.containers["order_canvas"].bbox("all"))
        self.containers["order_canvas"].create_window((0, 0),
                                                      window=self.containers["orders_container"],
                                                      anchor=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_CANVAS"][
                                                          "anchor"])
        # TODO change width
        self.containers["order_canvas"].config(width=const.ARCHIVE_WIDGET_CONFIG_VALUES["ORDER_CANVAS"]["width"] +
                                                     self.containers["orders_scrollbar"].winfo_width())

    def create_order(self, order_id):
        """
        Invoking this method creates new order in window
        :return:
        """
        # add new order to list container
        self.orders += [
            ArchivedOrder(master=self.containers["orders_container"],
                          database_container=self.databases, order_id=order_id)]

        # set up grid of lastly created object and update scrollbar range
        self.orders[-1].grid(row=len(self.orders),
                             column=const.ARCHIVE_WIDGET_CONFIG_VALUES["NEW_ORDER"]["column"],
                             sticky=const.ARCHIVE_WIDGET_CONFIG_VALUES["NEW_ORDER"]["sticky"])

        self.containers["orders_container"].update_idletasks()
        self.containers["order_canvas"].config(scrollregion=
                                               self.containers["order_canvas"].bbox("all"))

    def create_widgets(self):
        self.widgets.update({
            "date_label": tk.Label(master=self.containers["panel_frame"], textvariable=self.date_string)
        })
        self.widgets.update({
            "previous_day_button": tk.Button(master=self.containers["panel_frame"], text="<-",
                                             command=lambda: self.change_day(-1))
        })
        self.widgets.update({
            "next_day_button": tk.Button(master=self.containers["panel_frame"], text="->",
                                         command=lambda: self.change_day(1))
        })
        self.widgets["date_label"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["DATE_LABEL"]["row"],
                                        column=const.ARCHIVE_WIDGET_CONFIG_VALUES["DATE_LABEL"]["column"])
        self.widgets["previous_day_button"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["PREVIOUS_DAY_BUTTON"]["row"],
                                                 column=const.ARCHIVE_WIDGET_CONFIG_VALUES["PREVIOUS_DAY_BUTTON"][
                                                     "column"])
        self.widgets["next_day_button"].grid(row=const.ARCHIVE_WIDGET_CONFIG_VALUES["NEXT_DAY_BUTTON"]["row"],
                                             column=const.ARCHIVE_WIDGET_CONFIG_VALUES["NEXT_DAY_BUTTON"]["column"])

    def get_today(self):
        date = datetime.datetime.now()
        # set searching date to 00:00:00:000000
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)

        return date

    def change_day(self, number_of_days):
        self.date += datetime.timedelta(days=number_of_days)
        self.date_string.set(self.date.strftime("%Y-%m-%d"))
        day_ids = self.get_orders_id_from(self.date)
        for order in self.orders:
            order.destroy()
        self.containers["orders_container"].update_idletasks()
        self.containers["order_canvas"].config(scrollregion=
                                               self.containers["order_canvas"].bbox("all"))
        for id in day_ids:
            self.create_order(id)

    def get_orders_id_from(self, day_start):
        day_end = day_start + datetime.timedelta(days=1)
        return self.databases.orders.select_orders_from(day_start, day_end)
