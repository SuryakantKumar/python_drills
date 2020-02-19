import unittest

from file_operations import *


class TestFileOperations(unittest.TestCase):
    def test_operations(self):
        write_to_file('./data.txt', 'Simple is better than complex.\n')
        s = read_file('./data.txt')
        self.assertEqual(s, 'Simple is better than complex.\n')

        append_to_file('./data.txt', 'Explicit is better than implicit.\n')
        s2 = read_file('./data.txt')
        self.assertEqual(
            s2, 'Simple is better than complex.\nExplicit is better than implicit.\n')

    def test_numbers_and_squares(self):
        numbers_and_squares(4, './data.txt')
        output = read_file('./data.txt')
        expected_output = """
        1,1\n2,4\n3,9\n4,16\n
        """
        self.assertEqual(output.strip(), expected_output.strip())


if __name__ == '__main__':
    unittest.main()
