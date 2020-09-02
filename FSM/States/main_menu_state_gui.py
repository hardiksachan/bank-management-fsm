from FSM.States.state import State
import tkinter
from tkinter import *
from tkinter import messagebox


class MainMenuStateGUI(MainMenuState):

    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.lower_bound = 0
        self.upper_bound = 3
    t=tkinter.Tk()
    t.title("WELCOME TO BANK")
    t.geometry("500x500")
    def enter(self):
        def value(x):
            return self.selection=x
        l=Label(t, text="MAIN MENU").grid(row=0,columnspan=2,sticky='')
        b=Button(t, text="SIGN UP(NEW)",command=value(1)).grid(row=1,sticky='')
        b=Button(t, text="SIGN IN(EXISTING)",command=value(2)).grid(row=2,sticky='')
        b=Button(t, text="ADMIN SIGN IN",command=value(3)).grid(row=3,sticky='')
        b=Button(t, text="QUIT",command=value(0)).grid(row=4,sticky='')

    def check_transitions(self):
        if self.selection == 0:
            self.state_machine.change_state(self.app.exit_state)
        elif self.selection == 1:
            self.state_machine.change_state(self.app.sign_up_state)
        elif self.selection == 2:
            self.state_machine.change_state(self.app.sign_in_state)
        elif self.selection == 3:
            # self.state_machine.change_state(self.app.admin_sign_in_state)
            messagebox.showinfo(" "," coming soon!!!")
            self.showUI()
            self.update_selection()
