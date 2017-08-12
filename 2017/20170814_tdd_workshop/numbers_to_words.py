"""
Numbers in Words Kata

http://codingdojo.org/kata/NumbersInWords/

The Kata is now to write a little converter class or function to convert numbers into words.

Example::

    >>> numbers_to_words(745)
    'seven hundred and fourty five'

Additional Kata: Convert it back.
"""
import unittest


def numbers_to_words(num):
    return


class NumbersToWordsTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual('zero', numbers_to_words(0))


if __name__ == '__main__':
    unittest.main(exit=False)
