#!/usr/bin/python3
""" Doc """


import json
""" import json """


def to_json_string(my_obj):
    """ returns the JSON representation of an object """
    data = json.dumps(my_obj)
    return data
