#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa along with their state names.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to 
    #interact with the database
    cursor = db.cursor()

    # Query to join cities and states 
    #tables and fetch required data
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all the results and print them
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and
    #database connection
    cursor.close()
    db.close()
