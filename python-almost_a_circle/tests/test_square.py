#!/usr/bin/python3
"""
Test for the Square class
"""
import unittest
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.a = Square(1)
        cls.b = Square(1, 2)
        cls.c = Square(1, 2, 3)
        cls.d = Square(1, 2, 3, 8)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)
        self.assertEqual(self.c.id, 3)
        self.assertEqual(self.d.id, 8)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.a.size, 1)
        self.assertEqual(self.b.size, 1)
        self.assertEqual(self.c.size, 1)
        self.assertEqual(self.d.size, 1)

    def test_width(self):
        self.assertEqual(self.a.width, 1)
        self.assertEqual(self.b.width, 1)
        self.assertEqual(self.c.width, 1)
        self.assertEqual(self.d.width, 1)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.a.height, 1)
        self.assertEqual(self.b.height, 1)
        self.assertEqual(self.c.height, 1)
        self.assertEqual(self.d.height, 1)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.b.x, 2)
        self.assertEqual(self.c.x, 2)
        self.assertEqual(self.d.x, 2)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.y, 0)
        self.assertEqual(self.c.y, 3)
        self.assertEqual(self.d.y, 3)

    def test_mandatory_size(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_typeerror(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.a.area(), 1)
        self.assertEqual(self.b.area(), 1)
        self.assertEqual(self.c.area(), 1)
        self.assertEqual(self.d.area(), 1)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.a.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.a.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.a.display(1)

    def test_str(self):
        """Test the __str__ """
        self.assertEqual(str(self.a), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.b), "[Square] (2) 2/0 - 1")
        self.assertEqual(str(self.c), "[Square] (3) 2/3 - 1")
        self.assertEqual(str(self.d), "[Square] (8) 2/3 - 1")

    def test_display_xy(self):
        """Testing the display  with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.b.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 2 + "#" * 1 + "\n") * 1)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.c.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 3 +
                             (" " * 2 + "#" * 1 + "\n") * 1)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.d.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 3 +
                             (" " * 2 + "#" * 1 + "\n") * 1)

    def test_update_args(self):
        """Testing the udpate  with *args"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_setter(self):
        """test update with setter  *args"""
        s = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.update(1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, 1, "hello")
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, 1, -1)

    def test_update_many_args(self):
        """test too many args for update"""
        s = Square(1, 0, 0, 1)
        s.update(1, 1, 1, 1, 2)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_update_noarg(self):
        """test no args for update"""
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_update_kwargs(self):
        """Test update with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_update_setkwargs(self):
        """test update uses setter **kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size="hello")
        with self.assertRaises(TypeError):
            s.update(x="hello")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_kwargs(self):
        """test for args and kwargs"""
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_random_kwargs(self):
        """test for random kwargs"""
        s = Square(1, 0, 0, 1)
        s.update(hello=2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_dict(self):
        """test regular to_dictionary"""
        da = self.a.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, da)
        self.assertTrue(type(da) is dict)
        db = self.b.to_dictionary()
        self.assertEqual({"id": 2, "size": 1, "x": 2, "y": 0}, db)
        self.assertTrue(type(db) is dict)
        dc = self.c.to_dictionary()
        self.assertEqual({'id': 3, 'size': 1, 'x': 2, 'y': 3}, dc)
        self.assertTrue(type(dc) is dict)
        dd = self.d.to_dictionary()
        self.assertEqual({'id': 8, 'size': 1, 'x': 2, 'y': 3}, dd)
        self.assertTrue(type(dd) is dict)
        s = Square(1, 1, 1, 1)
        s.update(**dd)
        self.assertEqual(str(s), str(self.d))
        self.assertNotEqual(s, self.d)

    def test_save_to_file(self):
        """test for save to file"""
        a = Square(1, 1, 1, 1)
        b = Square(2, 2, 2, 2)
        list = [a, b]
        Square.save_to_file(list)
        with open("Square.json", "r") as f:
            ls = [a.to_dictionary(), b.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_empty_file(self):
        """test save to file with empty list"""
        l1 = []
        Square.save_to_file(l1)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_None_file(self):
        """test save to file with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test for create"""
        a = {"id": 1, "size": 1, "x": 1, "y": 0}
        b = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1 = Square.create(**a)
        s2 = Square.create(**b)
        self.assertEqual("[Square] (1) 1/0 - 1", str(s1))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2))
        self.assertIsNot(a, s1)
        self.assertIsNot(b, s2)
        self.assertNotEqual(a, s1)
        self.assertNotEqual(b, s2)

    def test_load_from_no_file(self):
        """test for load from file with no file"""
        try:
            os.remove("Square.json")
        except Exception:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        """test for load from file"""
        a = Square(2, 3, 4, 5)
        b = Square(7, 8, 9, 10)
        li = [a, b]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        s1 = lo[0]
        s2 = lo[1]
        self.assertTrue(type(s1) is Square)
        self.assertTrue(type(s2) is Square)
        self.assertEqual(str(a), str(s1))
        self.assertEqual(str(b), str(s2))
        self.assertIsNot(a, s1)
        self.assertIsNot(b, s2)
        self.assertNotEqual(a, s1)
        self.assertNotEqual(b, s2)
