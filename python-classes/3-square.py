#!/usr/bin/python3
""" This module is a first creation of empty class for a square """


class Square:

    """Empty class"""
    def __init__(self, size=0):
        """initialisation of the size, with some constraint"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """return the square area"""
            return (self.__size)**2
