#!/usr/bin/python3
""" takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name searched
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC".format(state_name)
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()

    db.close()
