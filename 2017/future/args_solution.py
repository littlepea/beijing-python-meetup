"""
Args Kata

http://codingdojo.org/kata/Args/

Write a function that takes a string with CLI arguments/flags and returns a dictionary with argument names and values.

For example if the program is to be called with these arguments::

    -l -p 8080 -d /usr/logs

this indicates a schema with 3 flags: l, p, d. The "l" (logging) flag has no values associated with it,
it is a boolean flag, True if present, False if not. the "p" (port) flag has an integer value,
and the "d" (directory) flag has a string value.

If a flag mentioned in the schema is missing in the arguments, a suitable default value should be returned.
For example "False" for a boolean, 0 for a number, and '' for a string.

If you are feeling ambitious, extend your code to support lists eg::

    -g this,is,a,list -d 1,2,-3,5

So the "g" flag indicates a list of strings, ['this', 'is', 'a', 'list']
and the "d" flag indicates a list of integers, [1, 2, -3, 5].
"""
import unittest


def _parse_value(val):
    try:
        name, value = val.split()
    except ValueError:
        return val.strip(), True

    try:
        return name, int(value)
    except ValueError:
        return name, value


def parse_arguments(args):
    parsed = []

    for _ in args.split('-'):
        if not _:
            continue

        parsed.append(_parse_value(_))

    return dict(parsed)


class ArgsTest(unittest.TestCase):
    def test_string(self):
        self.assertDictEqual({'d': '/usr/logs'}, parse_arguments('-d /usr/logs'))

    def test_integer(self):
        self.assertDictEqual({'p': 8080}, parse_arguments('-p 8080'))

    def test_boolean(self):
        self.assertDictEqual({'l': True}, parse_arguments('-l'))

    def test_mixed(self):
        self.assertDictEqual({'l': True, 'p': 8080, 'd': '/usr/logs'},
                             parse_arguments('-l -p 8080 -d /usr/logs'))


if __name__ == '__main__':
    unittest.main(exit=False)
