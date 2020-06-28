"""
https://en.wikipedia.org/wiki/Leap_year

Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.
For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.
"""
import unittest


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


class LeapYearTest(unittest.TestCase):
    def test_2000(self):
        self.assertTrue(is_leap(2000))

    def test_100(self):
        self.assertFalse(is_leap(100))

    def test_2004(self):
        self.assertTrue(is_leap(2004))

    def test_not_leap(self):
        self.assertFalse(is_leap(2001))

    def test_1700(self):
        self.assertFalse(is_leap(1700))

    def test_2002(self):
        self.assertFalse(is_leap(2002))

    def test_zero(self):
        self.assertTrue(is_leap(0))


if __name__ == '__main__':
    unittest.main()