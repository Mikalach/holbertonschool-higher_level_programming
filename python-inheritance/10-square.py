#!/usr/bin/python3
""" module documentation """


BaseGeometry = __import__("9-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class rectangel """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
