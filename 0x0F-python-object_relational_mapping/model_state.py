#!/usr/bin/python3
"""
Defines a State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Class with id and name attributes
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
