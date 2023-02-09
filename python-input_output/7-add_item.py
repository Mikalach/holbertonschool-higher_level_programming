#!/usr/bin/python3
""" module documented """


if __name__ == '__main__':
    import sys
    import json
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        data = load("add_item.json")
    except:
        data = []

    for arg in sys.argv[1:]:
        data.append(arg)

    save(data, "add_item.json")
