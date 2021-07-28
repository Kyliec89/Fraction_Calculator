from unittest import TestCase
import fractionCalculator
import fraction

class TestFractionCalculator(TestCase):
    def setUp(self):
        self.test_calculator = fractionCalculator.FractionCalculator()
        self.fraction1 = fraction.Fraction()
        self.fraction2 = fraction.Fraction()

    def test_calculate_addition_fraction_plus_fraction(self):
        self.fraction1.parser('2/3')
        self.fraction2.parser('1/8')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '+')
        self.assertEqual('19/24', self.test_calculator.get_result())

    def test_calculate_addition_fraction_plus_mixed(self):
        self.fraction1.parser('1/4')
        self.fraction2.parser('2_1/4')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '+')
        self.assertEqual('2_1/2', self.test_calculator.get_result())

    def test_calculate_addition_mixed_plus_mixed(self):
        self.fraction1.parser('2_1/3')
        self.fraction2.parser('8_4/5')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '+')
        self.assertEqual('11_2/15', self.test_calculator.get_result())

    def test_calculate_addition_negative_plus_positive(self):
        self.fraction1.parser('-1/4')
        self.fraction2.parser('3/7')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '+')
        self.assertEqual('5/28', self.test_calculator.get_result())

    def test_calculate_addition_mixed_negative_plus_positive(self):
        self.fraction1.parser('-3_1/3')
        self.fraction2.parser('7/8')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '+')
        self.assertEqual('-2_11/24', self.test_calculator.get_result())

    def test_calculate_subtraction_fraction_minus_fraction(self):
        self.fraction1.parser('4/9')
        self.fraction2.parser('15/7')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '-')
        self.assertEqual('-1_44/63', self.test_calculator.get_result())

    def test_calculate_subtraction_fraction_minus_mixed(self):
        self.fraction1.parser('4/7')
        self.fraction2.parser('3_2/5')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '-')
        self.assertEqual('-2_29/35', self.test_calculator.get_result())

    def test_calculate_subtraction_mixed_minus_mixed(self):
        self.fraction1.parser('8_3/7')
        self.fraction2.parser('2_4/5')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '-')
        self.assertEqual('5_22/35', self.test_calculator.get_result())

    def test_calculate_subtraction_negative_minus_positive(self):
        self.fraction1.parser('-1/4')
        self.fraction2.parser('3/7')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '-')
        self.assertEqual('-19/28', self.test_calculator.get_result())

    def test_calculate_subtraction_mixed_negative_minus_positive(self):
        self.fraction1.parser('-5_8/9')
        self.fraction2.parser('15/18')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '-')
        self.assertEqual('-6_13/18', self.test_calculator.get_result())

    def test_calculate_multiplication_fraction_times_fraction(self):
        self.fraction1.parser('12/3')
        self.fraction2.parser('9/15')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('2_2/5', self.test_calculator.get_result())

    def test_calculate_multiplication_fraction_times_mixed(self):
        self.fraction1.parser('3/8')
        self.fraction2.parser('23_7/9')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('8_11/12', self.test_calculator.get_result())

    def test_calculate_multiplication_mixed_times_mixed(self):
        self.fraction1.parser('5_4/9')
        self.fraction2.parser('17_3/8')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('94_43/72', self.test_calculator.get_result())

    def test_calculate_multiplication_negative_times_positive(self):
        self.fraction1.parser('-3/17')
        self.fraction2.parser('4/5')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('-12/85', self.test_calculator.get_result())

    def test_calculate_multiplication_mixed_negative_times_positive(self):
        self.fraction1.parser('-23_2/3')
        self.fraction2.parser('11/12')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('-21_25/36', self.test_calculator.get_result())

    def test_calculate_multiplication_double_negative(self):
        self.fraction1.parser('-11/5')
        self.fraction2.parser('-9/13')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '*')
        self.assertEqual('1_34/65', self.test_calculator.get_result())

    def test_calculate_division_fraction_by_fraction(self):
        self.fraction1.parser('11/18')
        self.fraction2.parser('1/3')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('1_5/6', self.test_calculator.get_result())

    def test_calculate_division_fraction_by_mixed(self):
        self.fraction1.parser('5/9')
        self.fraction2.parser('2_2/3')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('5/24', self.test_calculator.get_result())

    def test_calculate_division_mixed_by_mixed(self):
        self.fraction1.parser('4_4/9')
        self.fraction2.parser('1_1/2')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('2_26/27', self.test_calculator.get_result())

    def test_calculate_division_negative_by_positive(self):
        self.fraction1.parser('-1/4')
        self.fraction2.parser('3/7')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('-7/12', self.test_calculator.get_result())

    def test_calculate_division_mixed_negative_by_positive(self):
        self.fraction1.parser('-17_5/6')
        self.fraction2.parser('18/19')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('-18_89/108', self.test_calculator.get_result())

    def test_calculate_division_double_negative(self):
        self.fraction1.parser('-7/8')
        self.fraction2.parser('-1/4')
        self.test_calculator.calculate(self.fraction1, self.fraction2, '/')
        self.assertEqual('3_1/2', self.test_calculator.get_result())
