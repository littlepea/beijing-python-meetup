"""
Finds the first non-repeated character in a string

https://www.codeeval.com/open_challenges/12/
"""
import unittest


def first_unique_character(s):
    before = ''
    for i in range(0, len(s)):
        char = s[i]
        after = s[i+1:]
        if char not in before + after:
            return char
        before += char


class FirstUniqueCharacterTest(unittest.TestCase):
    def test_yellow(self):
        self.assertEquals('y', first_unique_character('yellow'))

    def test_tooth(self):
        self.assertEquals('h', first_unique_character('tooth'))


if __name__ == '__main__':
    unittest.main(exit=False)

