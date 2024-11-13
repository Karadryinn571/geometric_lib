import circle
import unittest


class SquareTestCase(unittest.TestCase):
    def testZeroSides(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)
    
    def testNormalValues(self):
        self.assertAlmostEqual(circle.area(2), 12.56, delta=0.01)
        self.assertAlmostEqual(circle.area(3), 28.27, delta=0.01)
        self.assertAlmostEqual(circle.area(7), 153.93, delta=0.01)

        self.assertAlmostEqual(circle.perimeter(9), 56.54, delta=0.01)
        self.assertAlmostEqual(circle.perimeter(5), 31.41, delta=0.01)
        self.assertAlmostEqual(circle.perimeter(2), 12.56, delta=0.01)
