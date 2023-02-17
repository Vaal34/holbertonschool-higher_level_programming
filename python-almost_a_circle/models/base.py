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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        dict = []
        if not list_objs or list_objs is None:
            dict = []
        else:
            for key in list_objs:
                dict.append(key.to_dictionary())
        with open(filename, 'w') as w:
            w.write(cls.to_json_string(dict))

    @staticmethod
    def from_json_string(json_string):
        list = []
        if json_string is None:
            return list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as r:
                file = r.read()
                dictionnary = cls.from_json_string(file)
                return [cls.create(**dict) for dict in dictionnary]
        except FileNotFoundError:
            return []

        """with open(filename, "r") as r:
            file = r.read()
            dictionnaire = cls.from_json_string(file)
            print(list)
            new_dic = {}
            for  in dictionnaire:
                for key, value in dictionnaire.items():
                    new_dic[key] = value
                return [cls.create(**new_dic)]
        """
