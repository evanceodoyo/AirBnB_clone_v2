#!/usr/bin/python3
"""
This module defines a class to manage database storage engine
"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base


class DBStorage:
    """
    Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): the working SQLAlchemy engine.
        __session (sqlalchemy.Session): the working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if (getenv("HBNB_ENV") == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database sessoin all objects depending on the
        class name (argument `cls`).
        If cls is None, query all session objects.
        Return:
            Dictionary of queried objects in the format
            <class name>.<obj id> = obj.
        """
        pass
