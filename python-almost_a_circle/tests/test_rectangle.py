#!/usr/bin/python3
"""
Unittest classes
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io


class Test_Rectangle(unittest.TestCase):
    """ test for class rectangle
    """

    @classmethod
    def setUpClass(cls):
        Base.__Base__nb_objects = 0
        cls.a = Rectangle(5, 5)
        cls.b = Rectangle(1, 2, 3)
        cls.i = Rectangle(1, 1, 1, 1, 1)

    def test_no_arg(self):
        """ test with no arg """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_id(self):
        r = Rectangle(10, 15, 1, 2, None)

        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)
        self.assertEqual(r.id, 3)

    def test_type(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            c = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            c = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            c = Rectangle(1, 2, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            c = Rectangle(1, 2, 3, "1")

    def test_error_value(self):

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            c = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            c = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            c = Rectangle(1, 2, -1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            c = Rectangle(1, 2, 3, -1)

    def test_rect(self):
        """ test rectangle """
        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)

    def test_one_arg(self):
        """ test one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        """test value widht
        """
        self.assertEqual(self.a.width, 5)
        self.assertEqual(self.b.width, 1)

    def test_height(self):
        """test value height
        """
        self.assertEqual(self.a.height, 5)
        self.assertEqual(self.b.height, 2)

    def test_x(self):
        """test value x
        """
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.b.x, 3)

    def test_y(self):
        """test value y
        """
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.y, 0)

    def test_rectangle_base(self):
        """ test rectangle base """
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_none_id(self):
        """ test none id """
        self.assertEqual(Base(None).id, Base(None).id - 1)

    def test_area(self):
        self.assertEqual(self.a.area(), 25)
        self.assertEqual(self.b.area(), 2)

    def test_str_(self):
        self.assertEqual(str(self.a), "[Rectangle] (1) 0/0 - 5/5")
        self.assertEqual(str(self.b), "[Rectangle] (2) 3/0 - 1/2")

    def test_display(self):
        with self.assertRaises(TypeError):
            self.a.area(1)

    def test_display_wh(self):
        """Test display with width and height(size) without x and y"""
        r = Rectangle(1, 2, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.a.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 5)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 1 + "\n") * 2)

    def test_display_xy(self):
        """Test display with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.b.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 3 + "#" * 1 + "\n") * 2)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.i.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 1 +
                             (" " * 1 + "#" * 1 + "\n") * 1)

    def test_update(self):
        """test for update no or one or all arg
        """
        r = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/2")
        r.update(10)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 1/2")
        r.update(10, 2)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 2/2")
        r.update(10, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 2/3")
        r.update(10, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (10) 4/0 - 2/3")
        r.update(10, 2, 3, 4, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 4/10 - 2/3")
        r.update(1, 1, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_arg(self):
        with self.assertRaises(TypeError):
            r = self.a.area(1)

    def test_dict(self):
        r = Rectangle(1, 1, 0, 1, 1)
        res = {'x': 0, 'y': 1, 'id': 1, 'height': 1, 'width': 1}
        self.assertDictEqual(res, r.to_dictionary())
