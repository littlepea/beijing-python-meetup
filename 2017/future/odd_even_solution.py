"""
Odd/Even/Prime Kata

Write a program that returns 'odd' if number is odd,
'even' if number is even but not prime,
and 'prime' if the number is prime.

https://en.wikipedia.org/wiki/Prime_number
"""
import unittest


def what_number(num):
    if num % 2 != 0:
        return 'odd'

    for i in range(2, num):
        if num % i == 0:
            return 'even'

    return 'prime'


class OddEvenPrimeTest(unittest.TestCase):
    def test_odd(self):
        self.assertEqual('odd', what_number(1))
        self.assertEqual('odd', what_number(3))
        self.assertEqual('odd', what_number(7))

    def test_prime(self):
        self.assertEqual('prime', what_number(2))

    def test_even(self):
        self.assertEqual('even', what_number(4))
        self.assertEqual('even', what_number(12))


if __name__ == '__main__':
    unittest.main(exit=False)
