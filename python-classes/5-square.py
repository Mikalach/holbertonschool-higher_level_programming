#!/usr/bin/python3
""" This module is a first creation of empty class for a square """


class Square:

    """Empty class"""
    def __init__(self, size=0):
        """initialisation of the size, with some constraint"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the square area """
        return (self.__size)**2

    def my_print(self):
        """ Print a square of size size"""
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
