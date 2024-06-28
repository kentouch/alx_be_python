

#### Pseudo code ####

# BEGIN

# INPUT: task, priority, time_bound
# match priority:
#       case 'high':
#           OUTPUT: "task is a high priority"
#       case 'medium':
#           OUTPUT: "task is a meium priority"
#       case 'low':
#           OUTPUT: "task is a low priority"
# END


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires you immediate attention today ")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a meium priority task that requires you immediate attention today ")
        else:
            print(f"Note: '{task}' is a meium priority. Consider completing it when you have free time")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low priority task that requires you immediate attention today ")
        else:
            print(f"Note: '{task}' is a low priority. Consider completing it when you have free time")
    case _:
        print("Invalid input")
