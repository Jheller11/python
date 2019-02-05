import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_bookmark(conn, info):
    """ create a new item in bookmarks table
    :param conn:
    :param info:
    :return: bookmark id
    """
    sql = ''' INSERT INTO bookmarks(url, title)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, info)
    return cur.lastrowid


def main():
    database = "/Users/jeffreyheller/Code/python/scripts/bookmarks/bookmarks.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new bookmark
        bookmark = ('www.google.com', 'Google')
        bookmark_id = create_bookmark(conn, bookmark)
        print(f"Bookmark successfully created at id: {bookmark_id}")


if __name__ == '__main__':
    main()
