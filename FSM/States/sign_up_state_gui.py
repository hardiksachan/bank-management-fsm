from FSM.States.sign_up_state import SignUpState
import tkinter
from tkinter import *
from tkinter import messagebox


class SignUpStateGUI(SignUpState):
    def __init__(self, state_machine, app):
        super().__init__(state_machine, app)
        self.main_frame = None

    def enter(self):
        print("Sign Up State Enter")

        def add():
            try:
                pincode = int(tb_pincode.get())
                if pincode < 100000 or pincode > 999999:
                    self.display_msg(["Invalid Pincode"])
                    return
            except:
                self.display_msg(["Invalid Pincode"])
                return
            password = tb_password.get()
            if len(password) < 8 or len(password) > 20:
                self.display_msg(["Please Enter password in given range"])
                return
            self.sign_up({
                "first-name": tb_fname.get(),
                "last-name": tb_lname.get(),
                "add-line1": tb_line1.get(),
                "add-line2": tb_line2.get(),
                "city": tb_city.get(),
                "state": tb_state.get(),
                "pincode": pincode,
                "password": password
            })

        self.app.tk_master.title("Sign Up")
        master = Frame(self.app.tk_master)
        self.main_frame = master
        master.pack()

        v = StringVar
        Label(master, text="first-name").grid(row=0)
        Label(master, text="last-name").grid(row=1)
        Label(master, text="add-line1").grid(row=2)
        Label(master, text="add-ine2").grid(row=3)
        Label(master, text="city").grid(row=4)
        Label(master, text="state").grid(row=5)
        Label(master, text="pincode", ).grid(row=6)
        Label(master, text="password", ).grid(row=7)
        tb_fname = Entry(master, textvariable=v)
        tb_fname.grid(row=0, column=1)
        tb_lname = Entry(master, textvariable=v)
        tb_lname.grid(row=1, column=1)
        tb_line1 = Entry(master, textvariable=v)
        tb_line1.grid(row=2, column=1)
        tb_line2 = Entry(master, textvariable=v)
        tb_line2.grid(row=3, column=1)
        tb_city = Entry(master, textvariable=v)
        tb_city.grid(row=4, column=1)
        tb_state = Entry(master, textvariable=v)
        tb_state.grid(row=5, column=1)
        tb_pincode = Entry(master, textvariable=v)
        tb_pincode.grid(row=6, column=1)
        tb_password = Entry(master, textvariable=v)
        tb_password.grid(row=7, column=1)
        btn_save = Button(master, text="save", command=add)
        btn_save.grid()
        self.app.tk_master.mainloop()

    def display_msg(self, msg):
        messagebox.showinfo("info", "\n".join(msg), parent=self.app.tk_master)

    def exit(self):
        print("Sign Up State Exit")
        self.main_frame.destroy()
        self.main_frame = None
