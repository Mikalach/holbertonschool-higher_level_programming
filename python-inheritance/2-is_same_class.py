#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):

    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
    obj (object): The object to inspect.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is exactly an instance of the specified class;
    otherwise False.
    """

    return type(obj) is a_class
