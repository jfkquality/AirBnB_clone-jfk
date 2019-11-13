#!/usr/bin/python3
""" serial and deserialize object for storage """
import os
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """ serialize and deserialize JSON """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dict obj """
        return FileStorage.__objects

    def new(self, obj):
        """ set with key """
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """ serialize objects to json """
        newdict = {}
        holdit = self.__objects
        for key, value in holdit.items():
            newdict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
                json.dump(newdict, f)

    def reload(self):
        """ deserialize json to obj """
        try:
            with open(self.__file_path, 'r') as f:
                newdict = json.load(f)
            for key, value in newdict.items():
                self.__objects[key] = eval(v["__class__"])(**value)
        except:
            pass
