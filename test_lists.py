import unittest

from lists import *


class TestList(unittest.TestCase):
    def test_sum_items_in_list(self):
        inputs_and_outputs = [
            ([1, 2, 3, 4], 10),
            ([1], 1),
            ([0], 0),
            ([], 0),
            ([-1, 2], 1),
        ]
        for inp, expected_output in inputs_and_outputs:
            output = sum_items_in_list(inp)
            self.assertEqual(output, expected_output)

    def test_list_length(self):
        inputs_and_outputs = [
            ([1, 2, 3, 4], 4),
            ([1], 1),
            ([0], 1),
            ([], 0),
            ([-1, 2], 2),
        ]
        for inp, expected_output in inputs_and_outputs:
            output = list_length(inp)
            self.assertEqual(output, expected_output)

    def test_last_three_items(self):
        inputs_and_outputs = [
            ([1, 2, 3, 4], [2, 3, 4]),
            ([1], [1]),
            ([], []),
            ([-1, 2], [-1, 2]),
        ]
        for inp, expected_output in inputs_and_outputs:
            output = last_three_items(inp)
            self.assertEqual(output, expected_output)

    def test_first_three_items(self):
        inputs_and_outputs = [
            ([1, 2, 3, 4], [1, 2, 3]),
            ([1], [1]),
            ([], []),
            ([-1, 2], [-1, 2]),
        ]
        for inp, expected_output in inputs_and_outputs:
            output = first_three_items(inp)
            self.assertEqual(output, expected_output)

    def test_sort_list(self):
        inputs_and_outputs = [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([1], [1]),
            ([], []),
            ([2, -1], [-1, 2]),
            (['c', 'b', 'a'], ['a', 'b', 'c'])
        ]
        for inp, expected_output in inputs_and_outputs:
            output = sort_list(inp)
            self.assertEqual(output, expected_output)

    def test_append_item(self):
        inputs_args_outputs = [
            ([1, 2, 3], 4, [1, 2, 3, 4]),
            (['a', 'b'], 'c', ['a', 'b', 'c']),
        ]
        for inp, arg, expected_output in inputs_args_outputs:
            output = append_item(inp, arg)
            self.assertEqual(output, expected_output)

    def test_remove_last_item(self):
        inputs_and_outputs = [
            ([1, 2, 3], [1, 2]),
            (['a', 'b'], ['a']),
        ]
        for inp, expected_output in inputs_and_outputs:
            output = remove_last_item(inp)
            self.assertEqual(output, expected_output)

    def test_count_occurrences(self):
        inputs_args_outputs = [
            ([1, 2, 3], 1, 1),
            ([1, 2, 3], 0, 0),
            ([1, 2, 2], 2, 2),
        ]
        for inp, arg, expected_output in inputs_args_outputs:
            output = count_occurrences(inp, arg)
            self.assertEqual(output, expected_output)

    def test_is_item_present_in_list(self):
        inputs_args_outputs = [
            ([1, 2, 3], 1, True),
            ([1, 2, 3], 0, False),
            ([1, 2, 2], 2, True),
        ]
        for inp, arg, expected_output in inputs_args_outputs:
            output = is_item_present_in_list(inp, arg)
            self.assertEqual(output, expected_output)

    def test_append_all_items_of_y_to_x(self):
        inputs_args_outputs = [
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([1], [2], [1, 2]),
            ([], [], []),
        ]
        for x, y, expected_output in inputs_args_outputs:
            output = append_all_items_of_y_to_x(x, y)
            self.assertEqual(output, expected_output)

    def test_list_copy(self):
        inputs = [
            ([1, 2, 3]),
            ([]),
            ([4, 5, 6])
        ]
        for inp in inputs:
            output = list_copy(inp)
            self.assertEqual(inp, output)
            self.assertIsNot(inp, output)


if __name__ == '__main__':
    unittest.main()
