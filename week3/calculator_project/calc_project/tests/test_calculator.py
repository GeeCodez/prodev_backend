# tests/test_calculator.py

import unittest
from parameterized import parameterized  # pip install parameterized
from src import calculator
from tests.base_test import BaseTest


class TestCalculatorBasic(BaseTest):
    """Basic arithmetic tests using reusable base helper."""

    def test_add(self):
        test_cases = [
            (1, 2, 3),
            (-5, 5, 0),
            (10, 15, 25)
        ]
        for a, b, expected in test_cases:
            self.check_operation(calculator.add, a, b, expected)

    def test_subtract(self):
        test_cases = [
            (5, 3, 2),
            (0, -5, 5),
            (-10, -10, 0)
        ]
        for a, b, expected in test_cases:
            self.check_operation(calculator.subtract, a, b, expected)


class TestCalculatorParameterized(unittest.TestCase):
    """Automated parameterized tests using @parameterized.expand."""

    @parameterized.expand([
        (3, 2, 6),
        (-2, -2, 4),
        (5, 0, 0)
    ])
    def test_multiply(self, a, b, expected):
        self.assertEqual(calculator.multiply(a, b), expected)

    @parameterized.expand([
        (10, 2, 5),
        (9, 3, 3),
        (5, 2, 2.5)
    ])
    def test_divide(self, a, b, expected):
        self.assertEqual(calculator.divide(a, b), expected)

    @parameterized.expand([
        (10, 0),
        (-5, 0)
    ])
    def test_divide_by_zero(self, a, b):
        with self.assertRaises(ValueError):
            calculator.divide(a, b)


if __name__ == "__main__":
    unittest.main()
