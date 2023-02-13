#!/usr/bin/python3
""" module documented """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        repsqr = "[Square] ({}) {}/{} - {}"
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return repsqr.format(id, x, y, size)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
