class StateMachine:

    def __init__(self):
        self.current_state = None

    def initialize(self, starting_state):
        self.current_state = starting_state
        self.current_state.enter()

    def change_state(self, new_state):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()
