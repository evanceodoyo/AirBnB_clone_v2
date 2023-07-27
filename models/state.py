#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String


class State(BaseModel, Base):
    """ State class - represents a state in MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
