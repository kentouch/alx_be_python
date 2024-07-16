# Implement a division calculator that robustly handles errors 
# like division by zero and non-numeric inputs 
# using command line arguments.


# Function to divide two numbers
def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            # Raise an exception if the denominator is zero
            raise ZeroDivisionError
        else:
            try:
                # Attempt to convert numerator and denominator to floats
                product = float(numerator) / float(denominator)
                return f"The result of the division is {product}"
            except ValueError:
                return "Error: Please enter numeric values only."
            
    # Handle the ZeroDivisionError exception    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

  

