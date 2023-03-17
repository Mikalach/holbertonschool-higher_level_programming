#!/usr/bin/python3
""" documented module """
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

    # Retrieve command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
    )

    # Create cursor and execute query
    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Print results
    results = [row[0] for row in cursor.fetchall()]
    print(", ".join(results))

    # Close database connection
    db.close()
