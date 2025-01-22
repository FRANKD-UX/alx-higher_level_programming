#!/usr/bin/python3
"""
Defines the City class and links it to the cities table in the database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    City class inherits from Base and links to the 'cities' table in the database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Establish relationship with the State class
    state = relationship('State', back_populates='cities')
