##### Pseudo code #####
# BEGIN
# INPUT: age
# function has_id(user):
#       return user["id"]
#
# match age:
#       case age if age >= 18 and has_id(user):
#                   OUTPUT: eligible to vote
#           else:
#                   OUTPUT: not eligible to vote
#       case _:
#           OUTPUT: not eligible to vote
# END



def has_id(user):
    return user["id"]


user = {"id": True}
age = int(input("Enter your age: "))

match age:
    case age if age >= 18 and has_id(user):
        print("eligible to vote")
    case _:
        print("not eligible to vote")