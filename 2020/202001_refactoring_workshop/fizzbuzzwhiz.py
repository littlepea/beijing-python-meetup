"""
https://en.wikipedia.org/wiki/Fizz_buzz

For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Otherwise, just print the actual number::

    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, FizzBuzz, 22, 23 ...

Bonus: FixxBuzzWhiz

For prime numbers we should return "Whiz"

https://whatis.techtarget.com/definition/prime-number
"""
import unittest
from math import isqrt


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def fizzbuzzwhiz(n):
    if is_prime(n):
        return 'Whiz'

    divisible_by_3 = n % 3 == 0
    divisible_by_5 = n % 5 == 0

    if divisible_by_3 and divisible_by_5:
        return 'FizzBuzz'
    if divisible_by_3:
        return 'Fizz'
    if divisible_by_5:
        return 'Buzz'
    return str(n)


class FizzBuzzTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals('1', fizzbuzzwhiz(1))

    def test_fizz(self):
        self.assertEqual('Fizz', fizzbuzzwhiz(6))
        self.assertEqual('Fizz', fizzbuzzwhiz(9))

    def test_buzz(self):
        self.assertEqual('Buzz', fizzbuzzwhiz(10))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizzbuzzwhiz(15))

    def test_whiz(self):
        self.assertEqual('Whiz', fizzbuzzwhiz(2))
        self.assertEqual('Whiz', fizzbuzzwhiz(3))
        self.assertEqual('Whiz', fizzbuzzwhiz(5))
        self.assertEqual('Whiz', fizzbuzzwhiz(41))


if __name__ == '__main__':
    unittest.main()
