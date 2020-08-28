from classes.accounts import Account


class Current(Account):
    interest = 0
    min_balance = 5000

    def open_account(self, amount):
        if amount < self.min_balance:
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
        elif self.balance - amount < 5000:
            print("Sorry You can't withdraw this much money as you need at least Rs", self.min_balance,
                  " to maintain this account")
            return False
        else:
            self.balance -= amount
            return True
