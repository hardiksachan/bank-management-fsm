import sys

from FSM.States.SignIn.change_address_state import ChangeAddressState
from FSM.States.SignIn.manage_funds_cust_state import ManageFundsCustomerState
from FSM.States.SignIn.open_account_state import OpenAccountState
from FSM.States.SignIn.sign_in_menu_state import SignInState
from FSM.States.exit_state import ExitState
from FSM.States.main_menu_state import MainMenuState
from FSM.States.sign_up_state_gui import SignUpStateGUI
from FSM.state_machine import StateMachine


class App:
    main_menu: MainMenuState
    state_Machine: StateMachine

    def __init__(self):
        self.state_Machine = StateMachine()
        self.main_menu = MainMenuState(self.state_Machine, self)
        self.exit_state = ExitState(self.state_Machine, self)
        self.sign_up_state = SignUpStateGUI(self.state_Machine, self)
        self.sign_in_state = SignInState(self.state_Machine, self)
        self.address_update_state = ChangeAddressState(self.state_Machine, self)
        self.open_new_account_state = OpenAccountState(self.state_Machine, self)
        self.manage_funds_customer_state = ManageFundsCustomerState(self.state_Machine, self)