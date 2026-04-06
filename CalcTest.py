import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 4), 6)    # Expect 10 - 4 = 6
        self.assertEqual(calc.subtract(4, 4), 0)     # Expect 4 - 4 = 0
        self.assertEqual(calc.subtract(4, 10), -6)   # Expect 4 - 10 = -6

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(5, 5), 25)    # Expect 5 * 5 = 25
        self.assertEqual(calc.multiply(5, 0), 0)     # Expect 5 * 0 = 0
        self.assertEqual(calc.multiply(5, -5), -25)  # Expect 5 * -5 = -25
        self.assertEqual(calc.multiply(-5, -5), 25)  # Expect -5 * -5 = 25
		
    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(9, 3), 3.0)    # Expect 9 / 3 = 3.0
        result = calc.divide(9,-3)
        self.assertEqual(result, -3.0) # Expect 9 / -3 = -3.0
        result = calc.divide(-9,-3)
        self.assertEqual(result, 3.0) # Expect -9 / -3 = 3.0
        self.assertRaises(ValueError, calc.divide, 9, 0) # Expect 9 / 0 = ValueError
                        
if __name__ == "__main__":
    unittest.main()