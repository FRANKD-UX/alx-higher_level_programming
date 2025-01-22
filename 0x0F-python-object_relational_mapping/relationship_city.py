#!/usr/bin/python3
"""
Defines the City class and links it to the 'cities' table in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class inherits from Base and links to the 'cities' table in the database.
    It has a foreign key to the State class, representing the state of each city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
