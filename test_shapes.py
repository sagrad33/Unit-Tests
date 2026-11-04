import unittest

import circle
import rectangle
import square
import triangle

class TestGeometricShapes(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(5), 25)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(10, 4), 40)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 4), 28)

    def test_circle_area(self):
        import math
        expected = math.pi * (3 ** 2)
        self.assertAlmostEqual(circle.area(3), expected, places=5)

    def test_circle_perimeter(self):
        import math
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(circle.perimeter(3), expected, places=5)

    def test_triangle_area(self):
        self.assertEqual(triangle.area(4, 5), 10.0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()
