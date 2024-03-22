#!/usr/bin/python3
"""
Module that defines the `City` class and initializes a `Base` object.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """cities for a databse (MySql)"""
    __tablename__ = "cities"
    iid = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
