#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query to fetch cities of the given state, safe from SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all results and format them
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
