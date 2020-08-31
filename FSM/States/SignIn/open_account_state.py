import os

from tabulate import tabulate

import database
import db_admin
from FSM.States.SignIn.sign_in_base_state import SignInParentState
from classes.accounts import AccountType
from classes.current_account import Current
from classes.fixed_deposit_account import FixedDeposit
from classes.savings_account import Savings


class OpenAccountState(SignInParentState):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 3

    def check_transitions(self):
        if self.selection == 0:
            # self.app.sign_in_state.set_id(self.id)
            self.state_machine.change_state(self.app.sign_in_state)
        else:
            self.open_new_account()
            input("\nPress ENTER to continue...")
            self.showUI()
            self.update_selection()

    def showUI(self):
        os.system('cls||clear')
        print("\n --- Menu --- ")
        print("1. Open Savings Account")
        print("2. Open Current Account")
        print("3. Open Fixed Deposit Account")
        print("0. Exit")

    def get_new_account(self):
        msg = "Enter Balance "
        term = None
        if self.selection == 1:
            account = Savings()
            acc_type = AccountType.savings
            msg += ": "
        elif self.selection == 2:
            account = Current()
            acc_type = AccountType.current
            msg += "(min 5000) : "
        elif self.selection == 3:
            account = FixedDeposit()
            acc_type = AccountType.fd
            msg += "(min 1000) : "
        else:
            return None

        balance = int(input(msg))
        while not account.open_account(balance):
            balance = int(input("\nEnter Valid Balance : "))

        if self.selection == 3:
            try:
                term = int(input("\nEnter Deposit Term (Min 12 months) : "))
            except:
                print("Invalid Deposit term")
                return
            while term < 12:
                term = int(input("Please Enter a valid Deposit Term\n"))

        account.set_account_type(acc_type)
        if isinstance(account, FixedDeposit):
            account.set_deposit_term(term)
        return account

    def open_new_account(self):
        account = self.get_new_account()
        if account is not None:
            database.open_new_account_customer(account, self.id)
            if self.selection == 3:
                res = db_admin.get_fd_report(self.id)
                print(res)
                print(tabulate(res, headers=["Account No", "Amount", "Deposit Term"], tablefmt="pretty"))

        else:
            print("Invalid Choice")
