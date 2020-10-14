from ScreenManager.Screens.SignIn.change_address_screen import ChangeAddressScreen
from ScreenManager.Screens.SignIn.manage_funds_cust_screen import ManageFundsCustomerScreen
from ScreenManager.Screens.SignIn.open_account_screen import OpenAccountScreen
from ScreenManager.Screens.SignIn.sign_in_menu_screen import SignInScreen
from ScreenManager.Screens.exit_screen import ExitScreen
from ScreenManager.Screens.main_menu_screen import MainMenuScreen
from ScreenManager.Screens.sign_up_state import SignUpScreen
from ScreenManager.screen_manager import ScreenManager


class App:
    main_menu: MainMenuScreen
    screen_manager: ScreenManager

    def __init__(self):
        self.screen_manager = ScreenManager()
        self.main_menu = MainMenuScreen(self.screen_manager, self)
        self.exit_screen = ExitScreen(self.screen_manager, self)
        self.sign_up_screen = SignUpScreen(self.screen_manager, self)
        self.sign_in_screen = SignInScreen(self.screen_manager, self)
        self.address_update_screen = ChangeAddressScreen(self.screen_manager, self)
        self.open_new_account_screen = OpenAccountScreen(self.screen_manager, self)
        self.manage_funds_customer_screen = ManageFundsCustomerScreen(self.screen_manager, self)
