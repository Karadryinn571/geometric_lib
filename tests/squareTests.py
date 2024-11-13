import square
import unittest


class SquareTestCase(unittest.TestCase):
    def testZeroSides(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)
    
    def testNormalValues(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(15), 225)
        self.assertEqual(square.area(6), 36)

        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(17), 68)
        self.assertEqual(square.perimeter(6), 24)
