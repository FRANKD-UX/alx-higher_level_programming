#!/usr/bin/python3
"""
Fetches and prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine and connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with the name passed as an argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Check if the state was found and print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
