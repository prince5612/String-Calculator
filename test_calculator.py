
import unittest
from calculator import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # 1. Empty input returns 0.0 and single number return as it is
    def test_empty_input(self):
        self.assertEqual(self.calc.calculate(""), 0.0)
        self.assertEqual(self.calc.calculate("1"),1)

    # 2. Default operator '+' and default delimiter ','
    def test_default_addition(self):
        self.assertEqual(self.calc.calculate("1,2,3,4"), 10)

    # 3. Leading operator '*' overrides default
    def test_leading_multiplication(self):
        # *2,3,4 -> treat as (2*3)*4 = 24
        self.assertEqual(self.calc.calculate("*2,3,4"), 24)

    # 4. Leading operator '-' overrides default
    def test_leading_subtraction(self):
        # -10,3,2 -> (10-3)-2 = 5
        self.assertEqual(self.calc.calculate("-10,3,2"), 5)

    # 5. Single custom delimiter header
    def test_single_custom_delimiter(self):
        #default operator +
        self.assertEqual(self.calc.calculate("[;]1;2;3"), 6)

    # 6. Multiple custom delimiters
    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.calculate("[;][%]1;2%3"), 6)

    # 7. Ignore numbers > 1000
    def test_ignore_large_numbers(self):
        self.assertEqual(self.calc.calculate("2,1001,3"), 5)

    # 8. Inline operator switching within number tokens
    def test_inline_operator_switching(self):
        # 1,+,2,*,3 -> (1+2)*3 = 9
        expr = "1,+,2,*,3"
        self.assertEqual(self.calc.calculate(expr), 9)

    # 9. Mixed operators without explicit header
    def test_mixed_operators(self):
        # default + delimiter comma, operators in token stream
        self.assertEqual(self.calc.calculate("1,+,2,*,3,-,1"), ((1+2)*3)-1)

    # 10. redundant delimiters ignored
    def test_redundant_delimiters(self):
        #default delimiter , and operator + 
        self.assertEqual(self.calc.calculate("1,,,,3,,,,,5"),(1+3+5))

    # 11. Division by zero raises error
    def test_division_by_zero(self):
        with self.assertRaises(CalculatorError):
            self.calc.calculate("10/0")

    # 12. Invalid token (non-digit, non-operator)
    def test_invalid_token(self):
        with self.assertRaises(CalculatorError):
            self.calc.calculate("1,a,2")

    # 13. No numbers at all raises error
    def test_no_numbers(self):
        with self.assertRaises(CalculatorError):
            self.calc.calculate("[;];;;+")

    # 14. Header without proper closing bracket raises error
    def test_invalid_header(self):
        with self.assertRaises(CalculatorError):
            self.calc.calculate("[;1;2;3")

    # 15. Complex case: multiple delimiters, inline ops, ignore >1000
    def test_complex_expression(self):
        expr = "-[x][*]5x1001*-*2*3"  # delimiters x & *, ignore 1001 , operator -
        # tokens: 5, 2, 3 -> ((5-2)-3) = 0
        self.assertEqual(self.calc.calculate(expr), 0)

if __name__ == '__main__':
    unittest.main()
