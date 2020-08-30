import os

import database
import db_admin
from FSM.States.state import State
from classes.customer import CustomerStatus, Customer


class SignInState(State):
    id: int

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.id = None
        self.lower_bound = 0
        self.upper_bound = 5

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
            self.state_machine.change_state(self.app.main_menu)
        elif self.selection == 1:
            # self.app.address_update_state.set_id(self.id)
            self.state_machine.change_state(self.app.address_update_state)
        elif self.selection == 2:
            # self.app.open_new_account_state.set_id(self.id)
            self.state_machine.change_state(self.app.open_new_account_state)
        elif self.selection == 0:
            self.set_id_all_states(None)
            self.state_machine.change_state(self.app.main_menu)
        else:
            self.state_machine.change_state(self.app.main_menu)

    def showUI(self):
        os.system('cls||clear')
        print("\n--- Menu ---")
        print("1. Address Change")
        print("2. Open New Account")
        print("3. Manage Funds")
        print("4. Print Statement")
        print("5. Account Closure")
        print("0. Logout")
        self.update_selection()

    def set_id(self, id):
        self.id = id

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
                self.set_id_all_states(id)
                print("Login Successful")
            else:
                att = customer.get_login_attempts() - 1
                customer.set_login_attempts(att)
                database.update_customer(customer)
                print("Incorrect Password")
        else:
            print("Customer doesn't exist")

    def logout(self):
        self.set_id_all_states(None)

    def set_id_all_states(self, _id):
        self.id = _id
        self.app.address_update_state.set_id(_id)
        self.app.open_new_account_state.set_id(_id)
        # TODO: Add more states when implemented
