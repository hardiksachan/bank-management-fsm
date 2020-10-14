from ScreenManager.Screens.screen import Screen


class ExitScreen(Screen):

    def enter(self):
        self.showUI()

    def __init__(self, screen_manager, app):
        super().__init__(screen_manager, app)

    def showUI(self):
        print("Bye!!")
        self.exit()

    def exit(self):
        raise SystemExit(0)

    def check_transitions(self):
        pass
