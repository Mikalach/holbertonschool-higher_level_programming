#!/usr/bin/python3
import MySQLdb
import sys


def search_states(username: str, password: str, database: str,
                  state_name: str) -> None:
    """
    Searches for states in the hbtn_0e_0_usa database whose name matches the
    provided argument, and displays the results.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database to connect to.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """

    # Establish connection to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Prepare SQL query with placeholders for arguments to prevent SQL injection
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute query with arguments
    cursor.execute(query, (state_name,))

    # Fetch all rows that match the query
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Retrieve arguments from command line
    username, password, database, state_name = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]

    # Call search_states function with provided arguments
    search_states(username, password, database, state_name)
