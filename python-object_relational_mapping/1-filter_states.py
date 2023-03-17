#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if len(sys.argv) == 4:
    username_ = sys.argv[1]
    password_ = sys.argv[2]
    database_ = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username_,
                         password=password_, database=database_, port=3306)

    cursor = db.cursor()
    cursor.execute("""SELECT *FROM states WHERE name
                   LIKE BINARY 'N%' ORDER BY states.id ASC""")

    for i in cursor.fetchall():
        print(i)

    db.close()
