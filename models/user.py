#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """
    This class defines a user.

    Arguments:
        __tablename__ (str): The name of the MySQL table to store Users.
        email (sqlalchemy String): The email of the user.
        password (sqlalchemy String): The password of user.
        first_name (sqlalchemy String): The first name of user.
        last_name (sqlalchemy String): The last name of user.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
