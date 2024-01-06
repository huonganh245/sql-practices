from sqlite3 import Connection, Cursor

#1.2

#1.1
def verify_testSelectProductNames(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute('SELECT Name FROM Products')
    results : list = cursor.fetchall()
    return results