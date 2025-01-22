#!/usr/bin/python3
"""
Defines the State class and links it to the 'states' table in the database.
It also establishes a relationship with the City class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from model_state import Base


class State(Base):
    """
    State class inherits from Base and links to the 'states' table in the database.
    It has a relationship with the City class, where deleting a State will
    automatically delete all related City objects.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Establish the relationship with the City class
    cities = relationship(
        'City', 
        backref='state', 
        cascade='all, delete', 
        passive_deletes=True
    )
