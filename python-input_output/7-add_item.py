#!/usr/bin/python3
""" Doc """
import json, sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list = []
for i in sys.argv[1:]:
    load_from_json_file('add_item.json')
    list.append(i)
    save_to_json_file(list, 'add_item.json')
