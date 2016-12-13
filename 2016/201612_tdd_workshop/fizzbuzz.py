"""
https://en.wikipedia.org/wiki/Fizz_buzz

For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Otherwise, just print the actual number::

    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, FizzBuzz, 22, 23 ...
"""
import unittest


def fizzbuzz(n):
    fb = ''
    if n % 3 == 0:
        fb += 'Fizz'
    if n % 5 == 0:
        fb += 'Buzz'

    return fb or str(n)


class FizzBuzzTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals('1', fizzbuzz(1))

    def test_fizz(self):
        self.assertEqual('Fizz', fizzbuzz(3))

    def test_buzz(self):
        self.assertEqual('Buzz', fizzbuzz(5))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizzbuzz(15))


if __name__ == '__main__':
    unittest.main()
