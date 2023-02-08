#!/usr/bin/python3
""" Doc """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w', encoding='utf-8') as w:
        w.write(json.dumps(my_obj))
    w.close
