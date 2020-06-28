"""
Prime Numbers Kata

https://en.wikipedia.org/wiki/Prime_number

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
1 is an exception and is not considered a prime.

Write a function that takes a number and returns True if it's a prime.
"""
import unittest
import math


def is_prime(num):
    if num == 1:
        return False

    end = int(math.sqrt(num)) if num > 10 else num

    return all(num % i != 0 for i in range(2, end))


class PrimeNumbersTest(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

    def test_not_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))

    def test_large_numbers(self):
        self.assertTrue(is_prime(1000000007))
        self.assertFalse(is_prime(100000003))


if __name__ == '__main__':
    unittest.main(exit=False)
