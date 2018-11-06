DATABASE_NAME = "shopData"
TABLE_MENU_DATA_NAME = "menuData"

TABLE_MENU_DATA_COLUMNS = ("positionID",  # 0
                           "positionName",  # 1
                           "positionCode",  # 2
                           "priceDefault",  # 3
                           "priceGaiwan",  # 4
                           "pricePackage",  # 5
                           "priceBulk")  # 6
MENU_DATA_FILE = "sql/db.txt"

TABLE_ORDERS_DATA_NAME = "orders"
TABLE_ORDERS_DATA_COLUMNS = ("orderID",  # 0
                             "status",  # 1
                             "openingTime",  # 2
                             "discount",  # 3
                             "discountForSale",  # 4
                             "priceSum",  # 5
                             "orderTable"  # 6
                             )
TABLE_ORDERS_DATA_DEFAULT_VALUES = (False,
                                    0,
                                    False,
                                    0
                                    )
TABLE_ORDERED_ITEMS_NAME = "orderedItems"
TABLE_ORDERED_ITEMS_COLUMNS = ("itemID",
                               "orderID",
                               "positionID",
                               "count",
                               "type"
                               )
