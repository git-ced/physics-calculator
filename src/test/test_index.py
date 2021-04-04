import unittest
import math
from src.index import coulombs_law, electric_field_2d


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


class TestElectricField2D(unittest.TestCase):
    def test_electric_field_2d(self):
        angle = math.atan(12 / 5)
        ep = coulombs_law(q1='14n', q2='1', r='13c', k=(8.9876 * 1e9))
        en = coulombs_law(q1='-17n', q2='1', r='13c', k=(8.9876 * 1e9))
        result = electric_field_2d(ep, en, angle, 'center', 'top')
        self.assertEqual(result['EP'], 7445.349112426035)
        self.assertEqual(result['EN'], -9040.781065088757)
        self.assertEqual(result['ANGLE'], 1.176005207095135)
        self.assertEqual(result['EXP'], 2863.5958124715526)
        self.assertEqual(result['EYP'], 6872.629949931725)
        self.assertEqual(result['EXN'], 3477.2234865725995)
        self.assertEqual(result['EYN'], -8345.336367774236)
        self.assertEqual(result['ESUMX'], 6340.819299044152)
        self.assertEqual(result['ESUMY'], -1472.7064178425117)
        self.assertEqual(result['ENET MAGNITUDE'], 6509.5970363982815)
        self.assertEqual(result['ENET ANGLE'], -0.22821194179065718)
