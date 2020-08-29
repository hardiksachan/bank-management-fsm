from FSM.States.state import State


class MainMenuState(State):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 3

    def enter(self):
        super().enter()
        self.update_selection()

    def showUI(self):
        print("--- Main Menu --- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("3. Admin Sign In ")
        print("0. Quit ")

    def check_transitions(self):
        if self.selection == 0:
            self.state_machine.change_state(self.app.exit_state)
        elif self.selection == 1:
            self.state_machine.change_state(self.app.sign_up_state)
        elif self.selection == 2:
            self.state_machine.change_state(self.app.sign_in_state)
        elif self.selection == 3:
            self.state_machine.change_state(self.app.admin_sign_in_state)
