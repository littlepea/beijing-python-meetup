"""
FizzBuzzWhiz Kata

Same as FizzBuzz but substitute prime numbers with "Whiz"

Write some code that will generate a string of integers, starting at 1 and going up to 100, all separated by commas.
Substitute any integer which is divisible by 3 with "Fizz", and any integer which is divisible by 5 with "Buzz",
and any integer divisible by 3 and 5 with "FizzBuzz".

If none of the above conditions apply just return the number itself.
"""
import unittest


def fizzbuzzwhiz(num):
    return


class FizzBuzzWhizTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual('1', fizzbuzzwhiz(1))


if __name__ == '__main__':
    unittest.main(exit=False)
