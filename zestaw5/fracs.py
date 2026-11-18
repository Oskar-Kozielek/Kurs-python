from math import gcd


def _normalize(frac):
    numerator, denominator = frac

    if denominator == 0:
        raise ZeroDivisionError("Mianownik ułamka nie może być równy zero.")

    if numerator == 0:
        return [0, 1]

    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    return [numerator, denominator]


def add_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return _normalize([a * d + c * b, b * d])


def sub_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return _normalize([a * d - c * b, b * d])


def mul_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return _normalize([a * c, b * d])


def div_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2

    if c == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")

    return _normalize([a * d, b * c])


def is_positive(frac):
    numerator, denominator = frac

    if denominator == 0:
        raise ZeroDivisionError("Mianownik ułamka nie może być równy zero.")

    return (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0)


def is_zero(frac):
    numerator, denominator = frac

    if denominator == 0:
        raise ZeroDivisionError("Mianownik ułamka nie może być równy zero.")

    return numerator == 0


def cmp_frac(frac1, frac2):
    a, b = _normalize(frac1)
    c, d = _normalize(frac2)

    left = a * d
    right = c * b

    if left < right:
        return -1
    if left > right:
        return 1
    return 0


def frac2float(frac):
    numerator, denominator = frac

    if denominator == 0:
        raise ZeroDivisionError("Mianownik ułamka nie może być równy zero.")

    return numerator / denominator


import unittest


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [-1, 2]), [0, 1])
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), [0, 1])
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([-1, 2], [2, 3]), [-1, 3])
        self.assertEqual(mul_frac([0, 5], [3, 4]), [0, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        self.assertEqual(div_frac([-1, 2], [1, 4]), [-2, 1])
        self.assertEqual(div_frac([0, 3], [2, 5]), [0, 1])
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive([0, 1]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)
        self.assertEqual(cmp_frac([3, 4], [1, 2]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, -2], [-1, 2]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([-1, 4]), -0.25)
        self.assertAlmostEqual(frac2float([3, 2]), 1.5)
        with self.assertRaises(ZeroDivisionError):
            _ = frac2float([1, 0])


if __name__ == "__main__":
    unittest.main()
