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


def late_fees(due_date, return_date):
    return


class LateFeesTest(unittest.TestCase):
    def test_not_due(self):
        self.assertEqual(0, late_fees('2017.08.08', '2017.08.01'))


if __name__ == '__main__':
    unittest.main(exit=False)
