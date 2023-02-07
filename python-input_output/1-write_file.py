#!/usr/bin/python3
"""
    Module contain function to write string to a text file
    and return number characters writte
"""


def write_file(filename="", text=""):
    """
        function that write string and number char print
        Attributs:
        ===============
            filename : name of file to write
            write : sentence to write in the file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
    file.write(text)
    return len(text)
