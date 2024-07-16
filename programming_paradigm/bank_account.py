### implementing a banking account class encapsulating banking operations
# creates a class called BankingAccount
# initialize the account balance
# implementation of methods such deposit(), withdraw(), show_balance()

class BankAccount:
    # initialize he 
    def __init__(self, account_balance=0):
        self._account_balance = account_balance

    # implement a deposit method using a parameter called amount
    def deposit(self, amount):
        # add the amount to the account balance
        self._account_balance = self._account_balance + amount
    
    # implement a withdraw method using a parameter called amount
    def withdraw(self, amount):
        if amount > self._account_balance:
            return False
        else:
            # subtract the amount from the account balance
            self._account_balance = self._account_balance - amount
            return True

    # implement a display_balance method using a parameter called amount
    def display_balance(self):
        print(f"Current Balance:{float(self._account_balance)}") 

