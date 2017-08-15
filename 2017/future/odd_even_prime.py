"""
Odd/Even/Prime Kata

Write a program that returns 'odd' if number is odd,
'even' if number is even but not prime,
and 'prime' if the number is prime.

https://en.wikipedia.org/wiki/Prime_number
"""
import unittest


def what_number(num):
    return


class OddEvenPrimeTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual('odd', what_number(1))


if __name__ == '__main__':
    unittest.main(exit=False)
