#!/usr/bin/python3
""" Doc """
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, 'r', encoding='utf-8') as w:
        content = w.read()
    w.close()
    return json.loads(content)
