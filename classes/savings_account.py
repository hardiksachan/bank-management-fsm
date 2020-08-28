from classes.accounts import Account


class Savings(Account):
    interest = 7.5
    min_balance = 0

    def open_account(self, amount):
        if amount < 0:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def deposit(self, amount):
        if amount < 0:
            print("Please input a valid amount")
            return False
        else:
            self.balance += amount
            return True

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry You don't have enough balance")
            return False
        else:
            self.balance -= amount
            return True