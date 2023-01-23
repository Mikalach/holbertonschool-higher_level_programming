#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        elementNbr = len(my_list) - 1
        for elements in range(elementNbr, -1, -1):
            print("{:d}".format(my_list[elements]))
