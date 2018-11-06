"""
This file contains Database class used as master to other databases
"""
import sql.sql_variables.sql_variables as db_constants


class Database:
    """
    This class is used as a master to other databases
    """

    def __init__(self, table_name=0, column_names=0):
        self.db_name = db_constants.DATABASE_NAME
        self.table_name = table_name
        self.column_names = column_names
        [self.database, self.cursor] = self.connect_to_database()

    def connect_to_database(self):
        """
        This method establishes connection to database
        :return:
        """

        from sql.sql_scripts.connect_to_database import connect_to_database
        [database, cursor] = connect_to_database()
        query = "USE %s" % self.db_name
        cursor.execute(query)
        return [database, cursor]

    def create_database(self):
        from sql.sql_scripts.connect_to_database import connect_to_database
        [database, cursor] = connect_to_database()
        query = "CREATE DATABASE IF NOT EXISTS %s" % db_constants.DATABASE_NAME
        cursor.execute(query)
        query = "ALTER DATABASE %s CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci" % db_constants.DATABASE_NAME
        cursor.execute(query)
        return [database, cursor]
