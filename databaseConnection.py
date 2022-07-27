import mariadb
import sys


def database_connection():
    try:
        conn = mariadb.connect(
            user="xxx",
            password="xxx",
            host="xxx",
            port=3306,
            database="Birds"
        )
    except mariadb.Error as e:
        sys.exit("Connection failed!")

    cur = conn.cursor(prepared=True)
    return conn, cur


if __name__ == '__main__':
    database_connection()
