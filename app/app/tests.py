
"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_num(self):
        res = calc.sub(10, 5)
        self.assertEqual(res, 5)
