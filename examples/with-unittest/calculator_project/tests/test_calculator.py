import unittest
from main import Calculator, logger


logger.info("Running calculator tests...")
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_multiplication(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)
    
    def test_division(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_addition_with_negative_numbers(self):
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

    def test_addition_with_floats(self):
        result = self.calc.add(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0)

    def test_addition_with_two_strings(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", "3")
    
    def test_addition_with_string_and_number(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
    
    def test_parameters_are_numbers(self):
        with self.assertRaises(TypeError):
            self.calc.add([], {})

if __name__ == '__main__':
    unittest.main()