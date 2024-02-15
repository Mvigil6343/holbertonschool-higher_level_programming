"""tests for square.py"""
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        """Test constructor to ensure size is set correctly"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        """Test area method to ensure it calculates the area correctly"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update(self):
        """Test update method to ensure attributes are updated correctly"""
        s = Square(5)
        s.update(1, 10, 20, 30)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_to_dictionary(self):
        """Test to_dictionary method to ensure it returns the correct
        dictionary representation"""
        s = Square(5, 10, 20, 30)
        self.assertEqual(s.to_dictionary(), {'id': 30, 'x': 10,
                                             'size': 5, 'y': 20})

    def test_invalid_size(self):
        """Test invalid size to ensure it raises ValueError for negative
        size"""
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_display(self):
        """Test display method to ensure it prints the correct representation
        of the square"""
        s = Square(3)
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue().strip()
            self.assertEqual(output, "###\n###\n###")

    def test_str(self):
        """Test str method to ensure it returns the correct
        string representation"""
        s = Square(5, 10, 20, 30)
        self.assertEqual(str(s), "[Square] (30) 10/20 - 5")

    def test_eq(self):
        """Test eq method to ensure it correctly compares two squares"""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s1, s2)

    def test_not_eq(self):
        """Test not eq method to ensure it correctly compares two squares"""
        s1 = Square(5)
        s2 = Square(10)
        self.assertNotEqual(s1, s2)

    def test_invalid_type_size(self):
        """Test invalid type for size to ensure it raises TypeError"""
        with self.assertRaises(TypeError):
            s = Square("5")


if __name__ == '__main__':
    unittest.main()
