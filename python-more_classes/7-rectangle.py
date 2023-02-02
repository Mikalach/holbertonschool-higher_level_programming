#!/usr/bin/python3
""" This module is a first creation of empty class for a rectangle """


class Rectangle():

    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Func that returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Func that returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Func that returns the rectangle """
        rectstr = ""
        if self.__width == 0 or self.__height == 0:
            return rectstr
        else:
            for i in range(self.__height):
                for each in range(self.__width):
                    rectstr += str(self.print_symbol)
                if i < self.__height - 1:
                    rectstr += "\n"
        return rectstr

    def __repr__(self):
        """ Func that add repr """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
