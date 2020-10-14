from ScreenManager.Screens.screen import Screen


class MainMenuScreen(Screen):

    def __init__(self, screen_manager, app):
        super().__init__(screen_manager, app)
        self.lower_bound = 0
        self.upper_bound = 2

    def enter(self):
        self.showUI()
        self.update_selection()

    def showUI(self):
        print("--- Main Menu --- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("0. Quit ")

    def check_transitions(self):
        if self.selection == 0:
            self.screen_manager.change_screen(self.app.exit_screen)
        elif self.selection == 1:
            self.screen_manager.change_screen(self.app.sign_up_screen)
        elif self.selection == 2:
            self.screen_manager.change_screen(self.app.sign_in_screen)
