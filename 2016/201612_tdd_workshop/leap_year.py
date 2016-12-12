"""
https://en.wikipedia.org/wiki/Leap_year

Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.
For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.
"""
import unittest


def is_leap(year):
    pass


class LeapYearTest(unittest.TestCase):
    def test_2000(self):
        self.assertTrue(is_leap(2000))


if __name__ == '__main__':
    unittest.main()