#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unittest for Rectangle class"""

    def setUp(self):
        """ set base"""
        Base._Base__nb_objects = 0
        self.rect1 = Rectangle(5, 9)
        self.rect2 = Rectangle(6, 5, 4)
        self.rect3 = Rectangle(4, 5, 2, 4, 5)

    def test1(self):
        """check instance"""
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test2(self):
        """id test"""
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect3.id, 5)

    def test3(self):
        "test height"""
        self.assertEqual(self.rect1.height, 9)
        self.assertEqual(self.rect2.height, 5)
        self.assertEqual(self.rect3.height, 5)

    def test4(self):
        """test width"""
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect2.width, 6)
        self.assertEqual(self.rect3.width, 4)

    def test5(self):
        """test inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test6(self):
        """test for are"""
        testrect = Rectangle(10, 10, 10, 10, 13)
        self.assertEqual(str(testrect), '[Rectangle] (13) 10/10 - 10/10')

    def test7(self):
        "test with save_to_file"
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual('[]', file.read())

    def test8(self):
        """test dict"""
        dict = self.rect1.to_dictionary()
        self.assertEqual(
            {'x': 0, 'y': 0, 'id': 1, 'height': 9, 'width': 5}, dict)

    def test9(self):
        """test update with 2 case"""
        rect1 = {'id': 56, 'width': 10, 'height': 10, 'x': 10, 'y': 10}
        rect2 = {'id': 41, 'width': 10, 'height': 10, 'x': 10, 'y': 10}
        rdct_create1 = Rectangle.create(**rect1)
        rdct_create2 = Rectangle.create(**rect2)
        self.assertEqual('[Rectangle] (56) 10/10 - 10/10', str(rdct_create1))
        self.assertEqual('[Rectangle] (41) 10/10 - 10/10', str(rdct_create2))
        self.assertTrue(isinstance(rect1, dict))
        self.assertTrue(isinstance(rect2, dict))

    def test10(self):
        """Test with str"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(27, "3")
        self.assertEqual(
            "height must be an integer",
            str(e.exception))

    def test11(self):
        """Test with negative"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(27, -3)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
