#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Defines amenity.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenites.
        name (sqlalchemy String): The name of the amenity.
        place_amenities(sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False)
