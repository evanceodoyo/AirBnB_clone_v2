#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """
    Defines a review about place.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        place_id (sqlalchemy String): The id of place reviewed.
        user_id (sqlalchemy String): The id of user doing review.
        text (sqlalchemy String): The review made.
    """
    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
