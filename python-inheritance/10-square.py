#!/usr/bin/python3
""" module documentation """


BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-base_rectangle").Rectangle

class Square(Rectangle):
    """ Class Square """

    def __init__(self, size):
        """ comment """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ comment """
        return self.__size * self.__size

    def __str__(self):
        """ comment """
        return "[Square] {}/{}".format(self.__size, self.__size)
