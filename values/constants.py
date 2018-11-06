ORDER_DEFAULT_ITEM_COUNT = 4

ORDER_LABEL_ROW = 1
ORDER_PANEL_ROW = 0

ITEM_ENTRY_COLUMNS = {"CODE": 1,
                      "NAME": 2,
                      "TYPE": 5,
                      "COUNT": 4,
                      "DEF_PRICE": 6,
                      "PRICE": 7,
                      "DISC_PRICE": 9,
                      "HINT": 8
                      }
ITEMS_PADX = 0
ITEM_PADX = 0
ITEM_PADY = 0

WIDTH = {
    "BASE": 4
}

ORDER_DELETE_BUTTON_COLUMN = 0
ORDER_TRANSFER_BUTTON_COLUMN = 1
ORDER_TABLE_ENTRY_COLUMN = 3
ORDER_DISCOUNT_ENTRY_COLUMN = 5
ORDER_BULK_DISCOUNT_ENTRY_COLUMN = 6
ORDER_TABLE_LABEL_COLUMN = 2
ORDER_ADD_ITEM_BUTTON_COLUMN = 0
ORDER_DISCOUNT_LABEL_COLUMN = 4
ORDER_SUM_LABEL_COLUMN = 6
ORDER_SUM_ENTRY_COLUMN = 7
ORDER_SUM_DISCOUNTED_LABEL_COLUMN = 8
ORDER_SUM_DISCOUNTED_ENTRY_COLUMN = 9

ORDER_FRAME_SIZE = {"width": 900, "height": 600}

APPLICATION_WIDGET_CONFIG_VALUES = {
    "TK": {"title": "Aplikancja"},
    "OPEN_RECORD": {"row": 0, "column": 0, "height": 10, "width": 20, "text": "otwórz ewidencję"},
    "SETTINGS": {"row": 0, "column": 1, "height": 10, "width": 20, "text": "opcje"}

}
SETTINGS_WIDGET_CONFIG_VALUES = {
    "SETUP_DATABASES": {"row": 0, "column": 0, "height": 10, "width": 20, "text": "stwórz bazy"},
    "CLEAR_ORDERS": {"row": 0, "column": 1, "height": 10, "width": 20, "text": "usuń dane"}

}
RECORD_WIDGET_CONFIG_VALUES = {
    "RECORD_WINDOW": {"title": "Ewidencja"},
    "CREATE_ORDER_BUTTON": {"text": "stwórz zamówienie", "width": 15, "height": 2, "row": 0, "column": 0},
    "OPEN_ARCHIVE_BUTTON": {"text": "archiwum", "width": 15, "height": 2, "row": 0, "column": 1},
    "SHOW_MENU_BUTTON": {"text": "wyświetl menu", "width": 15, "height": 2, "row": 0, "column": 2},
    "RESTORE_ORDERS_BUTTON": {"text": "odzyskaj niezamknięte", "width": 15, "height": 2, "row": 0, "column": 3},
}
ORDER_WIDGET_CONFIG_VALUES = {
    "CODE_LABEL": {
        "text": "kod", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["CODE"]},
    "NAME_LABEL": {
        "text": "nazwa", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["NAME"]},
    "COUNT_LABEL": {
        "text": "liczba", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["COUNT"]},
    "TYPE_LABEL": {
        "text": "typ", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["TYPE"]},
    "DEF_PRICE_LABEL": {
        "text": "cena/szt.", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["DEF_PRICE"]},
    "PRICE_LABEL": {
        "text": "cena", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["PRICE"]},
    "HINT_LABEL": {
        "text": "uwagi", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["HINT"]},
    "DISC_PRICE_LABEL": {
        "text": "cena końcowa", "row": ORDER_LABEL_ROW, "column": ITEM_ENTRY_COLUMNS["DISC_PRICE"]},
    "DELETE_BUTTON": {
        "text": "x", "width": 2, "height": 1, "row": ORDER_PANEL_ROW, "column": 0},
    "TRANSFER_BUTTON": {
        "text": "->", "width": 2, "height": 1, "row": ORDER_PANEL_ROW, "column": 1},
    "TABLE_LABEL": {
        "text": "stolik", "row": ORDER_PANEL_ROW, "column": 2},
    "TABLE_ENTRY": {
        "width": 8, "row": ORDER_PANEL_ROW, "column": 3},
    "DISCOUNT_LABEL": {
        "text": "zniżka", "row": ORDER_PANEL_ROW, "column": 4},
    "DISCOUNT_ENTRY": {
        "width": 2, "height": 1, "row": ORDER_PANEL_ROW, "column": 5},
    "BULK_DISCOUNT_BUTTON": {
        "text": "na wagę?", "row": ORDER_PANEL_ROW, "column": 7, "columnspan": 2},
    "ADD_ITEM_BUTTON": {
        "text": "+", "width": 2, "height": 1, "row": 2, "column": 0, "sticky": 'nw', "rowspan": 2, "pady": 5,
        "padx": 5},
    "SUM_LABEL": {
        "text": "suma", "row": 2, "column": 6},
    "SUM_ENTRY": {
        "width": 8, "row": 2, "column": 7},
    "DISC_SUM_LABEL": {
        "text": "suma końcowa", "row": 2, "column": 8},
    "DISC_SUM_ENTRY": {
        "width": 8, "row": 2, "column": 9}
}

ITEM_WIDGET_CONFIG_VALUES = {
    "CODE_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["CODE"], "width": WIDTH["BASE"] * 1, "padx": ITEM_PADX},
    "NAME_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["NAME"], "columnspan": 2, "width": WIDTH["BASE"] * 7, "padx": ITEM_PADX},
    "COUNT_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["COUNT"], "width": WIDTH["BASE"] * 1, "padx": ITEM_PADX},
    "PRICE_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["PRICE"], "width": WIDTH["BASE"] * 2, "padx": ITEM_PADX},
    "DEF_PRICE_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["DEF_PRICE"], "width": WIDTH["BASE"] * 2, "padx": ITEM_PADX},
    "DISC_PRICE_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["DISC_PRICE"], "width": WIDTH["BASE"] * 2, "padx": ITEM_PADX},
    "TYPE_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["TYPE"], "width": WIDTH["BASE"] * 3, "padx": ITEM_PADX},
    "HINT_ENTRY": {
        "column": ITEM_ENTRY_COLUMNS["HINT"], "width": WIDTH["BASE"] * 2, "padx": ITEM_PADX},
}

ARCHIVE_WIDGET_CONFIG_VALUES = {
    "MAIN_FRAME": {
        "row": 0, "column": 0, "sticky": "news"},
    "ORDER_CANVAS": {
        "row": 0, "column": 0, "sticky": "news", "width": 600, "anchor": "nw"},
    "PANEL_FRAME": {
        "row": 0, "column": 0},
    "ORDERS_CONTAINER": {
        "row": 0, "column": 0},
    "ORDER_FRAME": {
        "width": 500, "height": 600, "row": 1, "column": 0, "sticky": "nw", "weight": 5},
    "ORDERS_SCROLLBAR": {
        "orient": "vertical", "row": 0, "column": 1, "sticky": "ns"},
    "NEW_ORDER": {
        "column": 0, "sticky": "w"},
    "DATE_LABEL": {
        "row": 0, "column": 1},
    "PREVIOUS_DAY_BUTTON": {
        "row": 0, "column": 0},
    "NEXT_DAY_BUTTON": {
        "row": 0, "column": 2}
}

ARCHIVED_ORDER_WIDGET_CONFIG_VALUES = {
    "ITEM_FRAME": {
        "row": 2, "column": 0, "columnspan": 4, "sticky": "w"},
    "NAME": {
        "text": "nazwa", "font": 'Helvetica 11 bold', "width": WIDTH["BASE"] * 7, "anchor": "w",
        "row": 1, "column": 0, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "TYPE": {
        "text": "typ", "font": 'Helvetica 11 bold', "width": WIDTH["BASE"] * 3, "anchor": "w",
        "row": 1, "column": 1, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "COUNT": {
        "text": "ilość", "font": 'Helvetica 11 bold', "width": WIDTH["BASE"] * 2, "anchor": "w",
        "row": 1, "column": 2, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "DISC_PRICE": {
        "text": "cena", "font": 'Helvetica 11 bold', "width": WIDTH["BASE"] * 2, "anchor": "w",
        "row": 1, "column": 3, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "OPENING_TIME": {
        "text": "otwarto: ", "font": 'Helvetica 11 bold', "anchor": "w",
        "row": 0, "column": 0, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "DISCOUNT": {
        "text": "zniżka: ", "font": 'Helvetica 11 bold', "anchor": "w",
        "row": 3, "column": 0, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "PRICE_SUM": {
        "text": "suma: ", "font": 'Helvetica 11 bold', "anchor": "w",
        "row": 3, "column": 2, "columnspan": 2, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "TRANSFER_BACK_BUTTON": {
        "text": "<--", "width": 6, "row": 0, "column": 3, "columnspan": 2, "padx": ITEM_PADX,
        "sticky": "w", "pady": ITEM_PADY},

}

ARCHIVED_ITEM_WIDGET_CONFIG_VALUES = {
    "NAME": {"width": WIDTH["BASE"] * 7, "anchor": "w",
             "column": 0, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "TYPE": {"width": WIDTH["BASE"] * 3, "anchor": "w",
             "column": 1, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "COUNT": {"width": WIDTH["BASE"] * 2, "anchor": "w",
              "column": 2, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
    "PRICE": {"width": WIDTH["BASE"] * 2, "anchor": "w",
              "column": 3, "padx": ITEM_PADX, "sticky": "w", "pady": ITEM_PADY},
}

MENU_WIDGET_CONFIG_VALUES = {
    "MAIN_FRAME": {"row": 0, "column": 0, "sticky": "news"},
    "PANEL_FRAME": {"row": 0, "column": 0, "sticky": "nw"},
    "MENU_FRAME": {"row": 1, "column": 0, "sticky": "nw", "width": 675, "height": 400, "weight": 5},
    "CANVAS": {"row": 0, "column": 0, "sticky": "news", "anchor": "nw", "width": 600},
    "SCROLLBAR": {"row": 0, "column": 1, "sticky": "ns", "orient": "vertical"},
    "MENU_CONTAINER": {"row": 0, "column": 0},
    "ID_LABEL": {"text": "id", "width": WIDTH["BASE"] * 1,
                 "row": 1, "column": 0, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "NAME_LABEL": {"text": "nazwa", "width": WIDTH["BASE"] * 7,
                   "row": 1, "column": 1, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "CODE_LABEL": {"text": "kod", "width": WIDTH["BASE"] * 1,
                   "row": 1, "column": 2, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_0_LABEL": {"text": "sztuka", "width": WIDTH["BASE"] * 2,
                      "row": 1, "column": 3, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_1_LABEL": {"text": "gaiwan", "width": WIDTH["BASE"] * 2,
                      "row": 1, "column": 4, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_2_LABEL": {"text": "opk.", "width": WIDTH["BASE"] * 2,
                      "row": 1, "column": 5, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_3_LABEL": {"text": "na wagę", "width": WIDTH["BASE"] * 2,
                      "row": 1, "column": 6, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "ID": {"width": WIDTH["BASE"], "column": 0, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "NAME": {"width": WIDTH["BASE"] * 7, "column": 1, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "CODE": {"width": WIDTH["BASE"], "column": 2, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_0": {"width": WIDTH["BASE"] * 2, "column": 3, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_1": {"width": WIDTH["BASE"] * 2, "column": 4, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_2": {"width": WIDTH["BASE"] * 2, "column": 5, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "PRICE_3": {"width": WIDTH["BASE"] * 2, "column": 6, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"},
    "EDIT_BUTTON": {"text": "edit", "width": 1, "column": 7, "padx": ITEM_PADX, "pady": ITEM_PADY, "sticky": "w"}
}

# TODO FIX THEEESEEE
ORDER_ADD_ITEM_BUTTON_ROW = 2
ORDER_ITEM_STARTING_ROW = 2
ORDER_SUM_STARTING_ROW = 2 + ORDER_DEFAULT_ITEM_COUNT

ORDER_FRAME_COLUMN = 0

# WIDTH_ORDER = WIDTH_CODE+WIDTH_COUNT+WIDTH_DEFAULT_PRICE+\
#             WIDTH_DISCOUNTED_PRICE+WIDTH_HINT+WIDTH_NAME+\
#            WIDTH_PRICE+WIDTH_TYPE
WIDTH_ORDER = 600

type_list = ['', 'sztuka', 'czajnik', 'gaiwan', 'gram', 'opakowanie']
