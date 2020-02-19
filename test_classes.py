import unittest

from classes import *


class TestClasses(unittest.TestCase):
    def test_point(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        self.assertEqual(p1.x, 0)
        self.assertEqual(p1.y, 0)

        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 4)

        d1 = p1.distance(p2)
        self.assertEqual(d1, 5.0)

        d2 = p2.distance(p1)
        self.assertEqual(d2, 5.0)


if __name__ == '__main__':
    unittest.main()
