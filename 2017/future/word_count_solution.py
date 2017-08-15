"""
Word Counter Kata

A function that, given a delimited string, returns a collection of all of the unique words in it
and the count of how many times they occurred.

Example::

    >>> word_count('boom bang boom')
    {'boom': 2, 'bang': 1}
"""
import unittest
from collections import defaultdict


def word_count(string):
    counter = defaultdict(int)
    for word in string.split():
        counter[word] += 1
    return counter


class WordCounterTest(unittest.TestCase):
    def test_boom_bang(self):
        self.assertDictEqual({'boom': 2, 'bang': 1},
                             word_count('boom bang boom'))


if __name__ == '__main__':
    unittest.main(exit=False)
