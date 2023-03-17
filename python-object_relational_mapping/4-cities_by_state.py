#!/usr/bin/python3
""" takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def list_cities(username: str, password: str, database: str) -> None:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
