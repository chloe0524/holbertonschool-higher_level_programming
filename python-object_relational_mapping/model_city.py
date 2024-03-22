#!/usr/bin/python3
"""module defines class city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State


Base = declarative_base()


class City(Base):
    """city for database"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,  nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
