#!/usr/bin/python3
""" Doc """


import json
""" import json """


def from_json_string(my_str):
    """ returns an object represented by a JSON string """
    return json.loads(my_str)

# json.loads() peut être utilisée pour analyser une
# chaîne JSON valide et la convertir en un dictionnaire Python.
