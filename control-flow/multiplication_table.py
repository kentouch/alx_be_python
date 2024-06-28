#### Pseudo code ####

# BEGIN
# INPUT: x (user input)
# for y in range(1, 11):
#       z = x * y
#       OUTPUT: x, "*" , y, "=", z
# END


number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    z = number * y
    print(number, "*", y, "=", z)