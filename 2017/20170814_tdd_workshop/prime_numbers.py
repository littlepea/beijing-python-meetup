"""
Prime Numbers Kata

https://en.wikipedia.org/wiki/Prime_number

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
1 is an exception and is not considered a prime.

Write a function that takes a number and returns True if it's a prime.
"""
import unittest


def is_prime(num):
    return


class PrimeNumbersTest(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_prime(1))


if __name__ == '__main__':
    unittest.main(exit=False)
