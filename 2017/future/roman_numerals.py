"""
Roman Numerals Kata

http://codingdojo.org/kata/RomanNumerals/

you should write a function to convert from normal numbers to Roman Numerals. eg::

     1 --> I
     10 --> X
     7 --> VII

http://www.novaroma.org/via_romana/numbers.html
"""
import unittest


def roman(num):
    return


class RomanNumeralsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual('I', roman(1))


if __name__ == '__main__':
    unittest.main(exit=False)
