import os

import database
from FSM.States.state import State


class ChangeAddressState(State):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.id = None
        self.lower_bound = 0
        self.upper_bound = 5

    def enter(self):
        if self.id is None:
            print("Please Sign In First!")
            input("Press ENTER to continue...")
            self.state_machine.change_state(self.app.sign_in_state)
        self.showUI()
        self.update_selection()

    def check_transitions(self):
        if self.selection == 0:
            self.app.sign_in_state.set_id(self.id)
            self.state_machine.change_state(self.app.sign_in_state)
        else:
            self.update_address()

    def showUI(self):
        os.system('cls||clear')
        print("-- Menu --")
        print("1. Change Address Line 1")
        print("2. Change Address Line 2")
        print("3. Change State")
        print("4. Change City")
        print("5. Change Pincode")
        print("0. Go Back")

    def set_id(self, _id):
        self.id = _id

    def update_address(self):
        ch = self.selection
        if not (1 <= ch <= 5):
            self.showUI()
            self.update_selection()
            return

        if ch == 1:
            addr = input("Enter New Address Line 1\n> ")
        elif ch == 2:
            addr = input("Enter New Address Line 2\n> ")
        elif ch == 3:
            addr = input("Enter New State\n> ")
        elif ch == 4:
            addr = input("Enter New City\n> ")
        elif ch == 5:
            addr = input("Enter New Pincode\n> ")

        database.change_address_customer(ch, self.id, addr)
        input("\nPress ENTER to continue...")
        self.showUI()
        self.update_selection()
