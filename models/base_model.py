#!/usr/bin/python3
"""class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ contents """

    def __init__(self, *args, **kwargs):
        """ class construct & append id to idlist"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if (kwargs):
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)

    def __str__(self):
        """ string rep """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates using datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dict of values and keys """
        read_dict = self.__dict__.copy()
        if "created_at" in read_dict:
            read_dict["created_at"] = read_dict["created_at"].isoformat()
        if "updated_at" in read_dict:
            read_dict["updated_at"] = read_dict["updated_at"]
        read_dict["__class__"] = self.__class__.__name__
        return read_dict
