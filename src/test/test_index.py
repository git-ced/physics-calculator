import unittest
import math
import index as calculate


class TestCoulomb(unittest.TestCase):
    def test_both_charge(self):
        result = calculate.coulombs_law(F='-0.0561875 base', r='2.0 base')
        self.assertEqual(result['product charges'], -2.5e-11)
        self.assertEqual(result['each charge'], 5e-6)

    def test_electric_force(self):
        result = calculate.coulombs_law(q1='5 u', q2='-5 u', r='2.0 base')
        self.assertEqual(result, -0.05618749999999999)

    def test_first_charge(self):
        result = calculate.coulombs_law(
            q1='5 u', F='-0.0561875 base', r='2.0 base')
        self.assertAlmostEqual(result, -5e-6)

    def test_second_charge(self):
        result = calculate.coulombs_law(
            q2='-5 u', F='-0.0561875 base', r='2.0 base')
        self.assertAlmostEqual(result, 5e-6)

    def test_return_charge(self):
        result = calculate.coulombs_law(
            q1='5 u', q2='-5 u', F='-0.0561875 base')
        self.assertAlmostEqual(result, 2.0)

    def test_incomplete_given(self):
        result = calculate.coulombs_law(q1='-0.0561875 base', r='2.0 base')
        self.assertEqual(result, None)


class TestElectricField2D(unittest.TestCase):
    def test_electric_field_2d(self):
        angle = math.atan(12 / 5)
        ep = calculate.coulombs_law(
            q1='14n', q2='1', r='13c', k=(8.9876 * 1e9))
        en = calculate.coulombs_law(
            q1='-17n', q2='1', r='13c', k=(8.9876 * 1e9))
        result = calculate.electric_field_2d(ep, en, angle, 'center', 'top')
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


class TestGauss(unittest.TestCase):
    def test_flux(self):
        result = calculate.gauss_law(Q='3u')
        self.assertEqual(result, 338829.907386492)

    def test_charge(self):
        result = calculate.gauss_law(I=338829.907386492)
        self.assertEqual(result, 3e-6)

    def test_incomplete_given(self):
        result = calculate.gauss_law()
        self.assertEqual(result, None)


class TestElectricFlux(unittest.TestCase):
    def test_flux(self):
        result = calculate.electric_flux(E='3u', A='9', phi=60)
        self.assertEqual(result, 1.3500000000000003e-5)

    def test_area(self):
        result = calculate.electric_flux(E='3u', I=321321, phi=60)
        self.assertEqual(result, 214213999999.99994)

    def test_magnitude(self):
        result = calculate.electric_flux(A='9', I=321321, phi=60)
        self.assertEqual(result, 71404.66666666666)

    def test_incomplete_given(self):
        result = calculate.electric_flux(I=32)
        self.assertEqual(result, None)
