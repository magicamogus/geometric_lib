import unittest
from rectangle import perimeter, area

class Test_Rectangle_Functions(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(0, 5), 0)
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)
    
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)

if __name__ == '__main__':
    unittest.main()
