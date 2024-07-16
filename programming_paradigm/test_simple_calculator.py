# Test script for simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """ Test cases for arithmetic operations made in a calculator """

    # set up means to run before each test
    def setUp(self):
        self.calc = SimpleCalculator()
    
    # test addition operation
    def testAdd(self):
        # positive numbers as input
        self.assertEqual(self.calc.add(2, 3), 5)
        # negative number as input
        self.assertEqual(self.calc.add(2, -3), -1)
    # test substraction
    def testSub(self):
        # positive numbers as input 
        self.assertEqual(self.calc.sub(4, 5), -1)
        # negative numbers as input
        self.assertEqual(self.calc.sub(4, -7), 11)
    # test multiplication
    def testMult(self):
        # positive numbers as input
        self.assertEqual(self.calc.mult(3, 9), 27)
        # negative numbers as input
        self.assertEqual(self.calc.mult(3, -5), -15)
    
    # test division
    def testDiv(self):
        # positive numbers as input
        self.assertEqual(self.calc.div(8, 4), 2)
        # negative numbers as input
        self.assertEqual(self.calc.div(8, -4), -2)
        # negative numbers as input
        self.assertEqual(self.calc.div(8, 0),"Error: Cannot divide by zero.")

if __name__=="__main__":
    unittest.main()
        