"""
https://en.wikipedia.org/wiki/Fibonacci_number

In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence,
and characterized by the fact that every number after the first two is the sum of the two preceding ones:


The first 21 Fibonacci numbers Fn for n = 0, 1, 2, ..., 20 are::

    F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	 F18  F19  F20
    0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597 2584 4181 6765
"""
import unittest


def fibonacci(n):
    pass


class FibonacciTest(unittest.TestCase):
    def test_zero(self):
        self.assertEquals(0, fibonacci(0))


if __name__ == '__main__':
    unittest.main()
