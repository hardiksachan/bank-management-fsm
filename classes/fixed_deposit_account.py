from classes.accounts import Account


class FixedDeposit(Account):
    min_balance = 1000

    def open_account(self, amount):
        if amount < self.min_balance:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def set_deposit_term(self, term):
        self.deposit_term = term

    def get_deposit_term(self):
        return self.deposit_term
