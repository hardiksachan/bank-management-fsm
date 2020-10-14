from abc import ABC

from ScreenManager.Screens.screen import Screen


class SignInParentScreen(Screen, ABC):
    def __init__(self, screen_manager, app):
        super().__init__(screen_manager, app)
        self.id = None

    def set_id(self, _id):
        self.id = _id

    def enter(self):
        if self.id is None:
            print("Please Sign In First!")
            input("Press ENTER to continue...")
            self.screen_manager.change_screen(self.app.sign_in_screen)
        self.showUI()
        self.update_selection()
