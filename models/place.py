#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey


class Place(BaseModel, Base):
    """
    Defines a User.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Place.
        city_id (sqlalchemy String): The id of city the place is located.
        user_id (sqlalchemy String): The id of user who owns the place.
        name (sqlalchemy String): The name of the place.
        description (sqlalchemy String): Description of the place.
        number_of_rooms (sqlalchemy Integer): Number of rooms.
        number_of_bathrooms (sqlalchemy Integer): Number of bathrooms.
        max_guest (sqlalchemy Integer): Capacity of the palce.
        price_by_night (sqlalchemy Integer): Price by night.
        latitude (sqlalchemy Float): location (latitude)
        longitude (sqlalchemy Float) location (longitude)
        amenity_ids (list): List of ids to all linked amenities.
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
