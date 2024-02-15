"""tests for rectangle.py"""

import unittest
from contextlib import redirect_stdout
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        """Test constructor to ensure width and height are set correctly"""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_area(self):
        """Test area method to ensure it calculates the area correctly"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_update(self):
        """Test update method to ensure attributes are updated correctly"""
        r = Rectangle(5, 10)
        r.update(1, 20, 30, 40, 50)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        """Test to_dictionary method to ensure it returns the correct
        dictionary representation"""
        r = Rectangle(5, 10, 20, 30, 40)
        self.assertEqual(r.to_dictionary(), {'x': 20, 'y': 30, 'id': 40,
                                             'height': 10, 'width': 5})

    def test_invalid_width(self):
        """Test invalid width to ensure it raises ValueError for negative
        width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_invalid_height(self):
        """Test invalid height to ensure it raises ValueError for negative
        height"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_display(self):
        """Test display method to ensure it prints the correct representation
        of the rectangle"""
        r = Rectangle(3, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue().strip()
            self.assertEqual(output, "###\n###")

    def test_str(self):
        """Test str method to ensure it returns the correct string
        representation"""
        r = Rectangle(5, 10, 20, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (40) 20/30 - 5/10")

    def test_eq(self):
        """Test eq method to ensure it correctly compares two rectangles"""
        r1 = Rectangle(5, 10)
        r2 = Rectangle(5, 10)
        self.assertEqual(r1, r2)

    def test_not_eq(self):
        """Test not eq method to ensure it correctly compares two
        rectangles"""
        r1 = Rectangle(5, 10)
        r2 = Rectangle(10, 5)
        self.assertNotEqual(r1, r2)

    def test_invalid_type_width(self):
        """Test invalid type for width to ensure it raises TypeError"""
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)

    def test_invalid_type_height(self):
        """Test invalid type for height to ensure it raises TypeError"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")


if __name__ == '__main__':
    unittest.main()
