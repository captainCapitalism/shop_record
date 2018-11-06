"""
This file contains a class OrderedItems and it"s methods, that carry operations on ordered Items
"""
import sql.sql_variables.sql_variables as db_constants
from sql.database_scripts.database_class import Database


class OrderedItems(Database):
    """
    This class handles operations on table containing orderedItems
    """

    def __init__(self):
        super(OrderedItems, self).__init__(db_constants.TABLE_ORDERED_ITEMS_NAME,
                                           db_constants.TABLE_ORDERED_ITEMS_COLUMNS)

    def create_table(self):
        """
        This method creates table to store ordered Items
        """
        variables = ()
        variables += (self.table_name,)
        variables += self.column_names
        query = "CREATE TABLE IF NOT EXISTS %s (" \
                "%s INT AUTO_INCREMENT PRIMARY KEY," \
                "%s INT, " \
                "%s INT, " \
                "%s DOUBLE," \
                "%s VARCHAR(10)" \
                ")" % variables
        self.cursor.execute(query)

    def reset_table(self):
        """
        This method drops existing table and replaces it with new instance
        """

        query = "DROP TABLE IF EXISTS %s" % self.table_name
        self.cursor.execute(query)
        self.create_table()

    def insert_item_into_database(self, order_id, position_id, item_count=1, item_type=""):
        """

        :param order_id:
        :param position_id:
        :param item_count:
        :param item_type:
        :return:
        """
        constants = (tuple([self.table_name]) + self.column_names[1:])
        input_variables = (order_id, position_id, item_count, item_type)
        variables = constants + input_variables
        query = "INSERT INTO %s (%s, %s, %s, %s) VALUES (%s, %s, %s, \"%s\")" % variables
        self.cursor.execute(query)
        self.database.commit()

    def select_all_items_from_order(self, order_id):
        """

        :param order_id:
        :return:
        """
        variables = (self.table_name, self.column_names[1], order_id)
        query = "SELECT * FROM %s WHERE %s = %s" % variables
        cursor = self.database.cursor(dictionary=True)
        cursor.execute(query)
        all_ordered_items = cursor.fetchall()
        cursor.close()
        return all_ordered_items

    def select_item_from_order(self, item_id):
        """

        :param item_id:
        :return:
        """
        variables = (self.table_name, self.column_names[0], item_id)
        query = "SELECT * FROM %s WHERE %s = %s" % variables
        cursor = self.database.cursor(dictionary=True)
        cursor.execute(query)
        ordered_item = cursor.fetchall()[0]
        cursor.close()
        return ordered_item

    def update_ordered_item_value(self, item_id, variable_name, variable_value):
        """
        this method updates one of the ordered item's values
        :param item_id:
        :param variable_name:
        :param variable_value:
        :return:
        """
        variables = [self.table_name, variable_name,
                     variable_value, self.column_names[0], item_id]
        query = "UPDATE %s SET %s = \'%s\' WHERE %s = %s" % tuple(variables)
        self.cursor.execute(query)
        self.database.commit()

    def delete_item(self, item_id):
        """
        This method removes chosen item from table
        :param item_id:
        :return:
        """
        variables = [self.table_name, self.column_names[0], item_id]
        query = "DELETE FROM %s  WHERE %s = %s" % tuple(variables)
        self.cursor.execute(query)
        self.database.commit()

    def delete_all_items_from_order(self, order_id):
        """
        This method removes all items of chosen order
        :param order_id:
        :return:
        """
        variables = [self.table_name, self.column_names[1], order_id]
        query = "DELETE FROM %s  WHERE %s = %s" % tuple(variables)
        self.cursor.execute(query)
        self.database.commit()
