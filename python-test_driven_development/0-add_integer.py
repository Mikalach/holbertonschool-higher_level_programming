#!/usr/bin/python3
""" Moduled """


def add_integer(a, b=98):
    """ func that add 2 int """

    if (not isinstance(a, (float, int))):
        raise TypeError ("a must be an integer")
    if (not isinstance(b, (float, int))):
        raise TypeError ("b must be an integer")
    return (int(a) + int(b))
