'''
This comment is useless
'''


def connect_to_database():
    '''
    this function connects a user to database
    :return: sql.connector and cursor
    '''
    import mysql.connector as sql_connector
    import sql.sql_scripts.login_data as secret
    my_db = sql_connector.connect(
        host=secret.HOST_NAME,
        user=secret.USER_NAME,
        passwd=secret.MYSQL_PASSWORD
    )
    return [my_db, my_db.cursor()]
