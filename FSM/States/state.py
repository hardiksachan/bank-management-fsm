import os
from abc import abstractmethod, ABC

from FSM.state_machine import StateMachine


class State(ABC):
    state_machine: StateMachine

    def __init__(self, state_machine, app):
        self.state_machine = state_machine
        self.app = app
        self.selection = -1
        self.lower_bound = -1
        self.upper_bound = -1

    @abstractmethod
    def enter(self):
        pass

    def exit(self):
        os.system('cls||clear')

    def update_selection(self):
        try:
            sel = int(input("\n> "))
        except:
            print("Invalid Choice")
            self.update_selection()
        while not(self.lower_bound <= sel <= self.upper_bound):
            print("Invalid Choice")
            try:
                sel = int(input("> "))
            except:
                print("Invalid Choice")
        self.selection = sel
        self.check_transitions()

    @abstractmethod
    def check_transitions(self):
        pass

    @abstractmethod
    def showUI(self):
        pass
