import unittest
import src.area as area


class TestArea(unittest.TestCase):
    def test_square(self):
        self.assertEqual(area.square(3), 9)

    def test_rectangle(self):
        self.assertEqual(area.rectangle(3, 5), 15)

    def test_circle(self):
        self.assertEqual(area.circle(2), 12.566370614359172)

    def test_triangle(self):
        self.assertEqual(area.triangle(5, 10), 25)

    def test_parallelogram(self):
        self.assertEqual(area.parallelogram(5, 10), 50)


class TestSurfaceArea(unittest.TestCase):
    def test_sphere(self):
        self.assertEqual(area.sphere(2), 50.26548245743669)

    def test_cube(self):
        self.assertEqual(area.cube(3), 54)

    def test_cylinder(self):
        self.assertEqual(area.cylinder(2, 4), 75.39822368615503)
