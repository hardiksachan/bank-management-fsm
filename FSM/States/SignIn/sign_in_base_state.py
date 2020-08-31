from abc import ABC

from FSM.States.state import State


class SignInParentState(State, ABC):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.id = None

    def set_id(self, _id):
        self.id = _id

    def enter(self):
        if self.id is None:
            print("Please Sign In First!")
            input("Press ENTER to continue...")
            self.state_machine.change_state(self.app.sign_in_state)
        self.showUI()
        self.update_selection()
