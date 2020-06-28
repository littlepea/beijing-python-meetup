"""
FizzBuzzWhiz Kata

Same as FizzBuzz but for prime numbers add "Whiz"

Write some code that will generate a string of integers, starting at 1 and going up to 100, all separated by commas.
Substitute any integer which is divisible by 3 with "Fizz", and any integer which is divisible by 5 with "Buzz",
and any integer divisible by 3 and 5 with "FizzBuzz".

If none of the above conditions apply just return the number itself.
"""
import unittest


def is_prime(num):
    if num == 1:
        return False

    return all(num % i != 0 for i in range(2, num))


def fizzbuzzwhiz(num):
    res = ''

    if num % 3 == 0:
        res += 'Fizz'

    if num % 5 == 0:
        res += 'Buzz'

    if is_prime(num):
        res += 'Whiz'

    return res or str(num)


class FizzBuzzWhizTest(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual('1', fizzbuzzwhiz(1))
        self.assertEqual('4', fizzbuzzwhiz(4))
        self.assertEqual('8', fizzbuzzwhiz(8))

    def test_whiz(self):
        self.assertEqual('Whiz', fizzbuzzwhiz(2))
        self.assertEqual('FizzWhiz', fizzbuzzwhiz(3))
        self.assertEqual('BuzzWhiz', fizzbuzzwhiz(5))
        self.assertEqual('Whiz', fizzbuzzwhiz(7))
        self.assertEqual('Whiz', fizzbuzzwhiz(11))

    def test_fizz(self):
        self.assertEqual('Fizz', fizzbuzzwhiz(6))
        self.assertEqual('Fizz', fizzbuzzwhiz(9))
        self.assertEqual('Fizz', fizzbuzzwhiz(12))

    def test_buzz(self):
        self.assertEqual('Buzz', fizzbuzzwhiz(10))
        self.assertEqual('Buzz', fizzbuzzwhiz(20))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizzbuzzwhiz(15))
        self.assertEqual('FizzBuzz', fizzbuzzwhiz(45))


if __name__ == '__main__':
    unittest.main(exit=False)
