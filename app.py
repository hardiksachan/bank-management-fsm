import sys

from FSM.States.exit_state import ExitState
from FSM.States.main_menu_state import MainMenuState
from FSM.States.sign_up_state import SignUpState
from FSM.state_machine import StateMachine


class App:
    main_menu: MainMenuState
    state_Machine: StateMachine

    def __init__(self):
        self.state_Machine = StateMachine()
        self.main_menu = MainMenuState(self.state_Machine, self)
        self.exit_state = ExitState(self.state_Machine, self)
        self.sign_up_state = SignUpState(self.state_Machine, self)
