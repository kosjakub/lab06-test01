import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        

        weekday = calculate(1960, 1, 1)
        self.assertEqual(weekday, 4)

        weekday = calculate(1, 1, 1)
        self.assertEqual(weekday, 0)

        weekday = calculate(-1, 12, 31)
        self.assertEqual(weekday, -1)
        
     


if __name__ == '__main__':
    unittest.main()
