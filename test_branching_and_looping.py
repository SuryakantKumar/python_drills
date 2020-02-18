import unittest

from branching_and_looping import *


class TestBranchingAndLooping(unittest.TestCase):

    def test_integers_from_start_to_end_using_range(self):
        inputs_and_outputs = [
            ((0, 4, 1), [0, 1, 2, 3]),
            ((5, 8, 2), [5, 7]),
            ((8, 5, -1), [8, 7, 6]),
            ((8, 5, -2), [8, 6])
        ]
        for args, expected_output in inputs_and_outputs:
            output = integers_from_start_to_end_using_range(*args)
            self.assertEqual(output, expected_output)

    def test_integers_from_start_to_end_using_while(self):
        inputs_and_outputs = [
            ((0, 4, 1), [0, 1, 2, 3]),
            ((5, 8, 2), [5, 7]),
            ((8, 5, -1), [8, 7, 6]),
            ((8, 5, -2), [8, 6])
        ]
        for args, expected_output in inputs_and_outputs:
            output = integers_from_start_to_end_using_while(*args)
            self.assertEqual(output, expected_output)

    def test_two_digit_primes(self):
        output = two_digit_primes()

        expected_output = [11,
                           13,
                           17,
                           19,
                           23,
                           29,
                           31,
                           37,
                           41,
                           43,
                           47,
                           53,
                           59,
                           61,
                           67,
                           71,
                           73,
                           79,
                           83,
                           89,
                           97]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
