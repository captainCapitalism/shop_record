"""
This file contains a class MenuDatabase and it"s methods, that carry operations on menu data
"""
import sql.sql_variables.sql_variables as db_constants
from sql.database_scripts.database_class import Database


class MenuDatabase(Database):
    """
    This class handles operations on table containing menu positions
    """

    def __init__(self):
        super(MenuDatabase, self).__init__(db_constants.TABLE_MENU_DATA_NAME, db_constants.TABLE_MENU_DATA_COLUMNS)

    def create_table(self):
        """
        This method creates database at destined server
        """

        db_initialization_values = tuple([self.table_name]) + self.column_names
        query = "CREATE TABLE IF NOT EXISTS %s (" \
                "%s INT AUTO_INCREMENT PRIMARY KEY, " \
                "%s VARCHAR(40) NOT NULL," \
                "%s VARCHAR(4)," \
                "%s DOUBLE," \
                "%s DOUBLE," \
                "%s DOUBLE," \
                "%s DOUBLE" \
                ")" % db_initialization_values
        self.cursor.execute(query)
        self.set_table()

    def set_table(self):
        """
        This method sets values in created database that will serve as menu positions
        """

        query = "DELETE FROM %s" % self.table_name
        self.cursor.execute(query)
        menu_file = db_constants.MENU_DATA_FILE
        menu = open(menu_file, "r")

        for line in menu:
            column_values = line.split(";")
            column_values = [x.strip() for x in column_values]

            self.insert_into_menu(column_values)

        self.database.commit()
        menu.close()

    def reset_table(self):
        """
        This method drops existing table and replaces it with new instance
        """

        query = "DROP TABLE IF EXISTS %s" % self.table_name
        self.cursor.execute(query)
        self.create_table()

    def insert_into_menu(self, column_values):
        """
        This method inserts new item into menuDatabase
        :param column_values: desired values of new row in database
        """

        column_values[2] = float(column_values[2])
        column_values[3] = float(column_values[3])
        column_values[4] = float(column_values[4])
        column_values[5] = float(column_values[5])

        column_values = tuple(column_values)

        # remove first element of column names to not include key value positionID
        variables = (tuple([self.table_name]) + self.column_names[1:] + column_values)
        query = "INSERT INTO %s (%s, %s, %s, %s, %s, %s)" \
                " VALUES (\'%s\', \'%s\', %s, %s, %s, %s)" % variables
        self.cursor.execute(query)

    def search_for_position(self, item_name):
        """
        This method searches for a pattern in name in existing database
        :param item_name: desired string
        :return: list of items, that satisfy requirements
        """
        # TODO find better sorting: if /name/ at start of /position/ goes to front
        item_name = "\"%" + item_name + "%\""
        variables = (self.column_names[1], self.table_name, self.column_names[1], item_name)
        query = "SELECT %s FROM %s WHERE %s LIKE %s" % variables
        self.cursor.execute(query)
        results = []
        for item in self.cursor:
            results += [item[0]]
        results.sort()
        return tuple(results)

    def select_position_price(self, item_id, item_type, discount=0, discount_for_sale=0):
        """
        This method selects price from database based on input
        :param item_id:
        :param item_type:
        :param discount_for_sale:
        :return: price of item with item_id based on item_type
        """
        if item_type == "":
            column = self.column_names[3]
            if not discount_for_sale:
                discount_for_sale = True
        elif item_type == "sztuka":
            column = self.column_names[3]
            if not discount_for_sale:
                discount_for_sale = True
        elif item_type == "gaiwan":
            column = self.column_names[4]
            if not discount_for_sale:
                discount_for_sale = True
        elif item_type == "gram":
            column = self.column_names[6]
        elif item_type == "opakowanie":
            column = self.column_names[5]
        variables = (column, self.table_name, self.column_names[0], item_id)
        query = "SELECT %s FROM %s WHERE %s = %s" % variables
        self.cursor.execute(query)
        price = self.cursor.fetchone()[0]
        discounted_price = price - (price * discount * 0.01 * discount_for_sale)
        return [price, discounted_price]

    def select_by_name(self, name):
        """
        This method selects row from database using given name
        :param name: Name of desired item
        :return:
        """
        cursor = self.database.cursor(dictionary=True)
        variables = (self.table_name, self.column_names[1], name)
        query = "SELECT * FROM %s WHERE %s = \'%s\'" % variables
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def select_all(self):
        cursor = self.database.cursor(dictionary=True)
        query = "SELECT * FROM %s" % self.table_name
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close
        return result

    def select_by_id(self, item_id):
        """
        This method selects row from database using given name
        :param item_id: id of desired item
        :return:
        """
        cursor = self.database.cursor(dictionary=True)
        variables = (self.table_name, self.column_names[0], item_id)
        query = "SELECT * FROM %s WHERE %s = \'%s\'" % variables
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def update_entry(self, column_values):
        """text =,
        This method updates tem in menuDatabase
        :param column_values: desired values of row in database
        """
        column_values[3] = float(column_values[3])
        column_values[4] = float(column_values[4])
        column_values[5] = float(column_values[5])
        column_values[6] = float(column_values[6])

        # remove first element of column names to not include key value positionID
        variables = (self.table_name,
                     self.column_names[1], column_values[1], self.column_names[2], column_values[2],
                     self.column_names[3], column_values[3], self.column_names[4], column_values[4],
                     self.column_names[5], column_values[5], self.column_names[6], column_values[6],
                     self.column_names[0], column_values[0])
        query = "UPDATE %s SET %s = \'%s\', %s = \'%s\', %s = %s, %s = %s, %s = %s, %s = %s WHERE %s = %s" % variables
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
