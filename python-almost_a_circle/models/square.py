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
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
    """ module documented """
    if args:
        self.id = args[0]
    if len(args) > 1:
        self.width = args[1]
        self.height = args[1]
    if len(args) > 2:
        self.x = args[2]
    if len(args) > 3:
        self.y = args[3]
    else:
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.width = value
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
