import sys

import tkinter

from FSM.States.SignIn.change_address_state import ChangeAddressState
from FSM.States.SignIn.manage_funds_cust_state import ManageFundsCustomerState
from FSM.States.SignIn.open_account_state import OpenAccountState
from FSM.States.SignIn.sign_in_menu_state import SignInState
from FSM.States.SignIn.sign_in_menu_state_gui import SignInStateGUI
from FSM.States.exit_state import ExitState
from FSM.States.main_menu_state import MainMenuState
from FSM.States.main_menu_state_gui import MainMenuStateGUI
from FSM.States.sign_up_state_gui import SignUpStateGUI
from FSM.state_machine import StateMachine


class App:

    def __init__(self):
        self.state_Machine = StateMachine()

        self.tk_master = tkinter.Tk()
        self.tk_master.geometry("300x300")

        self.main_menu = MainMenuStateGUI(self.state_Machine, self)
        self.sign_up_state = SignUpStateGUI(self.state_Machine, self)
        self.sign_in_state = SignInStateGUI(self.state_Machine, self)
        self.exit_state = ExitState(self.state_Machine, self)
        self.address_update_state = ChangeAddressState(self.state_Machine, self)
        self.open_new_account_state = OpenAccountState(self.state_Machine, self)
        self.manage_funds_customer_state = ManageFundsCustomerState(self.state_Machine, self)