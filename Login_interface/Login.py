from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import datetime
import random
from random import randint

def main():
    root = Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("680x500+450+200")
#        a="#%02x%02x%02x"%(randint(0,255),randint(0,255),randint(0,255))
        self.master.config(bg='#827397')
        self.frame = Frame(self.master, bg='#827397')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle=Label(self.frame, text= 'LOGIN SYSTEM' , font=('algerian',50),bg='#af8baf',fg='#26191b')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

# ================================================ LOG IN FRAME =================================================== #

        self.LoginFrame1=LabelFrame(self.frame , width =680 ,height=500 ,font =('algerian',20),relief='ridge',
                                    bg='#af8baf',fg='#26191b',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=680, height=500, font=('algerian', 20), relief='ridge',
                                      bg='#af8baf',fg='#26191b', bd=10)
        self.LoginFrame2.grid(row=2, column=0)

# ============================================== LABEL AND ENTRY ================================================== #

        self.lblUsername=Label(self.LoginFrame1,text='Username',font=('Times New Roman',20,'bold'))
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('Times New Roman',20,'bold'),textvariable=self.Username )
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text='Password', font=('Times New Roman', 20, 'bold'))
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('Times New Roman', 20, 'bold'), show='*',
                                 textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1)

# ===============================================    BUTTONS    ================================================ #

        self.btnLogin = Button(self.LoginFrame2, text='LOGIN', width=17,relief=RAISED, command=self.Login_System)
        self.btnLogin.grid(row=3, column=0)

        self.btnReset = Button(self.LoginFrame2, text='RESET',relief=RAISED, width=17, command=self.Reset)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(self.LoginFrame2, text='EXIT',relief=RAISED, width=17 , command=self.iExit)
        self.btnExit.grid(row=3, column=2)

# ========================================== Username & PassworD ================================================== #

    def Login_System(self):
        u=(self.Username.get())
        p=(self.Password.get())

# ============================================   Button CODING   =================================================== #

        if u==str('MasterTimo') and p==('abcde'):
            tkinter.messagebox.showinfo('Login Systems',('Welcome !',u))
            self.new_window = Toplevel(self.master)
            self.app = Window2(self.new_window)
        else:
            tkinter.messagebox.askyesno('Login Systems',"Too Bad,invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()


    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()


    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno("Login Systems","Confirm if you want to exit")
        if self.iExit > 0 :
            self.master.destroy()
        else:
            command =self.new_window()
            return

# ===============================================  2ND WINDOW  ==================================================== #

    def new_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Window2(self.new_window)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Management")
        self.master.geometry("680x500+450+200")
        self.master.config(bg='#D8B9C3')
        self.frame = Frame(self.master, bg='#D8B9C3')
        self.frame.pack()


if __name__=='__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()
