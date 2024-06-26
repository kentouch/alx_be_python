

##### Pseudo code #####
# BEGIN
# Input:grade
# match grade:
#        case 80-90:
#            print("A")
#        case 70-80:
#            print("B")
#        case 60-70:
#            print("C")
#        case 50-60:
#            print("D")
#        case 0-50:
#            print("F")
#        case _:
#            print("Invalid grade")
# END



grade = int(input("Enter your grade:"))

match grade:
    # case grade in range(80, 91):
    case grade if grade in range(80, 91):
        print("Congratulations, you got A")
    # case grade in range(70, 81):
    case grade if grade in range(70, 81):
        print("Perfect, you got B")
    # case grade in range(60, 71):
    case grade if grade in range(60, 71):
        print("Good job, you got C")
    # case grade in range(50, 61):
    case grade if grade in range(50, 61):
        print("Try your best next time, you got D")
    # case grade in range(0, 51):
    case grade if grade in range(0, 51):
        print("Sorry, you got F")
    # case _:
    case _:
        print("Invalid grade")
