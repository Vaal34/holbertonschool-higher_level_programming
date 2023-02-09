#!/usr/bin/python3
""" Doc """
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)