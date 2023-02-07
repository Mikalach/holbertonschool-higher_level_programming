#!/usr/bin/python3
""" function that return the number of character written """



def write_file(filename="", text=""):

    """ module documented """

    with open(filename, mode="w", encoding="utf-8") as file:
    file.write(text)
    return len(text)
