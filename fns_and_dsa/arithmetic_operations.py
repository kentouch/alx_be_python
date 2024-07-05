# Python script for Arithmetic operations

def perform_operation(num1, num2, operation):
    '''match the input operation'''
    match operation:
        case operation if operation == 'add':
            return num1 + num2
        case operation if operation == 'subtract':
            return num1 - num2
        case operation if operation == 'multiply':
            return num1 * num2
        case operation if operation == 'divide':
            if num2 != 0:
                return num1/num2
            else:
                return "no number is divisible by zero"
        case _:
            return 'Invalid operation'


