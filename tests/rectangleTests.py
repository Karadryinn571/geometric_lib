import rectangle
import unittest


class RectangeTestCase(unittest.TestCase):
    def testZeroSides(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 15), 0)
    
    def testNormalValues(self):
        self.assertEqual(rectangle.area(4, 8), 32)
        self.assertEqual(rectangle.area(15, 2), 30)
        self.assertEqual(rectangle.area(6, 9), 54)

        self.assertEqual(rectangle.perimeter(2, 4), 12)
        self.assertEqual(rectangle.perimeter(17, 8), 50)
        self.assertEqual(rectangle.perimeter(13, 6), 38)
