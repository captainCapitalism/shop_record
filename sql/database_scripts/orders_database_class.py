"""
This file contains a class MenuDatabase and it"s methods, that carry operations on menu data
"""
import sql.sql_variables.sql_variables as db_constants
from sql.database_scripts.database_class import Database


class OrdersDatabase(Database):
    """
    This class is responsible for handling operations on orders taken
    """

    def __init__(self):
        super(OrdersDatabase, self). \
            __init__(db_constants.TABLE_ORDERS_DATA_NAME, db_constants.TABLE_ORDERS_DATA_COLUMNS)

    def create_table(self):
        """
        This method initializes table
        :return:
        """
        self.connect_to_database()
        db_initialization_values = (tuple([self.table_name]) + self.column_names)
        query = "CREATE TABLE IF NOT EXISTS %s (" \
                "%s INT AUTO_INCREMENT PRIMARY KEY," \
                "%s BOOL, " \
                "%s DATETIME DEFAULT CURRENT_TIMESTAMP," \
                "%s DOUBLE," \
                "%s BOOL," \
                "%s DOUBLE," \
                "%s VARCHAR(6)" \
                ")" % db_initialization_values
        self.cursor.execute(query)

    def reset_table(self):
        """
        This method resets table
        :return:
        """
        query = "DROP TABLE IF EXISTS %s" % self.table_name
        self.cursor.execute(query)
        self.create_table()

    def create_empty_order(self):
        """
        This method creates new order in table
        :return:
        """
        variables = (self.table_name, self.column_names[1]) + \
                    self.column_names[3:-1] + db_constants.TABLE_ORDERS_DATA_DEFAULT_VALUES
        query = "INSERT INTO %s (%s, %s, %s, %s) VALUES (%s,%s,%s,%s)" % variables
        self.cursor.execute(query)
        self.database.commit()

    def update_order_value(self, order_id, variable_name, variable_value):
        """
        this method updates on of the order"s values
        :param order_id:
        :param variable_name:
        :param variable_value:
        :return:
        """
        variables = [self.table_name, variable_name,
                     variable_value, self.column_names[0], order_id]
        query = "UPDATE %s SET %s = %s WHERE %s = %s" % tuple(variables)
        self.cursor.execute(query)
        self.database.commit()

    def add_item_to_order(self, order_id, name, menu_db, ordered_items_db):
        """

        :param order_id:
        :param name:
        :param menu_db:
        :param ordered_items_db:
        :return:
        """
        menu_position_dictionary = menu_db.select_by_name(name)
        ordered_items_db.insert_item_into_dabatase(order_id, menu_position_dictionary["positionID"])

    def calculate_sum(self, order_id, ordered_items_db, menu):
        """
        This method calculates sum and discounted sum of all items placed in order
        :param order_id:
        :param ordered_items_db:
        :param menu:
        :return:
        """
        order_values = self.get_order_values_from_id(order_id)
        items_in_order = ordered_items_db.select_all_items_from_order(order_id)
        discount = order_values["discount"]
        discount_for_sale = order_values["discountForSale"]
        sum_of_prices = 0
        sum_of_discounted_prices = 0
        if not items_in_order:
            pass
        else:
            for item in items_in_order:
                [item_price, item_discounted_price] = menu.select_position_price(item["positionID"],
                                                                                 item["type"],
                                                                                 discount,
                                                                                 discount_for_sale)
                sum_of_prices += item["count"] * item_price
                sum_of_discounted_prices += item["count"] * item_discounted_price
        self.update_order_value(order_id, self.column_names[5], sum_of_discounted_prices)
        self.database.commit()
        return [sum_of_prices, sum_of_discounted_prices]

    def get_order_values_from_id(self, order_id):
        cursor = self.database.cursor(dictionary=True)
        variables = (self.table_name, self.column_names[0], order_id)
        query = "SELECT * from %s WHERE %s = %s" % variables
        cursor.execute(query)
        order_variables = cursor.fetchone()
        return order_variables

    def delete_order(self, order_id, items):
        """
        This method removes order from table and invokes method do remove it's records in ordered_items
        :param order_id:
        :param items
        :return:
        """
        variables = [self.table_name, self.column_names[0], order_id]
        query = "DELETE FROM %s  WHERE %s = %s" % tuple(variables)
        self.cursor.execute(query)
        self.database.commit()
        items.delete_all_items_from_order(order_id)

    def select_orders_from(self, start_date, end_date):
        variables = (self.column_names[0], self.table_name, self.column_names[1], self.column_names[2], start_date,
                     self.column_names[2], end_date)
        query = "SELECT %s FROM %s WHERE %s = 1 AND %s >= \'%s\' AND %s < \'%s\'" % variables
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = [i[0] for i in result]  # change list of tuples to list

        return result

    def find_open_orders(self):

        variables = (self.column_names[0], self.table_name, self.column_names[1])
        query = "SELECT %s FROM %s WHERE %s = 0" % variables
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]  # change list of tuples to list
        return results
