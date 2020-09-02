from FSM.States.main_menu_state import MainMenuState
from FSM.States.state import State
import tkinter
from tkinter import *
from tkinter import messagebox


class MainMenuStateGUI(MainMenuState):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.main_frame = None

    def enter(self):
        print("Main Menu State Enter")

        def value(x):
            self.selection = x
            self.check_transitions()

        self.app.tk_master.title("Main Menu")
        master = Frame(self.app.tk_master)
        self.main_frame = master
        master.pack()

        Label(master, text="MAIN MENU").grid(row=0, columnspan=2, sticky='')
        Button(master, text="SIGN UP(NEW)", command=lambda: (value(1))) \
            .grid(row=1, sticky='')
        Button(master, text="SIGN IN(EXISTING)", command=lambda: (value(2))) \
            .grid(row=2, sticky='')
        Button(master, text="ADMIN SIGN IN", command=lambda: (value(3))) \
            .grid(row=3, sticky='')
        Button(master, text="QUIT", command=lambda: (value(0))) \
            .grid(row=4, sticky='')

        self.app.tk_master.mainloop()

    def check_transitions(self):
        if self.selection == 0:
            self.state_machine.change_state(self.app.exit_state)
        elif self.selection == 1:
            self.state_machine.change_state(self.app.sign_up_state)
        elif self.selection == 2:
            self.state_machine.change_state(self.app.sign_in_state)
        elif self.selection == 3:
            # self.state_machine.change_state(self.app.admin_sign_in_state)
            self.display_msg(["Coming Soon"])

    def display_msg(self, msg):
        messagebox.showinfo("info", "\n".join(msg), parent=self.app.tk_master)

    def exit(self):
        print("Main Menu State Exit")
        self.main_frame.destroy()
        self.main_frame = None
