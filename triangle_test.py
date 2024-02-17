import unittest
from triangle import perimeter, area

class TestTriangleFunctions(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(0, 5), 0)
        self.assertAlmostEqual(area(2.5, 4.2), 5.25)
    
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 0, 0), 0) 
        self.assertAlmostEqual(perimeter(2.5, 4.2, 3.1), 9.8)

if __name__ == '__main__':
    unittest.main()