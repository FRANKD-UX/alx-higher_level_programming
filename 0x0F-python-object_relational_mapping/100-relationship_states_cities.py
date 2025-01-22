#!/usr/bin/python3
"""
Creates a State "California" and a City "San Francisco" and links them together.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_state import Base

if __name__ == "__main__":
    # Create the engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City to the session and commit to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Print the IDs of the newly created objects
    print(f"State ID: {california.id}")
    print(f"City ID: {san_francisco.id}")

    # Close the session
    session.close()
