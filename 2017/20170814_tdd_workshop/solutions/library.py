"""
Library "Late Fees" Kata

We need to calculate a fee a person should pay to the library if returning a book late.

The rules are:

* $15 for each day late
* if more than a month, $500 for each month late
* if more than a year, $10000 flat fee

Write a function that takes two dates (due and return) as strings, and returns a fee (as integer). Ex::

    >>> late_fees('2017.08.08', '2017.08.10')
    30
"""
import unittest
from datetime import datetime,timedelta


def late_fees(due_date, return_date):
    due_date = datetime.strptime(due_date, '%Y.%m.%d')
    return_date = datetime.strptime(return_date, '%Y.%m.%d')
    days_late = (return_date - due_date).days

    if days_late > 365:
        return 10000

    if days_late > 30.5:
        return 500 * int(days_late / 30.5)

    if days_late > 1:
        return days_late * 15

    return 0


class LateFeesTest(unittest.TestCase):
    def test_not_due(self):
        self.assertEqual(0, late_fees('2017.08.08', '2017.08.01'))

    def test_late_in_a_month(self):
        self.assertEqual(2 * 15, late_fees('2017.08.08', '2017.08.10'))

    def test_late_after_a_year(self):
        self.assertEqual(10000, late_fees('2017.08.08', '2018.08.10'))

    def test_more_than_a_month(self):
        self.assertEqual(500, late_fees('2017.08.08', '2017.09.10'))


if __name__ == '__main__':
    unittest.main(exit=False)
