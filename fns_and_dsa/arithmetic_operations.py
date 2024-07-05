# Python script for Arithmetic operations

def perform_operation(num1, num2, operation):
    '''match the input operation with elif'''
         if operation == 'add':
            return num1 + num2
         elif operation == 'subtract':
            return num1 - num2
         elif operation == 'multiply':
            return num1 * num2
         elif operation == 'divide' and num2 != 0:
            return num1/num2
         else:
            return "invalid operation input"


