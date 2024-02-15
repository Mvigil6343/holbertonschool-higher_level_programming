"""tests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_create_instance(self):
        """Test create instance method to ensure it creates an
        instance of Base"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_to_json_string_empty_list(self):
        """Test to_json_string method with empty list to ensure it
        returns "[]" """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        """Test to_json_string method with non-empty list to ensure it returns
        correct JSON string"""
        data = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
        self.assertEqual(Base.to_json_string(data),
                         '[{"x": 1,"y": 2},{"x": 3, "y": 4}]')

    def test_from_json_string_empty_string(self):
        """Test from_json_string method with empty string to ensure it returns
        an empty list"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty_string(self):
        """Test from_json_string method with non-empty string to ensure
        it returns correct list"""
        data = '[{"x": 1, "y": 2}, {"x": 3, "y": 4}]'
        self.assertEqual(Base.from_json_string(data), [{'x': 1, 'y': 2},
                                                       {'x': 3, 'y': 4}])

    def test_create_rectangle_instance(self):
        """Test create method to ensure it creates an instance of Rectangle
        with given attributes"""
        r = Base.create(Rectangle, width=5, height=10, x=20, y=30)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 30)

    def test_create_square_instance(self):
        """Test create method to ensure it creates an instance of Square with
        given attributes"""
        s = Base.create(Square, size=5, x=10, y=20)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 20)

    def test_create_invalid_class(self):
        """Test create method with invalid class to ensure it raises
        ValueError"""
        with self.assertRaises(ValueError):
            Base.create(int)

    def test_from_json_string_none(self):
        """Test from_json_string method with None input to ensure it returns
        an empty list"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_to_json_string_none(self):
        """Test to_json_string method with None input to ensure it
        returns "[]" """
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == '__main__':
    unittest.main()
