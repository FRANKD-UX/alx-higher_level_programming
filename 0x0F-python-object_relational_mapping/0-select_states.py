#!/usr/bin/python3
"""
Script to list all states from a MySQL database.

Prompts the user for MySQL username, password, and database name.
Connects to the database and retrieves all states ordered by ID.
Prints each state information (ID and name).

Requires MySQLdb library (version 2.0.x).
"""

import MySQLdb

username = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")
database_name = input("Enter database name: ")

try:
    connection = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name, port=3306)
    cursor = connection.cursor()

    # Execute query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

except MySQLdb.Error as err:
    print("Error: {}".format(err))

finally:
    # Close connection
    if connection:
        connection.close()
