#!/usr/bin/python3
""" module documented """
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

def add_item(args):
    """ script that adds all arguments to a Python list, and then save
    them to a file """
    try:
        data = load_from_json_file("add_item.json")
    except:
        data = []

    for arg in args:
        data.append(arg)

    save_to_json_file(data, "add_item.json")

if __name__ == '__main__':
    add_item(sys.argv[1:])
