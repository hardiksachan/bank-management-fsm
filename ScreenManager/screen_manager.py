class ScreenManager:

    def __init__(self):
        self.current_screen = None

    def initialize(self, starting_state):
        self.current_screen = starting_state
        self.current_screen.enter()

    def change_screen(self, new_state):
        self.current_screen.exit()
        self.current_screen = new_state
        self.current_screen.enter()
