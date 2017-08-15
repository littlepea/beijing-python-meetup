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
from collections import OrderedDict


DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
DOUBLES = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
HUNDRED = 'hundred'
THOUSAND = 'thousand'
AND = 'and'
DECIMALS = (
    (1000**4, 'trillion'),
    (1000**3, 'billion'),
    (1000**2, 'million'),
    (1000, 'thousand'),
)


def _plural_suffix(num):
    return 's' if num > 1 else ''


def _triple_digits_to_words(num):
    words = []
    
    if num > 99:
        triple = num // 100
        num -= triple * 100
        words.append(DIGITS[triple])
        words.append(HUNDRED + _plural_suffix(triple))
        if num:
            words.append(AND)
    
    if num > 19:
        double = num // 10
        num -= double * 10
        words.append(DOUBLES[double-2])
    
    if num:
        words.append(DIGITS[num])
    
    return ' '.join(words)


def numbers_to_words(num):
    words = []
    
    if not num:
        return 'zero'
    
    for decimal, word in DECIMALS:
        if num < decimal:
            continue
        digit = num // decimal
        num -= digit * decimal
        words.append(_triple_digits_to_words(digit))
        words.append(word + _plural_suffix(digit))
        if num and num < 100:
            words.append(AND)
    
    if num:
        words.append(_triple_digits_to_words(num))
    
    return ' '.join(words)


class SomeTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual('zero', numbers_to_words(0))
        
    def test_one(self):
        self.assertEqual('one', numbers_to_words(1))
        
    def test_ten(self):
        self.assertEqual('ten', numbers_to_words(10))
        
    def test_twenty(self):
        self.assertEqual('twenty', numbers_to_words(20))
        
    def test_twenty_one(self):
        self.assertEqual('twenty one', numbers_to_words(21))
        
    def test_thirty(self):
        self.assertEqual('thirty', numbers_to_words(30))
        
    def test_ninety_nine(self):
        self.assertEqual('ninety nine', numbers_to_words(99))
        
    def test_hundred(self):
        self.assertEqual('one hundred', numbers_to_words(100))
        
    def test_101(self):
        self.assertEqual('one hundred and one', numbers_to_words(101))
        
    def test_110(self):
        self.assertEqual('one hundred and ten', numbers_to_words(110))
        
    def test_999(self):
        self.assertEqual('nine hundreds and ninety nine', numbers_to_words(999))
        
    def test_thousand(self):
        self.assertEqual('one thousand', numbers_to_words(1000))
        
    def test_1009(self):
        self.assertEqual('one thousand and nine', numbers_to_words(1009))
        
    def test_9999(self):
        self.assertEqual('nine thousands nine hundreds and ninety nine', numbers_to_words(9999))
        
    def test_ten_thousand(self):
        self.assertEqual('ten thousands', numbers_to_words(10000))
        
    def test_nineteen_thousand(self):
        self.assertEqual('nineteen thousands', numbers_to_words(19000))
        
    def test_twenty_thousand(self):
        self.assertEqual('twenty thousands', numbers_to_words(20000))
        
    def test_99999(self):
        self.assertEqual('ninety nine thousands nine hundreds and ninety nine', numbers_to_words(99999))
        
    def test_hundred_thousand(self):
        self.assertEqual('one hundred thousands', numbers_to_words(100000))
        
    def test_999999(self):
        self.assertEqual('nine hundreds and ninety nine thousands nine hundreds and ninety nine',
                         numbers_to_words(999999))
        
    def test_million(self):
        self.assertEqual('one million', numbers_to_words(1000000))
        
    def test_999999999(self):
        self.assertEqual(
            'nine hundreds and ninety nine millions nine hundreds and ninety nine thousands nine hundreds and ninety nine',
            numbers_to_words(999999999))
        
    def test_billion(self):
        self.assertEqual('one billion', numbers_to_words(1000000000))


if __name__ == '__main__':
    unittest.main(exit=False)
