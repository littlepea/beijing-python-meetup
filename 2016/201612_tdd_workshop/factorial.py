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
    pass


class FactorialTest(unittest.TestCase):
    def test_zero(self):
        self.assertEquals(0, factorial(0))


if __name__ == '__main__':
    unittest.main()
