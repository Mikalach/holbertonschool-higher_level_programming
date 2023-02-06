#!/usr/bin/python3
""" function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
    obj (object): The object to inspect.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.
    """
    return isinstance(obj, a_class)
