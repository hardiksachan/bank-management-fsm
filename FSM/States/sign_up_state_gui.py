from FSM.States.sign_up_state import SignUpState
import tkinter
from tkinter import *
from tkinter import messagebox

class SignUpStateGUI(SignUpState):


    def input_sign_up(self):
        def add():
                return messagebox.showinfo("SUCCESS","YOUR ACCOUNT WAS CREATED SUCCESSFULLY" )
                return {
                     "first-name": e1.get(),
                     "last-name": e2.get,
                     "add-line1": e3.get(),
                     "add-line2": e4.get(),
                     "city": e5.get(),
                     "state": e6.get(),
                     "pincode": e7.get(),
                     "password": e8.get()
                        } 
                
        master=tkinter.Tk()
        master.geometry("300x300")
        v=StringVar
        master.title("entry")
        Label(master,text="first-name").grid(row=0)
        Label(master,text="last-name").grid(row=1)
        Label(master,text="add-line1").grid(row=2)
        Label(master,text="add-ine2").grid(row=3)
        Label(master,text="city").grid(row=4)
        Label(master,text="state").grid(row=5)
        Label(master,text="pincode",).grid(row=6)
        Label(master,text="password",).grid(row=7)
        e1=Entry(master,textvariable=v)
        e1.grid(row=0,column=1)
        e2=Entry(master,textvariable=v)
        e2.grid(row=1,column=1)
        e3=Entry(master,textvariable=v)
        e3.grid(row=2,column=1)
        e4=Entry(master,textvariable=v)
        e4.grid(row=3,column=1)
        e5=Entry(master,textvariable=v)
        e5.grid(row=4,column=1)
        e6=Entry(master,textvariable=v)
        e6.grid(row=5,column=1)
        e7=Entry(master,textvariable=v)
        e7.grid(row=6,column=1)
        e8=Entry(master,textvariable=v)
        e8.grid(row=7,column=1)
        b=Button(master,text="save",command=add)
        b.grid()
        master.mainloop()
        pass

    def display_msg(self, msg):
        messagebox.showinfo("info",msg)# TODO: display msg array in msg box
        pass
