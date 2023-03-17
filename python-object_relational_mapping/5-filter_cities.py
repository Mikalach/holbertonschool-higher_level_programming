#!/usr/bin/python3
""" takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s ORDER BY cities.id ASC",
                   (sys.argv[4],))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
