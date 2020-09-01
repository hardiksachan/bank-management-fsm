import database
from FSM.States.state import State
from classes.Address import Address
from classes.customer import Customer, CustomerStatus


class SignUpState(State):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)

    def enter(self):
        self.showUI()
        self.sign_up()

    def check_transitions(self):
        pass

    def showUI(self):
        print("--- Sign Up (New Customer) --- \n")

    def sign_up(self):
        customer: Customer = Customer()

        user_input = self.input_sign_up()

        customer.set_first_name(user_input["first-name"])
        customer.set_last_name(user_input["last-name"])
        customer.set_password(user_input["password"])
        customer.set_status(CustomerStatus.open.value)
        customer.set_login_attempts(3)

        addr: Address = Address()
        addr.set_line_1(user_input["add-line1"])
        addr.set_line_2(user_input["add-line2"])
        addr.set_city(user_input["city"])
        addr.set_state(user_input["state"])
        addr.set_pincode(user_input["pincode"])

        customer.set_address(addr)

        customer_id = database.sign_up_customer(customer)

        self.display_msg([
            "Congratulations ! Your Account was Created Successfully",
            "Your Customer ID : " + customer_id
        ])

        self.state_machine.change_state(self.app.main_menu)

    def input_sign_up(self):
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

        return {
            "first-name": first_name,
            "last-name": last_name,
            "add-line1": add_line1,
            "add-line2": add_line2,
            "city": city,
            "state": state,
            "pincode": pincode,
            "password": password
        }
