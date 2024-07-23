#### class and static methods in python
## @decorators


# class calculator
class Calculator:
    # class attribute 
    calculation_type = "Arithmetic Operations"
    # class method
    @staticmethod
    def add(x, y):
        return x + y
    # static method
    @classmethod
    def multiply(cls, x, y):
        print(f"Calculation type: {cls.calculation_type}")
        return x * y