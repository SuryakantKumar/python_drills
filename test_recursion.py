import json
import unittest

from recursion import *


class TestRecursion(unittest.TestCase):
    def test_html_dict_search(self):
        with open('./html_dict.json', 'r') as f:
            html_dict = json.load(f)

        output = html_dict_search(html_dict, '.headline-item')
        expected_output = [
            {
                "name": "li",
                "attrs": {
                    "class": "headline-item"
                },
                "text": "zero",
                "children": []
            },
            {
                "name": "li",
                "attrs": {
                    "class": "headline-item"
                },
                "text": "one",
                "children": []
            },
            {
                "name": "li",
                "attrs": {
                    "class": "headline-item"
                },
                "text": "two",
                "children": []
            },
            {
                "name": "li",
                "attrs": {
                    "class": "headline-item"
                },
                "text": "three",
                "children": []
            }
        ]
        self.assertEqual(output, expected_output)

        output = html_dict_search(html_dict, '#buy-now-btn')
        expected_output = [{
            "name": "button",
            "attrs": {
                "id": "buy-now-btn"
            },
            "text": "Buy Now",
            "children": []
        }]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
