
# Explore datetime module
# let's import the datetime module

from datetime import datetime, timedelta, date
# Create a function that prints the current date
def display_current_datetime():
    """ Display the current date and time"""
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current dates and time: {current_date}")


# create a function that calculate a future date
def calculate_future_date():
    """ Display a future date """
    numbers_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days = numbers_of_days) + date.today()
    print("The future date: ", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()