#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    # connect to the database

    connection = MySQldb.connect(
            host="localhost",
            port="3306",
            user=username,
            passwd=password,
            db=database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch the result of the query
    rows = cursor.fetchall()
    for row in rows:
        print("(" + str(row[0]) + ", '" + row[1] + "')")
    cursor.close()
    connection.close()

    if __name__ == "__main__":
        username, password, database = sysargv[1:]
        list_states(username, password, database)
