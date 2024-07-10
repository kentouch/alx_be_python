# python script

# Global variable for keeping values factor

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# this function takes an input from fahrenheit to celcius
def convert_to_celsius(fahrenheit):
    """ convert to celsius """
    # formular to convert from fahrenheit in celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{fahrenheit} F is {celsius} C")

# this function takes an input from celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    """ convert to fahrenheit """
    # formular to convert from celsius to fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius} C is {fahrenheit} F")

def main ():
    temperature = float(input("Enter the temperature to convert: "))
    fahrenheit_or_celsius = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if fahrenheit_or_celsius == "C":
        convert_to_fahrenheit(temperature)
    elif fahrenheit_or_celsius == "F":
        convert_to_celsius(temperature)
    else:
        print("Invalid temperature, Please enter a numeric value .")

if __name__=="__main__":
    main()

