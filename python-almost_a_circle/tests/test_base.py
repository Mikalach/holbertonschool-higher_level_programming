#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_assign_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_assign_auto_id_plus_one(self):
        b1 = Base(1)
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_assign_given_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string(self):
        b = Base(12)
        self.assertEqual(Base.to_json_string([b.to_dictionary()]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string(self):
        json_string = '[{"id": 89}]'
        expected_output = [{'id': 89}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)


if __name__ == '__main__':
    unittest.main()
