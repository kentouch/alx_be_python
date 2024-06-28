

#### Pseudo code ####

# BEGIN

# INPUT: numb_1 (user input)
# INPUT: numb_2 = numb_1
# while numb > 0:
#       for x in range(1, numb_2 + 1):
#           print("*", end="")
#       print()
#       numb_1 = numb_1 - 1 


# END   


numb = int(input("Enter the size of the pattern:"))
numb_2 = numb

# each row has numb_2 number of stars
while numb > 0:
    # each row has numb_2 number of stars
    for x in range(1, numb_2 + 1):
        # print a star
        print("*", end="")
    print()
    numb = numb - 1