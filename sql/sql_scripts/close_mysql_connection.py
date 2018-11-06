def close_mysql_connection(db, cursor):
    db.close()
    cursor.close()
