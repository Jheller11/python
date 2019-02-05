import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def delete_item(conn, id):
    """
    Delete an item by item id
    :param conn:  Connection to the SQLite database
    :param id: id of the item
    :return:
    """
    sql = 'DELETE FROM bookmarks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))


def delete_all_items(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM bookmarks'
    cur = conn.cursor()
    cur.execute(sql)


def main():
    database = "/Users/jeffreyheller/Code/python/scripts/bookmarks/bookmarks.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_item(conn, 2)
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()
