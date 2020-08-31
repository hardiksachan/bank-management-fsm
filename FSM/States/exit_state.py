import sys

from FSM.States.state import State


class ExitState(State):

    def enter(self):
        self.showUI()

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)

    def showUI(self):
        print("Bye!!")
        self.exit()

    def exit(self):
        raise SystemExit(0)

    def check_transitions(self):
        pass
