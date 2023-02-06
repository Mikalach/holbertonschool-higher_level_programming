#!/usr/bin/python3
""" module documentation """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
