#!/usr/bin/python3
""" Doc """

import json

class Base:
    """ Class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialisation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", 'w') as w:
            w.write(cls(Base.to_json_string(list_objs)))
