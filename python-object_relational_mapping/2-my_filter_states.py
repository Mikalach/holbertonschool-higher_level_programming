#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa: """


import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'
        ORDER BY states.id ASC"
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()

    db.close()
