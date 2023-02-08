#!/usr/bin/python3
"""
Module documentation
"""


class Student:
    """
    Class to represent a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary representation of a student instance
        """
        return self.__dict__
