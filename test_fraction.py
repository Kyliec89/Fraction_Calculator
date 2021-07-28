from unittest import TestCase
import fraction

class TestFraction(TestCase):
    def setUp(self):
        self.test_fraction = fraction.Fraction()

    def test_parser_fraction(self):
        self.test_fraction.parser('3/4')
        self.assertIsNotNone(self.test_fraction)

    def test_parser_mixed_number(self):
        self.test_fraction.parser('1_2/5')
        self.assertIsNotNone(self.test_fraction)

    def test_parser_negative_fraction(self):
        self.test_fraction.parser('-1/7')
        self.assertIsNotNone(self.test_fraction)

    def test_parser_whole_num(self):
        self.test_fraction.parser('12')
        self.assertIsNotNone(self.test_fraction)

    def test_get_numerator_fraction(self):
        self.test_fraction.parser('3/4')
        self.assertEqual(3, self.test_fraction.get_numerator())

    def test_get_numerator_negative_fraction(self):
        self.test_fraction.parser('-15/4')
        self.assertEqual(-15, self.test_fraction.get_numerator())

    def test_get_numerator_whole_num(self):
        self.test_fraction.parser('12')
        self.assertEqual(12, self.test_fraction.get_numerator())

    def test_get_numerator_mixed_num(self):
        self.test_fraction.parser('7_1/2')
        self.assertEqual(15, self.test_fraction.get_numerator())

    def test_get_denominator_fraction(self):
        self.test_fraction.parser('15/2')
        self.assertEqual(2, self.test_fraction.get_denominator())

    def test_get_denominator_negative_fraction(self):
        self.test_fraction.parser('-7/9')
        self.assertEqual(9, self.test_fraction.get_denominator())

    def test_get_denominator_whole_num(self):
        self.test_fraction.parser('7')
        self.assertEqual(1, self.test_fraction.get_denominator())

    def test_get_denominator_mixed_num(self):
        self.test_fraction.parser('4_3/8')
        self.assertEqual(8, self.test_fraction.get_denominator())

    def test_is_mixed_false(self):
        self.test_fraction.parser('8/10')
        self.assertFalse(self.test_fraction.get_is_mixed())

    def test_is_mixed_true(self):
        self.test_fraction.parser('3_9/15')
        self.assertTrue(self.test_fraction.get_is_mixed())

    def test_is_mixed_improper(self):
        self.test_fraction.parser('18/7')
        self.assertFalse(self.test_fraction.get_is_mixed())

    def test_is_mixed_negative_true(self):
        self.test_fraction.parser('-5_7/8')
        self.assertTrue(self.test_fraction.get_is_mixed())

    def test_is_mixed_negative_false(self):
        self.test_fraction.parser('-3/8')
        self.assertFalse(self.test_fraction.get_is_mixed())

    def test_zero_error_false(self):
        self.test_fraction.parser('1/2')
        self.assertFalse(self.test_fraction.zero_error())

    def test_convert_to_improper_positive(self):
        self.test_fraction.parser('1_3/5')
        self.assertEqual(8, self.test_fraction.get_numerator())

    def test_convert_to_improper_negative(self):
        self.test_fraction.parser('-4_7/9')
        self.assertEqual(-43, self.test_fraction.get_numerator())
