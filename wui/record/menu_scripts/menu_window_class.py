import tkinter as tk
from wui.record.menu_scripts.edit_item_window_class import Edit
import values.constants as const


class MenuWindow(tk.Toplevel):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu
        self.containers = {}
        self.labels = {}
        self.widgets = {}
        self.menu_position_variable_container = []
        self.menu_position_widget_container = []
        self.create_containers()
        self.setup_containers()
        self.setup_scrollbar()
        self.create_panel_ui()
        self.list_menu()

    def create_containers(self):
        """
        This method initializes frames, canvas and scrollbar
        and stores them in container_widgets dictionaryionary
        :return:
        """
        self.containers.update({
            "main_frame": tk.Frame(master=self)})
        self.containers.update({
            "panel_frame": tk.Frame(master=self.containers["main_frame"]),
            "menu_frame": tk.Frame(master=self.containers["main_frame"],
                                   width=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["width"],
                                   height=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["height"])})
        self.containers.update({
            "canvas": tk.Canvas(master=self.containers["menu_frame"])})
        self.containers.update({
            "menu_container": tk.Frame(master=self.containers["canvas"]),
            "scrollbar": tk.Scrollbar(master=self.containers["menu_frame"],
                                      orient=const.MENU_WIDGET_CONFIG_VALUES["SCROLLBAR"]["orient"],
                                      command=self.containers["canvas"].yview)
        })

    def setup_containers(self):
        """
        This method sets up main window with necessary functions
        :return:
        """
        self.containers["main_frame"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["column"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["MAIN_FRAME"]["sticky"]
        )
        self.containers["panel_frame"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["PANEL_FRAME"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["PANEL_FRAME"]["column"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["PANEL_FRAME"]["sticky"]
        )
        self.containers["menu_frame"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["column"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["sticky"]
        )
        self.containers["menu_frame"].grid_rowconfigure(
            0, weight=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["weight"])
        self.containers["menu_frame"].grid_columnconfigure(
            0, weight=const.MENU_WIDGET_CONFIG_VALUES["MENU_FRAME"]["weight"])
        self.containers["canvas"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["CANVAS"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["CANVAS"]["column"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["CANVAS"]["sticky"]
        )
        self.containers["menu_container"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["MENU_CONTAINER"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["MENU_CONTAINER"]["column"]
        )

    def setup_scrollbar(self):
        """
        This method sets up scrollbar to allow scrolling
        :return:
        """
        self.containers["menu_frame"].grid_propagate(False)
        self.containers["scrollbar"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["SCROLLBAR"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["SCROLLBAR"]["column"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["SCROLLBAR"]["sticky"])
        # self.container_widgets["canvas"].bind_all("<Button-4>", self.on_mousewheel)  # TODO not working
        # self.container_widgets["canvas"].bind_all("<Button-5>", self.on_mousewheel)  # TODO not working
        self.containers["canvas"].config(
            yscrollcommand=self.containers["scrollbar"].set)
        self.containers["canvas"].config(
            scrollregion=self.containers["canvas"].bbox("all"))
        self.containers["canvas"].create_window(
            (0, 0),
            window=self.containers["menu_container"],
            anchor=const.MENU_WIDGET_CONFIG_VALUES["CANVAS"]["anchor"])
        # TODO change width
        self.containers["canvas"].config(
            width=const.MENU_WIDGET_CONFIG_VALUES["CANVAS"]["width"] + self.containers["scrollbar"].winfo_width())

    def create_panel_ui(self):
        """
        This method creates top panel objects
        :return:
        """
        self.widgets["create_item_button"] = tk.Button(
            self.containers["panel_frame"],
            text="create new entry", width=11, height=1,
            command=lambda: self.create_new_entry())
        self.widgets["create_item_button"].grid(row=0, column=0, columnspan=3)
        self.setup_labels()

    def setup_labels(self):
        master = self.containers["panel_frame"]
        self.labels.update({
            "id_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["width"]),
            "name_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["width"]),
            "code_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["width"]),
            "price0_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["width"]),
            "price1_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["width"]),
            "price2_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["width"]),
            "price3_label": tk.Label(
                master=master,
                text=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["text"],
                width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["width"]),
        })
        self.labels["id_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["ID_LABEL"]["sticky"])
        self.labels["name_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["NAME_LABEL"]["sticky"])
        self.labels["code_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["CODE_LABEL"]["sticky"])
        self.labels["price0_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0_LABEL"]["sticky"])
        self.labels["price1_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1_LABEL"]["sticky"])
        self.labels["price2_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2_LABEL"]["sticky"])
        self.labels["price3_label"].grid(
            row=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["row"],
            column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["column"],
            padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["padx"],
            pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["pady"],
            sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3_LABEL"]["sticky"])

    def list_menu(self):
        list_of_dictionary = self.menu.select_all()
        x = 0
        master = self.containers["menu_container"]
        for dictionary in list_of_dictionary:
            widget_new_row = {
                "id": tk.Label(master=master,
                               text=dictionary["positionID"],
                               width=const.MENU_WIDGET_CONFIG_VALUES["ID"]["width"]),
                "name": tk.Label(master=master,
                                 text=dictionary["positionName"],
                                 width=const.MENU_WIDGET_CONFIG_VALUES["NAME"]["width"]),
                "code": tk.Label(master=master,
                                 text=dictionary["positionCode"],
                                 width=const.MENU_WIDGET_CONFIG_VALUES["CODE"]["width"]),
                "price0": tk.Label(master=master,
                                   text=dictionary["priceDefault"],
                                   width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0"]["width"]),
                "price1": tk.Label(master=master,
                                   text=dictionary["priceGaiwan"],
                                   width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1"]["width"]),
                "price2": tk.Label(master=master,
                                   text=dictionary["pricePackage"],
                                   width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2"]["width"]),
                "price3": tk.Label(master=master,
                                   text=dictionary["priceBulk"],
                                   width=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3"]["width"]),
                "edit_button": tk.Button(master=master,
                                         text=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["text"],
                                         width=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["width"])
            }

            self.menu_position_widget_container += [widget_new_row]
            self.menu_position_widget_container[x]["id"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["ID"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["ID"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["ID"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["ID"]["pady"])
            self.menu_position_widget_container[x]["name"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["NAME"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["NAME"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["NAME"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["NAME"]["pady"])
            self.menu_position_widget_container[x]["code"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["CODE"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["CODE"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["CODE"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["CODE"]["pady"])
            self.menu_position_widget_container[x]["price0"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_0"]["pady"])
            self.menu_position_widget_container[x]["price1"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_1"]["pady"])
            self.menu_position_widget_container[x]["price2"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_2"]["pady"])
            self.menu_position_widget_container[x]["price3"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["PRICE_3"]["pady"])
            self.menu_position_widget_container[x]["edit_button"].grid(
                row=x + 1,
                column=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["column"],
                sticky=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["sticky"],
                padx=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["padx"],
                pady=const.MENU_WIDGET_CONFIG_VALUES["EDIT_BUTTON"]["pady"])
            self.menu_position_widget_container[x]["edit_button"].configure(
                command=lambda item_id=self.menu_position_widget_container[x]["id"].cget("text"): self.edit_item(
                    item_id))

            x += 1

        self.containers["menu_container"].update_idletasks()
        self.containers["canvas"].config(scrollregion=
                                         self.containers["canvas"].bbox("all"))

    def edit_item(self, item_id):
        Edit(menu=self.menu, menu_window=self, item_id=item_id)

    def create_new_entry(self):
        Edit(self.menu, self)

    def refresh_window(self):
        list_of_dictionary = self.menu.select_all()
        x = 0

        for dictionary in list_of_dictionary:
            self.menu_position_widget_container[x]["name"].configure(text=dictionary["positionName"])
            self.menu_position_widget_container[x]["code"].configure(text=dictionary["positionCode"])
            self.menu_position_widget_container[x]["price0"].configure(text=dictionary["priceDefault"])
            self.menu_position_widget_container[x]["price1"].configure(text=dictionary["priceGaiwan"])
            self.menu_position_widget_container[x]["price2"].configure(text=dictionary["pricePackage"])
            self.menu_position_widget_container[x]["price3"].configure(text=dictionary["priceBulk"])
            x += 1
