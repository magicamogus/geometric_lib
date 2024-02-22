import unittest
from square import perimeter, area

class Test_Square(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 6.25)
    
    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.5), 10)

if __name__ == '__main__':
    unittest.main()
