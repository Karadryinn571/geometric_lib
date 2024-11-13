import triangle
import unittest


class SquareTestCase(unittest.TestCase):
    def testZeroSides(self):
        self.assertEqual(triangle.area(0, 4), 0)
        self.assertEqual(triangle.area(8, 0), 0)
    
    def testNormalValues(self):
        self.assertEqual(triangle.area(4, 2), 4)
        self.assertEqual(triangle.area(15, 6), 45)
        self.assertEqual(triangle.area(9, 7), 31.5)

        self.assertEqual(triangle.perimeter(2, 9, 16), 27)
        self.assertEqual(triangle.perimeter(17, 11, 5), 33)
        self.assertEqual(triangle.perimeter(6, 7, 8), 21)
