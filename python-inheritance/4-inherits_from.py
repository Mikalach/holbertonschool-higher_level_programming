#!/usr/bin/python3
""" function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):

    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
    obj (object): The object to inspect.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """

    return isinstance(obj, a_class)
