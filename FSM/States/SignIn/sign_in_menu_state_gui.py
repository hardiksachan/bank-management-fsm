from FSM.States.SignIn.sign_in_menu_state import SignInState
from tkinter import *
from tkinter import messagebox


class SignInStateGUI(SignInState):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 7
        self.main_frame = None

    def enter(self):
        super().enter()
        print("Enter Sign In State")

    def showUI(self):
        def value(x):
            self.selection = x
            self.check_transitions()

        self.app.tk_master.title("Main Menu")

        if self.main_frame is not None:
            self.main_frame.destroy()
            self.main_frame = None
        master = Frame(self.app.tk_master)
        self.main_frame = master
        master.pack()

        Label(master, text="MENU", justify='center').grid(row=0, columnspan=2, sticky='')
        Button(master, text="ADDRESS CHANGE", command=lambda: (value(1))) \
            .grid(row=1, sticky='')
        Button(master, text="OPEN NEW ACCOUNT", command=lambda: (value(2))) \
            .grid(row=2, sticky='')
        Button(master, text="MANAGE FUNDS", command=lambda: (value(3))) \
            .grid(row=3, sticky='')
        Button(master, text="PRINT STATEMENT", command=lambda: (value(4))) \
            .grid(row=4, sticky='')
        Button(master, text="ACCOUNT CLOSURE", command=lambda: (value(5))) \
            .grid(row=5, sticky='')
        Button(master, text="PASSWORD CHANGE", command=lambda: (value(6))) \
            .grid(row=6, sticky='')
        Button(master, text="VIEW ALL ACCOUNTS", command=lambda: (value(7))) \
            .grid(row=7, sticky='')
        Button(master, text="QUIT", command=lambda: (value(0))) \
            .grid(row=8, sticky='')
        self.app.tk_master.mainloop()

    def input_sign_in(self):
        if self.main_frame is not None:
            self.main_frame.destroy()
            self.main_frame = None
        master = Frame(self.app.tk_master)
        self.main_frame = master
        master.pack()

        # try:
        tb_c_id = Entry(master)
        tb_c_id.grid(row=0, sticky='')
        tb_pwd = Entry(master,)
        tb_pwd.grid(row=2, sticky='')
        Button(master, text="Sign In", command=lambda: (self.sign_in(int(tb_c_id.get()), tb_pwd.get()))) \
            .grid(row=4, sticky='')
        # except:
        #     self.display_msg(["Enter valid ID"])

    # def input_print_statement(self):
    #     try:
    #         acc_no = int(input("Enter your account No\n"))
    #     except:
    #         self.display_msg(["Invalid Account No"])
    #         return
    #     print("Enter Dates in format (Year-Mon-Day) ")
    #     date_from = input("Date From : ")
    #     date_to = input("Date To : ")
    #     self.print_statement(acc_no, date_from, date_to)

    # Completely override in GUI
    # def close_account(self):
    #     try:
    #         acc_no = int(input("\nEnter Account No to close : "))
    #     except:
    #         self.display_msg(["Invalid Account No"])
    #         return
    #     account = database.get_all_info_account(acc_no, self.id, AccountStatus.close.value)
    #     if account is not None:
    #         balacne = database.close_account_customer(account)
    #         self.display_msg(["Account closed successfully",
    #                           f"Rs {balacne} will be delivered to you shortly!"])
    #     else:
    #         self.display_msg(["\nSorry Account No doesn't match"])
    #
    # # Completely override in GUI
    # def change_password(self):
    #     password = input("Enter New password (min 8 char and max 20 char)\n> ")
    #     while len(password) < 8 or len(password) > 20:
    #         print("Please Enter password in given range\n> ")
    #         password = input()
    #     database.change_password_customer(password, self.id)
    #     self.display_msg(["Password changed successfully!"])

    def display_msg(self, msg):
        messagebox.showinfo("info", "\n".join(msg), parent=self.app.tk_master)

    def exit(self):
        super().exit()
        print("Exit Sign In State")
        self.main_frame.destroy()
        self.main_frame = None
