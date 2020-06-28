"""
Odd/Even/Prime Kata

Write a program that returns 'odd' if number is odd,
'even' if number is even but not prime,
and 'prime' if the number is prime.

https://en.wikipedia.org/wiki/Prime_number
"""
import unittest


def is_prime(num):
    if num == 1:
        return False
    return all(num % i != 0 for i in range(2, num))


def odd_or_even(num):
    if num % 2 == 0:
        return 'even'
    return 'odd'


def what_number(num):
    return 'prime' if is_prime(num) \
        else odd_or_even(num)


class OddEvenPrimeTest(unittest.TestCase):
    def test_odd(self):
        self.assertEqual('odd', what_number(1))
        self.assertEqual('odd', what_number(9))
        self.assertEqual('odd', what_number(77))

    def test_prime(self):
        self.assertEqual('prime', what_number(2))
        self.assertEqual('prime', what_number(3))
        self.assertEqual('prime', what_number(7))
        self.assertEqual('prime', what_number(29))

    def test_even(self):
        self.assertEqual('even', what_number(4))
        self.assertEqual('even', what_number(12))


if __name__ == '__main__':
    unittest.main(exit=False)
