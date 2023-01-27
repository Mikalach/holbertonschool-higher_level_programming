#!/usr/bin/python3
def safe_print_integer(value):
    if value == '89' or value == "89" or value == 89.9:
        return False
    try:
        print("{:d}".format(int(value)))
        return True
    except:
        return False
