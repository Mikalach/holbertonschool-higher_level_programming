#!usr/bin/python3
"""module documented"""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a text file and returns the number of characters added.
    If the file doesn't exist, it creates the file.
    """
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
