import unittest
from circle import perimeter, area, math

class Test_Circle_Calculations(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), math.pi * 2.5**2)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

if __name__ == '__main__':
    unittest.main()