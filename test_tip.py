import unittest

from tip import calculate_tip


class TipTests(unittest.TestCase):
    def test_default_percent(self):
        self.assertEqual(calculate_tip(100), 10.0)

    def test_custom_percent(self):
        self.assertEqual(calculate_tip(50, 15), 7.5)

    def test_zero_bill(self):
        self.assertEqual(calculate_tip(0), 0.0)


if __name__ == "__main__":
    unittest.main()
