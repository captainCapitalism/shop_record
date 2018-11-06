import tkinter as tk
from wui.record.record_class import Record
from wui.settings.settings_class import Settings
import values.constants as const


# TODO CHANGE COLUMN NAMES TO DICT
# TODO EXTRACT VARIABLES FROM AUTOCOMPLETE ENTRIES

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(const.APPLICATION_WIDGET_CONFIG_VALUES["TK"]["title"])
        self.widget_container = {}
        self.create_menu()

    def create_menu(self):
        self.widget_container["Open Record"] = tk.Button(
            master=self,
            command=lambda: self.create_record(),
            text=const.APPLICATION_WIDGET_CONFIG_VALUES["OPEN_RECORD"]["text"],
            width=const.APPLICATION_WIDGET_CONFIG_VALUES["OPEN_RECORD"]["width"],
            height=const.APPLICATION_WIDGET_CONFIG_VALUES["OPEN_RECORD"]["height"])
        self.widget_container["Open Record"].grid(
            row=const.APPLICATION_WIDGET_CONFIG_VALUES["OPEN_RECORD"]["row"],
            column=const.APPLICATION_WIDGET_CONFIG_VALUES["OPEN_RECORD"]["column"])

        self.widget_container["Settings"] = tk.Button(
            master=self,
            command=lambda: self.create_settings(),
            text=const.APPLICATION_WIDGET_CONFIG_VALUES["SETTINGS"]["text"],
            width=const.APPLICATION_WIDGET_CONFIG_VALUES["SETTINGS"]["width"],
            height=const.APPLICATION_WIDGET_CONFIG_VALUES["SETTINGS"]["height"])
        self.widget_container["Settings"].grid(
            row=const.APPLICATION_WIDGET_CONFIG_VALUES["SETTINGS"]["row"],
            column=const.APPLICATION_WIDGET_CONFIG_VALUES["SETTINGS"]["column"])

    def create_record(self):
        Record()

    def create_settings(self):
        Settings()
