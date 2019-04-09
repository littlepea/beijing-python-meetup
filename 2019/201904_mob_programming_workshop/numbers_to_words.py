"""
Numbers in Words Kata

http://codingdojo.org/kata/NumbersInWords/

The Kata is now to write a little converter class or function to convert numbers into words.

Example::

    >>> numbers_to_words(745)
    'seven hundred fourty-five'

Additional Kata: Convert it back.
"""
import unittest


UNITS_DICT = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

TENS_DICT = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

DIGITS_DICT = {
    3: "hundred",
    4: "thousand",
}


def numbers_to_words(num):
    if num < 20:
        return UNITS_DICT[num]
    elif num < 100:
        tens = num // 10
        units = num % 10
        word_tens = TENS_DICT[tens]
        word_units = numbers_to_words(units)
        if units == 0:
            return word_tens
        return f'{word_tens}-{word_units}'
    else:
        s_num = str(num)
        power = len(s_num) - 1
        this_digit = num // (10 ** power)
        remainder = num % (10 ** power)
        words = numbers_to_words(this_digit) + " " + DIGITS_DICT[len(s_num)]
        if not remainder:
            return words
        if remainder < 100:
            words += " and"
        return f'{words} {numbers_to_words(remainder)}'


class NumbersToWordsTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual('zero', numbers_to_words(0))

    def test_one(self):
        self.assertEqual('one', numbers_to_words(1))

    def test_ten(self):
        self.assertEqual('ten', numbers_to_words(10))

    def test_25(self):
        self.assertEqual('twenty-five', numbers_to_words(25))

    def test_sixty(self):
        self.assertEqual('sixty', numbers_to_words(60))

    def test_hundred_one(self):
        self.assertEqual('one hundred and one', numbers_to_words(101))

    def test_two_hundred(self):
        self.assertEqual('two hundred', numbers_to_words(200))

    def test_one_thousand_one_hundred_and_eleven(self):
        self.assertEqual('one thousand one hundred and eleven', numbers_to_words(1111))

    def test_ten_thousand(self):
        self.assertEqual('ten thousand', numbers_to_words(10000))


if __name__ == '__main__':
    unittest.main(exit=False)
