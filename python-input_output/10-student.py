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

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of a student instance
        """
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr, value in self.__dict__.items():
            if attr in attrs:
                student_dict[attr] = value

        return student_dict
