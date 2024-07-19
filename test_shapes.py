import unittest
from shapes import *


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.area(), math.pi * 100, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right_angle())
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angle())

    def test_calculate_area(self):
        circle = Circle(10)
        triangle = Triangle(3, 4, 5)
        rectangle = Rectangle(5, 10)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 100, places=5)
        self.assertAlmostEqual(calculate_area(triangle), 6, places=5)
        self.assertAlmostEqual(calculate_area(rectangle), 50, places=5)

    def test_rectangle_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

if __name__ == '__main__':
    unittest.main()
