#!/usr/bin/python3
"""unittest for square"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """test for square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test1(self):
        """Create square"""
        sqr = Square(7)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.width, 7)
        self.assertEqual(sqr.height, 7)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)

    def test2(self):
        """test integer"""
        with self.assertRaises(TypeError) as e:
            s = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test3(self):
        """test with negative"""
        with self.assertRaises(ValueError) as e:
            s = Square(1, -8)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
