import unittest

from mixed_bag import *


class TestMixedBag(unittest.TestCase):
    def test_unique(self):
        inputs_and_outputs = [
            ([], set()),
            ([1, 1, 1], set([1])),
            ([1, 2, 1], set([1, 2])),
        ]
        for args, expected_output in inputs_and_outputs:
            output = unique(args)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
