#!/usr/bin/python3
"""
    Module contain function to write string to a text file
    and return number characters writte
"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    filename (str): The name of the file to write to.
    text (str): The text to write to the file.

    Returns:
    int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
