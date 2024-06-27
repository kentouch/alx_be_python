##### Pseudo code #####

# BEGIN
# INPUT: random_number (random_randint(1, 10))
# def get_random_number():
#   count = 0
#   while TRUE:
        #guess_number: int(input("Enter your guess: "))
        #match guess_number:
        #       case guess_number if guess_number == random_number:
        #               OUTPUT: correct guess
        #               OUTPUT: break
        #       case guess_number if guess_number > random_number:
        #               OUTPUT: too high
        #       case guess_number if guess_number < random_number:
        #               OUTPUT: too low
        #       case _:
        #               OUTPUT: invalid input
#       redo = (input("Try again, yes or no? "))
#       if redo.lower() == "no":
#               OUTPUT: break
#       else:
#               OUTPUT: continue
#       count ++
#   OUTPUT: count
# get_random_number()
# END


##### Code ####

import random

random_number = random.randint(1, 10)


def get_random_number():
    # the number of times the user has guessed is now 0
    count = 0
    # the user has to guess a number a number of times he wants
    while True:
        count += 1
        # input your guess number
        guess_number = int(input("Enter your guess: "))
        match guess_number:
            # case when you're you guessed id
            case guess_number if guess_number == random_number:
                print("Congratulations, you guessed it!")
                break
            # case when you guessed a number over the random one
            case guess_number if guess_number > random_number:
                print("Oops your number is Too high")
            # case when you guessed a number below the random one
            case guess_number if guess_number < random_number:
                print("Nope try again, your number is Too low")
            case _:
                print("Invalid input")
                
        print("The number is ", random_number)
        redo = input("Try again, yes or no? ")
        if redo.lower() == "no":
            break
        elif redo.lower() == "yes":
            continue
        else:
            print("Invalid input")
            break
        

    print("")
    print("The number of guess is: ", count)



    

get_random_number()
