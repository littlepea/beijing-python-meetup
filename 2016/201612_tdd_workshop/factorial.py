"""
https://en.wikipedia.org/wiki/Factorial

In mathematics, the factorial of a non-negative integer n, denoted by n!,
is the product of all positive integers less than or equal to n. For example::

    5! = 5 x 4 x 3 x 2 x 1 = 120

The value of 0! is 1, according to the convention for an empty product.

The first 7 Factorial examples are::

    0!	1!	2!	3!	4!	5!	 6!
    0	1	2	6	24	120	 720
"""
import unittest


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


class FactorialTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(1, factorial(1))

    def test_two(self):
        self.assertEquals(2, factorial(2))

    def test_three(self):
        self.assertEquals(6, factorial(3))

    def test_six(self):
        self.assertEquals(720, factorial(6))


if __name__ == '__main__':
    unittest.main()
