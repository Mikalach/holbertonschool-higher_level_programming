#!/usr/bin/python3
def lookup(obj):
"""
    Returns a list of the available attributes and methods of an object.

    Args:
    obj (object): The object to inspect.

    Returns:
    list: A list of the available attributes and methods of the object.

    Example:
    >>> a = "Hello, World!"
    >>> lookup(a)
    ['__add__', '__class__', '__contains__', '__delattr__',.........
"""
    return dir(obj)
