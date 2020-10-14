import database
from ScreenManager.Screens.screen import Screen
from classes.Address import Address
from classes.customer import Customer, CustomerStatus


class SignUpScreen(Screen):
    def __init__(self, screen_manager, app):
        super().__init__(screen_manager, app)

    def enter(self):
        self.showUI()
        self.sign_up()

    def check_transitions(self):
        pass

    def showUI(self):
        print("--- Sign Up (New Customer) --- \n")

    def sign_up(self):
        customer: Customer = Customer()
        first_name = input("Enter First Name\n> ")
        last_name = input("Enter Last Name\n> ")
        add_line1 = input("Enter Address Line 1\n> ")
        add_line2 = input("Enter Address Line 2\n> ")
        city = input("Enter City\n> ")
        state = input("Enter State\n> ")
        try:
            pincode = int(input("Enter Pincode\n> "))
            if pincode < 100000 or pincode > 999999:
                print("Invalid Pincode")
                return
        except:
            print("Invalid Pincode")
            return

        password = input("Enter password (min 8 char and max 20 char)\n> ")
        while len(password) < 8 or len(password) > 20:
            print("Please Enter password in given range\n> ")
            password = input()

        customer.set_first_name(first_name)
        customer.set_last_name(last_name)
        customer.set_password(password)
        customer.set_status(CustomerStatus.open.value)
        customer.set_login_attempts(3)

        addr: Address = Address()
        addr.set_line_1(add_line1)
        addr.set_line_2(add_line2)
        addr.set_city(city)
        addr.set_state(state)
        addr.set_pincode(pincode)

        customer.set_address(addr)

        database.sign_up_customer(customer)

        input("\nPress ENTER to continue...")

        self.screen_manager.change_screen(self.app.main_menu)
