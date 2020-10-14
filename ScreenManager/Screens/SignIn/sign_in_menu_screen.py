import os

from tabulate import tabulate

import database
import db_admin
import validate
from ScreenManager.Screens.SignIn.sign_in_base_screen import SignInParentScreen
from classes.accounts import AccountStatus
from classes.customer import CustomerStatus, Customer


class SignInScreen(SignInParentScreen):
    def __init__(self, screen_manager, app):
        super().__init__(screen_manager, app)
        self.lower_bound = 0
        self.upper_bound = 7

    def enter(self):
        if self.id is not None:
            self.showUI()
        else:
            self.sign_in()
            if self.id is not None:
                self.showUI()
            else:
                self.selection = 0
                self.check_transitions()

    def check_transitions(self):
        if self.id is None:
            self.screen_manager.change_screen(self.app.main_menu)
        elif self.selection == 1:
            self.screen_manager.change_screen(self.app.address_update_screen)
        elif self.selection == 2:
            self.screen_manager.change_screen(self.app.open_new_account_screen)
        elif self.selection == 3:
            self.screen_manager.change_screen(self.app.manage_funds_customer_screen)
        elif self.selection == 4:
            self.print_statement()
            input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 5:
            self.close_account()
            input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 6:
            self.change_password()
            input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 7:
            self.view_all_accounts()
            input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 0:
            self.set_id_for_all_screens(None)
            self.screen_manager.change_screen(self.app.main_menu)
        else:
            self.screen_manager.change_screen(self.app.main_menu)

    def showUI(self):
        os.system('cls||clear')
        print("\n--- Menu ---")
        print("1. Address Change")
        print("2. Open New Account")
        print("3. Manage Funds")
        print("4. Print Statement")
        print("5. Account Closure")
        print("6. Password Change")
        print("7. View All Accounts")
        print("0. Logout")
        self.update_selection()

    def sign_in(self):
        try:
            id = int(input("Enter Customer ID\n> "))
        except:
            print("Invalid ID")
            return

        if db_admin.check_customer_exists(id) is True:
            customer: Customer = database.get_all_info_customer(id)
            if customer.get_status() == CustomerStatus.locked.value:
                print("Sorry Your Account has been locked due to 3 unsuccessful login attempts")
                return
            password = input("Enter Password\n> ")
            res = database.login_customer(id, password)
            if res:
                database.reset_login_attempts(id)
                self.set_id_for_all_screens(id)
                print("Login Successful")
            else:
                att = customer.get_login_attempts() - 1
                customer.set_login_attempts(att)
                database.update_customer(customer)
                print("Incorrect Password")
                input("\nPress ENTER to continue...")
        else:
            print("Customer doesn't exist")

    def logout(self):
        self.set_id_for_all_screens(None)

    def set_id_for_all_screens(self, _id):
        self.id = _id
        self.app.address_update_screen.set_id(_id)
        self.app.open_new_account_screen.set_id(_id)
        self.app.manage_funds_customer_screen.set_id(_id)
        # TODO: Add more states when implemented

    def print_statement(self):
        try:
            acc_no = int(input("Enter your account No\n"))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, self.id, "statement")
        if account is not None:
            print("Enter Dates in format (Year-Mon-Day) ")
            date_from = input("Date From : ")
            date_to = input("Date To : ")
            if validate.validate_date(date_from, date_to):
                res = database.get_transactions_account(acc_no, date_from, date_to)
                print(tabulate(res, headers=["Date", "Transaction Type", "Amount", "Balance", "Account Type"],
                               tablefmt="pretty"))
            else:
                print("Please Enter Valid Dates")

    def close_account(self):
        try:
            acc_no = int(input("\nEnter Account No to close : "))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, self.id, AccountStatus.close.value)
        if account is not None:
            database.close_account_customer(account)
        else:
            print("\nSorry Account No doesn't match")

    def change_password(self):
        password = input("Enter New password (min 8 char and max 20 char)\n> ")
        while len(password) < 8 or len(password) > 20:
            print("Please Enter password in given range\n> ")
            password = input()

        database.change_password_customer(password, self.id)

    def view_all_accounts(self):
        res = database.get_customer_accounts(self.id)
        print(tabulate(res, headers=["Account No", "Amount", "Opened On", "Status", "Type"], tablefmt="pretty"))
