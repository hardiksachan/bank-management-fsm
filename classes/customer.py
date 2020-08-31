import enum


class Customer:
    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_customer_id(self, id):
        self.customer_id = id

    def set_password(self, pwd):
        self.password = pwd

    def set_login_attempts(self, att):
        self.login_attempts = att
        if att == 0:
            self.status = CustomerStatus.locked

    def set_status(self, status):
        self.status = status

    def set_address(self, addr):
        self.addr = addr

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_customer_id(self):
        return self.customer_id

    def get_password(self):
        return self.password

    def get_login_attempts(self):
        return self.login_attempts

    def get_status(self):
        return self.status

    def get_addr_line1(self):
        return self.addr.line1

    def get_addr_line2(self):
        return self.addr.line2

    def get_addr_city(self):
        return self.addr.city

    def get_addr_state(self):
        return self.addr.state

    def get_addr_pincode(self):
        return self.addr.pincode


class CustomerStatus(enum.Enum):
    locked = "locked"
    open = "open"
