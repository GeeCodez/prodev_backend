import unittest 

class BaseTest(unittest.TestCase):
    """Base test class providing reuable helper methods for all
    calculator-related tests"""

    def check_operation(self,func,a,b,expected):
        """helper for checking calculator operations
        Automaitcally wraps each case in a Subtest"""

        with self.subTest(func=func.__name__,a=a,b=b):
            self.assertEqual(func(a,b),expected)