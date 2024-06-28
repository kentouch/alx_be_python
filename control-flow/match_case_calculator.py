#### pseudo code ####

# BEGIN
# INPUT: f_num, s_num, operation (user input)
# match operation:
#       case "+":
#           result = f_num + s_num
#           OUTPUT: 'the result is' ,result
#       case "-":
#           result = f_num - s_num
#           OUTPUT: "the result is ", result
#       case "*":
#           result = f_num * s_num
#           OUTPUT: "the result is ", result
#       case "/":
#               if s_num > 0:
#                   result = f_num / s_num
#                   print("the result is", result)
#               else:
#                   print("Cannot dicide by zero")


# END


##### code ####

f_num = int(input("Enter first number: "))
s_num = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        result = f_num + s_num
        print("The result is", result)
    case "-":
        result = f_num - s_num
        print("The result is", result)
    case "*":
        result = f_num * s_num
        print("The result is", result)
    case "/":
        if s_num > 0:
            result = f_num / s_num
            print("The result is", result)
        else:
            print("Cannot divide by zero")