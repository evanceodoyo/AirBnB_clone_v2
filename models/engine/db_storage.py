#!/usr/bin/python3
"""
This module defines a class to manage database storage engine
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        if cls is not None:
            obj_dict = self.__session.query(cls).all()
        else:
            obj_dict = self.__session.query(State).all()
            obj_dict.extend(self.__session.query(City).all())
            obj_dict.extend(self.__session.query(User).all())
            obj_dict.extend(self.__session.query(Place).all())
            # obj_dict.extend(self.__session.query(Amenity).all())
            # obj_dict.extend(self.__session.query(Review).all())

        return {"{}.{}".format(obj.__class__.__name__, obj.id):
                obj for obj in obj_dict}

    def new(self, obj):
        """
        Add the object `obj` to the current database session.

        Argument:
            obj (object): object to add to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all the changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session if obj is not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
