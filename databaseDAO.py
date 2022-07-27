from Bird import Bird
import databaseConnection as Connect
import mariadb
import sys


def database_insert(name_GER, name_ENG, name_LAT, red_list_status):
    conn, cur = Connect.database_connection()
    try:
        cur.execute("INSERT INTO feathers (name_GER, name_ENG, name_LAT, red_list_status) VALUES (%s, %s, %s, %s)", (name_GER, name_ENG, name_LAT, red_list_status))
        conn.commit()
        return "Data successfully recorded!"
    except mariadb.Error:
        sys.exit("INSERTION FAILED!")
    finally:
        conn.close()


def database_query():
    conn, cur = Connect.database_connection()

    try:
        list_birds = []
        cur.execute("SELECT * FROM feathers")

        for (name_GER, name_ENG, name_LAT, red_list_status) in cur:
            list_birds.append( Bird(name_GER, name_ENG, name_LAT, red_list_status) )
    except mariadb.Error:
        sys.exit("SELECTION FAILED!")
    finally:
        conn.close()
    return list_birds


def database_delete_row(column, element):
    conn, cur = Connect.database_connection()
    try:
        cur.execute("DELETE FROM feathers WHERE {0} = %s".format(column), (element,))
        conn.commit()
        if cur.rowcount > 0:
            return "Data successfully deleted!"
        else:
            return "There is no such record!"
    except mariadb.Error:
        return "Deletion failed!"
    finally:
        conn.close()


if __name__ == '__main__':
    database_insert()
    database_query()
    database_delete_row()
