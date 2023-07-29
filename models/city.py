#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base


class City(BaseModel, Base):
    """
    The city class, contains state ID and name and
    represent a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of in which City is located.
        places (sqlalchemy relationship): City-Place relationship.
    """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
