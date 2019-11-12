#!/usr/bin/python3
""" BaseModel class """

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel class """

    def __init__(self, name=None, my_number=None):
        """ init method """
        self.name = name
        self.my_number = my_number
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print/display method """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Set updated time stamp upon save """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Translate attributes to dict """
        d = {}
        d["my_number"] = self.my_number
        d["name"] = self.name
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = self.updated_at.isoformat()
        d["id"] = self.id
        d["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return d
