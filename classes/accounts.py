from abc import ABC


class Account(ABC):

    def set_account_no(self, acc_no):
        self.account_no = acc_no

    def set_account_type(self, type):
        self.type = type

    def set_balance(self, bal):
        self.balance = bal

    def set_withdrawals_left(self, wd):
        self.withdrawals_left = wd

    def get_account_no(self):
        return self.account_no

    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return self.type

    def get_withdrawals_left(self):
        return self.withdrawals_left