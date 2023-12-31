"""Django Test Module in Root App """

from django.test import SimpleTestCase

from app import calc  # type: ignore


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        res = calc.minus(6, 5)
        self.assertEqual(res, 1)
