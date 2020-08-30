import os

import database
from FSM.States.state import State
from classes.accounts import AccountType
from classes.current_account import Current
from classes.fixed_deposit_account import FixedDeposit
from classes.savings_account import Savings


class OpenAccountState(State):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.id = None
        self.lower_bound = 0
        self.upper_bound = 3

    def enter(self):
        if self.id is None:
            print("Please Sign In First!")
            input("Press ENTER to continue...")
            self.state_machine.change_state(self.app.sign_in_state)
        self.showUI()
        self.update_selection()

    def check_transitions(self):
        if self.selection == 0:
            # self.app.sign_in_state.set_id(self.id)
            self.state_machine.change_state(self.app.sign_in_state)
        else:
            self.open_new_account()
            self.showUI()
            self.update_selection()

    def showUI(self):
        os.system('cls||clear')
        print("\n --- Menu --- ")
        print("1. Open Savings Account")
        print("2. Open Current Account")
        print("3. Open Fixed Deposit Account")
        print("0. Exit")

    def set_id(self, _id):
        self.id = _id

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
            # if ch == 3:
            #     res = db_admin.get_fd_report(id)
            #     print("Account No \t\t\t\t Amount \t\t\t\t Deposit Term")
            #     for i in range(0, len(res)):
            #         print(res[i][0], "   \t\t\t\t\t   ", res[i][1], "   \t\t\t\t   ", res[i][2])

        else:
            print("Invalid Choice")

        input("\nPress ENTER to continue...")