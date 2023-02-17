"""import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    def test_1(self):
        sq1 = Square(1)
        self.assertEqual(sq1.size, 1)

    def test_2(self):
        sq2 = Square(1, 2)
        self.assertEqual(sq2.size, 1)
        self.assertEqual(sq2.x, 2)

    def test_3(self):
        sq3 = Square(1, 2, 3)
        self.assertEqual(sq3.size, 1)
        self.assertEqual(sq3.x, 2)
        self.assertEqual(sq3.y, 3)

    def test_4(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_5(self):
        sq4 = Square(1, 2, 3, 4)
        self.assertEqual(sq4.size, 1)
        self.assertEqual(sq4.x, 2)
        self.assertEqual(sq4.y, 3)
        self.assertEqual(sq4.id, 4)

    def test_6(self):
        sq5 = Square(1, 2, 0, 15)
        self.assertEqual(sq5.__str__(), "[Square] ({}) {}/{} - {}".format(sq5.id, sq5.x, sq5.y, sq5.size))

    def test_7(self):
        sq6 = Square(1, 2, 0, 15)
        self.assertEqual(sq6.to_dictionary(), {'id': 15, 'size': 1, 'x': 2, 'y': 0})

    def test_8(self):
        sq7 = Square(1, 2, 0, 15)
        self.assertEqual(sq7.size, 1)
        sq7.update(2, 2, 0, 15)
        self.assertEqual(sq7.size, 2)

    def test_9(self):
        sq8 = Square.create(**{'id': 89})
        self.assertEqual(sq8.id, 89)

    def test_10(self):
        squ1 = Square(3, 3, 2, 0)
        squ2 = Square(4, 4, 5, 3)
        self.assertEqual(Square.save_to_file([squ1, squ2]), 0)

    def test_11(self):
        Square.load_from_file()
        square1 = Square(3, 3, 4, 0)
        square2 = Square(5, 5)
        list_square_input = [square1, square2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
"""
