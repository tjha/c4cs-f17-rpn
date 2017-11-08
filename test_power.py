import unittest

import rpn

class TestPower(unittest.TestCase):
    def test_power(self):
        result = rpn.calculate("3 2 ^")
        self.assertEqual(9, result)
    def test_power_reverse(self):
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)
