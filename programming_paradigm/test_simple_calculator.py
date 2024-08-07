# Test script for simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """ Test cases for arithmetic operations made in a calculator """

    # set up means to run before each test
    def setUp(self):
        self.calc = SimpleCalculator()
    
    # test addition operation
    def test_addition(self):
        # positive numbers as input
        self.assertEqual(self.calc.addition(2, 3), 5)
        # negative number as input
        self.assertEqual(self.calc.addition(2, -3), -1)
    # test substraction
    def test_subtraction(self):
        # positive numbers as input 
        self.assertEqual(self.calc.subtract(4, 5), -1)
        # negative numbers as input
        self.assertEqual(self.calc.subtract(4, -7), 11)
    # test multiplication
    def test_multiplication(self):
        # positive numbers as input
        self.assertEqual(self.calc.multiply(3, 9), 27)
        # negative numbers as input
        self.assertEqual(self.calc.multiply(3, -5), -15)
    
    # test division
    def test_division(self):
        # positive numbers as input
        self.assertEqual(self.calc.divide(8, 4), 2)
        # negative numbers as input
        self.assertEqual(self.calc.divide(8, -4), -2)
        # negative numbers as input
        self.assertEqual(self.calc.divide(8, 0),"Error: Cannot divide by zero.")

if __name__=="__main__":
    unittest.main()
        