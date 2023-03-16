#!/usr/bin/python3
import MySQLdb
import sys
""" lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to fetch all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
