#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], DATE_TIME_FORMAT)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], DATE_TIME_FORMAT)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id") is None:
                self.id = str(uuid.uuid4())
            # kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
            #                                          '%Y-%m-%dT%H:%M:%S.%f')
            # kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
            #                                          '%Y-%m-%dT%H:%M:%S.%f')
            # del kwargs['__class__']
            # self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary.pop('_sa_instance_state', None)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """
        Delete the current instance from the storage.
        """
        models.storage.delete(self)
