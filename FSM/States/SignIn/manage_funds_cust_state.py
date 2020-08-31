import os

from tabulate import tabulate

import database
import db_admin
from FSM.States.SignIn.sign_in_base_state import SignInParentState


class ManageFundsCustomerState(SignInParentState):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 4

    def check_transitions(self):
        if self.selection == 1:
            self.deposit_money()
            input("\nPress ENTER to continue...")
            self.showUI()
            self.update_selection()
        elif self.selection == 2:
            self.withdraw_money()
            input("\nPress ENTER to continue...")
            self.showUI()
            self.update_selection()
        elif self.selection == 3:
            self.transfer_money()
            input("\nPress ENTER to continue...")
            self.showUI()
            self.update_selection()
        elif self.selection == 4:
            self.avail_loan()
            input("\nPress ENTER to continue...")
            self.showUI()
            self.update_selection()
        elif self.selection == 0:
            self.state_machine.change_state(self.app.sign_in_state)

    def showUI(self):
        os.system('cls||clear')
        print("\n --- Menu --- ")
        print("1. Money Deposit")
        print("2. Money Withdrawal")
        print("3. Transfer Money")
        print("4. Avail Loan")
        print("0. Exit")

    def deposit_money(self):
        try:
            acc_no = int(input("Enter your account No\n> "))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, self.id, "deposit")
        if account is not None:
            try:
                amount = int(input("Enter amount to Deposit\n> "))
            except:
                print("Invalid Amount")
                return
            if account.deposit(amount):
                database.money_deposit_customer(account, amount)
                print("Rs ", amount, "Successfully deposited")
                print("Balance : Rs ", account.get_balance())

        else:
            print("Sorry Account No doesn't match")

    def withdraw_money(self):
        try:
            acc_no = int(input("Enter your account No\n> "))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, self.id, "withdraw")
        if account is not None:
            if account.get_withdrawals_left() == 0 and account.get_account_type() == "savings":
                print("Sorry You have exceeded withdrawals(10) for this month")

            else:
                try:
                    amount = int(input("Enter amount to Withdraw\n> "))
                except:
                    print("Invalid Amount")
                    return
                if account.withdraw(amount):
                    database.money_withdraw_customer(account, amount, "withdraw")
                    print("Rs ", amount, "Successfully withdrawn")
                    print("Balance : Rs ", account.get_balance())

        else:
            print("Sorry Account No doesn't match")

    def transfer_money(self):
        try:
            acc_no_sender = int(input("Enter Account No From : "))
        except:
            print("Invalid Account No")
            return
        account_sender = database.get_all_info_account(acc_no_sender, self.id, "withdraw")
        if account_sender is not None:
            try:
                acc_no_receiver = int(input("Enter Account No To Transfer Money To : "))
            except:
                print("Invalid Account No")
                return
            account_receiver = database.get_all_info_account(acc_no_receiver, -1, "transfer")
            if account_receiver is not None:
                try:
                    amount = int(input("\nEnter Amount To Transfer : "))
                except:
                    print("Invalid Amount")
                    return
                database.transfer_money_customer(account_sender, account_receiver, amount)
            else:
                print("Sorry Account doesn't exist")

        else:
            print("Sorry Account No doesn't match")

    def avail_loan(self):
        try:
            acc_no = int(input("\nEnter Your Savings Account No : "))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, self.id, "loan")
        if account is not None:
            max_loan = 2 * account.get_balance()
            msg = "\nEnter loan amount (Max Amount : Rs " + str(max_loan) + " ) (in multiples of 1000) : "
            try:
                loan_amt = int(input(msg))
            except:
                print("Invalid Amount")
                return
            if max_loan >= loan_amt > 0 and loan_amt % 1000 == 0:
                try:
                    loan_term = int(input("\nEnter repayment term (in months) : "))
                except:
                    print("Invalid repayment term")
                    return
                if loan_term > 0:
                    database.get_loan_customer(account.get_account_no(), loan_amt, loan_term)
                    res = db_admin.get_loan_report(self.id)
                    print(tabulate(res, headers=["Account No", "Amount", "Repay Term"], tablefmt="pretty"))
                else:
                    print("Sorry ! Invalid Loan Term")

            else:
                print("Sorry ! Invalid Loan Amount")

        else:
            print("Sorry! Account No Doesn't match")