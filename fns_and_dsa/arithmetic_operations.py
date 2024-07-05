# Python script for Arithmetic operations

def perform_operation(num1, num2, operation):
    '''match the input operation with elif'''
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "no number is divisible by zero"
        else:
            return num1/num2
    else:
        return "invalid operation input"


