import os

from tabulate import tabulate

import database
import db_admin
import validate
from FSM.States.SignIn.sign_in_base_state import SignInParentState
from classes.accounts import AccountStatus
from classes.customer import CustomerStatus, Customer
import tkinter
from tkinter import *
from tkinter import messagebox



class SignInStateGUI(SignInState):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 7

    def enter(self):
        if self.id is not None:
            self.showUI()
        else:
            self.input_sign_in()
            if self.id is not None:
                self.showUI()
            else:
                self.selection = 0
                self.check_transitions()

    def check_transitions(self):
        if self.id is None:
            self.state_machine.change_state(self.app.main_menu)
        elif self.selection == 1:
            self.state_machine.change_state(self.app.address_update_state)
        elif self.selection == 2:
            self.state_machine.change_state(self.app.open_new_account_state)
        elif self.selection == 3:
            self.state_machine.change_state(self.app.manage_funds_customer_state)
        elif self.selection == 4:
            self.input_print_statement()
            # input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 5:
            self.close_account()
            self.showUI()
        elif self.selection == 6:
            self.change_password()
            # input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 7:
            self.view_all_accounts()
            # input("\nPress ENTER to continue...")
            self.showUI()
        elif self.selection == 0:
            self.set_id_all_states(None)
            self.state_machine.change_state(self.app.main_menu)

    def showUI(self):
        def value(x):
            self.selection = x
            self.check_transitions()

        self.app.tk_master.title("Main Menu")
        master = Frame(self.app.tk_master)
        self.main_frame = master
        master.pack()

        Label(master, text="MENU",justify='center').grid(row=0, columnspan=2, sticky='')
        Button(master, text="ADDRESS CHANGE", command=lambda: (value(1))) \
            .grid(row=1, sticky='')
        Button(master, text="OPEN NEW ACCOUNT", command=lambda: (value(2))) \
            .grid(row=2, sticky='')
        Button(master, text="MANAGE FUNDS", command=lambda: (value(3))) \
            .grid(row=3, sticky='')
        Button(master, text="PRINT STATEMENT", command=lambda: (value(4))) \
            .grid(row=4, sticky='')
        Button(master, text="ACCOUNT CLOSURE", command=lambda: (value(5))) \
            .grid(row=5, sticky='')
        Button(master, text="PASSWORD CHANGE", command=lambda: (value(6))) \
            .grid(row=6, sticky='')
        Button(master, text="VIEW ALL ACCOUNTS", command=lambda: (valuE(7))) \
            .grid(row=7, sticky='')
        Button(master, text="QUIT", command=lambda: (value(8))) \
            .grid(row=8, sticky='')
        self.app.tk_master.mainloop()

    def sign_in(self, c_id, password):
        if db_admin.check_customer_exists(c_id) is True:
            customer: Customer = database.get_all_info_customer(c_id)
            if customer.get_status() == CustomerStatus.locked.value:
                self.display_msg(["Sorry Your Account has been locked due to 3 unsuccessful login attempts"])
                return
            res = database.login_customer(c_id, password)
            if res:
                database.reset_login_attempts(c_id)
                self.set_id_all_states(c_id)
                self.display_msg(["Login Successful"])
            else:
                att = customer.get_login_attempts() - 1
                customer.set_login_attempts(att)
                database.update_customer(customer)
                self.display_msg(["Incorrect Password"])
        else:
            self.display_msg(["Customer doesn't exist"])

    def input_sign_in(self):
        try:

           e1=Entry(master)
           e1.grid(row=0,sticky='')
           e2=Entry(master)
           e2.grid(row=2,sticky='')
           a=int(e1.get())
           b=e2.get()
           self.sign_in(a,b)
        except:
            messagebox.showinfo("ERROR","INVALID ID")

    def logout(self):
        self.set_id_all_states(None)

    def set_id_all_states(self, _id):
        self.id = _id
        self.app.address_update_state.set_id(_id)
        self.app.open_new_account_state.set_id(_id)
        self.app.manage_funds_customer_state.set_id(_id)
        # TODO: Add more states when implemented

    def print_statement(self, acc_no, date_from, date_to):
        account = database.get_all_info_account(acc_no, self.id, "statement")
        if account is None:
            self.display_msg(["Invalid Account Number"])
            return
        if validate.validate_date(date_from, date_to):
            res = database.get_transactions_account(acc_no, date_from, date_to)
            self.display_table(res, ["Date", "Transaction Type", "Amount", "Balance", "Account Type"])
        else:
            self.display_msg(["Please Enter Valid Dates"])

    def input_print_statement(self):
        try:
            acc_no = int(input("Enter your account No\n"))
        except:
            self.display_msg(["Invalid Account No"])
            return
        print("Enter Dates in format (Year-Mon-Day) ")
        date_from = input("Date From : ")
        date_to = input("Date To : ")
        self.print_statement(acc_no, date_from, date_to)

    # Completely override in GUI
    def close_account(self):
        try:
            acc_no = int(input("\nEnter Account No to close : "))
        except:
            self.display_msg(["Invalid Account No"])
            return
        account = database.get_all_info_account(acc_no, self.id, AccountStatus.close.value)
        if account is not None:
            balacne = database.close_account_customer(account)
            self.display_msg(["Account closed successfully",
                              f"Rs {balacne} will be delivered to you shortly!"])
        else:
            self.display_msg(["\nSorry Account No doesn't match"])

    # Completely override in GUI
    def change_password(self):
        password = input("Enter New password (min 8 char and max 20 char)\n> ")
        while len(password) < 8 or len(password) > 20:
            print("Please Enter password in given range\n> ")
            password = input()
        database.change_password_customer(password, self.id)
        self.display_msg(["Password changed successfully!"])

    def view_all_accounts(self):
        res = database.get_customer_accounts(self.id)
        self.display_table(res, ["Account No", "Amount", "Opened On", "Status", "Type"])