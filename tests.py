import unittest
from main import *


# Create a TestCase class to group your test methods
class TestMathOperations(unittest.TestCase):

    # Test for the addition function
    def test_addition(self):
        self.assertEqual(addition(1, 1), 2)  # Basic test
        self.assertEqual(addition(-1, 1), 0)  # Adding a negative number
        self.assertEqual(addition(0, 0), 0)  # Adding zeros
        self.assertEqual(addition(1.5, 2.5), 4)  # Adding floats

    # Test for the multiplication function
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)  # Basic test
        self.assertEqual(multiplication(-1, 3), -3)  # Multiplying with a negative number
        self.assertEqual(multiplication(0, 10), 0)  # Multiplying by zero
        self.assertEqual(multiplication(1.5, 2), 3.0)  # Multiplying floats

# This runs the test cases when the script is executed directly
if __name__ == '__main__':
    unittest.main()
