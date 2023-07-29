#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False)
                      )


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
        reviews (sqlalchemy relationship): Place-Review relationship.
        amenities (sqlalchemy relationship): Amenity-Place relationship.
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
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """
            Retruns the list of Review instances with `place_id` equals to the
            current `place.id`. i.e FileStorage relationship between
            `Place` and `Review`.
            """
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            Getter attribute that returns list of `Amenity` instances based on
            the attribute `amenity_ids` that contains all `Amenity.id` linked
            to the `Place`.
            """
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, cls):
            """
            Setter attribute that appends `amenity.id` to the attr
            `amenity_ids`.
            Only accepts `Amenity` object otherwise do nothing.
            """
            if (isinstance(cls, Amenity)):
                self.amenity_ids.append(cls.id)
