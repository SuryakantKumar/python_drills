import unittest

from dictionaries import *


class TestBranchingAndLooping(unittest.TestCase):
    def test_word_count(self):
        s = 'hello world'
        expected_output = {'hello': 1, 'world': 1}
        output = word_count(s)
        self.assertEqual(output, expected_output)

        s = "Python is an interpreted, high-level, general-purpose programming language. Python interpreters are available for many operating systems. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported."

        expected_output = {'Python': 3,
                           'is': 2,
                           'an': 1,
                           'interpreted': 1,
                           'high-level': 1,
                           'general-purpose': 1,
                           'programming': 4,
                           'language': 2,
                           'interpreters': 1,
                           'are': 2,
                           'available': 1,
                           'for': 1,
                           'many': 1,
                           'operating': 1,
                           'systems': 1,
                           'a': 1,
                           'multi-paradigm': 1,
                           'Object-oriented': 1,
                           'and': 1,
                           'structured': 1,
                           'fully': 1,
                           'supported': 1}
        output = word_count(s)
        self.assertEqual(output, expected_output)

    def test_dict_items(self):
        inputs_and_expected_outputs = [
            ({'a': 1, 'b': 2}, [('a', 1), ('b', 2)]),
            ({}, []),
            ({'a': 1}, [('a', 1)]),
        ]
        for inp, expected_output in inputs_and_expected_outputs:
            output = dict_items(inp)
            self.assertEqual(output, expected_output)

    def test_dict_items_sorted(self):
        inputs_and_expected_outputs = [
            ({'c': 3, 'a': 1, 'b': 2}, [('a', 1), ('b', 2), ('c', 3)]),
            ({}, []),
            ({'a': 1}, [('a', 1)]),
        ]
        for inp, expected_output in inputs_and_expected_outputs:
            output = dict_items_sorted(inp)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
