#!/usr/bin/python3
"""
Defines a State class and an instance of Base using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance
Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id, primary key.
        name (str): The state's name.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
