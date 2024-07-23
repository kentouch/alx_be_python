#### class and static methods in python
## @decorators


# class calculator
class Calculator:
    # class attribute 
    calculation_type = "Arithmetic Operations"
    # class method
    @staticmethod
    def add(a, b):
        return a + b
    # static method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b