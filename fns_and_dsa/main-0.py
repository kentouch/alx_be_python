import sys

from bank_account import BankAccount

def main():
    print("Welcome to the Bank!")
    # Create an instance of BankAccount
    account = BankAccount(100)  # Example starting balance of $100
    # Check if the user entered a command and amount
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        # Exit the program if the user did not enter a command and amount
        # sys.exit(1) is meaning exit with error
        sys.exit(1)

    # Get the command and amount from the user
    command, *params = sys.argv[1].split(':')
    # Call the appropriate function based on the command and amount
    amount = float(params[0]) if params else None
    # ]if the command is "deposit" and amount is not None:
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    # if the command is "withdraw" and amount is not None:
    elif command == "withdraw" and amount is not None:
        # Call the withdraw method of the BankAccount class
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    # if the command is "display"
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
# Call the main function if the script is being run directly
if __name__ == "__main__":
    main()