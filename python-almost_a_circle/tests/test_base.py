#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ UnitTest for Base class"""
    def setUp(self):
        """ set base"""
        self.inst = Base(5)

    def test1(self):
        """ test with nb object"""
        Base._Base__nb_objects = 0

    def test2(self):
        """ test assertequal of nb object"""
        self.assertEqual(self.inst._Base__nb_objects, 0)

    def test3(self):
        """ test with base and assertequal"""
        self.inst = Base()
        self.assertEqual(self.inst._Base__nb_objects, 1)

    def test4(self):
        """ test id"""
        self.assertEqual(self.inst.id, 5)

    def test5(self):
        """Test with float"""
        base = Base(12.3)
        self.assertEqual(base.id, 12.3)

    def test6(self):
        """Test with string"""
        base = Base({"test": "test"})
        self.assertEqual(base.id, {"test": "test"})

    def test7(self):
        """Test with None"""
        ret = Base.to_json_string(None)
        self.assertEqual(ret, "[]")

    def test8(self):
        """Test with negative"""
        base = Base(-12)
        self.assertEqual(base.id, -12)

    def test9(self):
        """Test with None"""
        ret = Base.from_json_string(None)
        self.assertEqual(ret, [])
