import unittest

from functions import *


class TestBranchingAndLooping(unittest.TestCase):

    def test_is_prime(self):
        inputs_and_outputs = [
            (2, True),
            (3, True),
            (4, False),
            (63, False),
            (97, True),
        ]
        for n, expected_output in inputs_and_outputs:
            output = is_prime(n)
            self.assertEqual(output, expected_output)

    def test_two_digit_primes(self):
        output = n_digit_primes()

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

        output = n_digit_primes(2)
        self.assertEqual(output, expected_output)

    def test_one_digit_primes(self):
        output = n_digit_primes(1)
        expected_output = [
            2,
            3,
            5,
            7
        ]
        output = n_digit_primes(1)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
