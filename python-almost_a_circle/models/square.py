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
