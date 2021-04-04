import unittest
from src.index import coulombs_law


class TestCoulomb(unittest.TestCase):
    def test_both_charge(self):
        result = coulombs_law(F='-0.0561875 base', r='2.0 base')
        self.assertEqual(result['product charges'], -2.5e-11)
        self.assertEqual(result['each charge'], 5e-6)

    def test_electric_force(self):
        result = coulombs_law(q1='5 u', q2='-5 u', r='2.0 base')
        self.assertEqual(result, -0.05618749999999999)

    def test_first_charge(self):
        result = coulombs_law(
            q1='5 u', F='-0.0561875 base', r='2.0 base')
        self.assertAlmostEqual(result, -5e-6)

    def test_second_charge(self):
        result = coulombs_law(
            q2='-5 u', F='-0.0561875 base', r='2.0 base')
        self.assertAlmostEqual(result, 5e-6)

    def test_return_charge(self):
        result = coulombs_law(
            q1='5 u', q2='-5 u', F='-0.0561875 base')
        self.assertAlmostEqual(result, 2.0)

    def test_incomplete_given(self):
        result = coulombs_law(q1='-0.0561875 base', r='2.0 base')
        self.assertEqual(result, None)
