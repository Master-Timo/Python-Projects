from tkinter import *
from random import randint

root = Tk()

root.title("Alpha")
root.geometry("1300x650")
root.maxsize(width=1300, height=650)
root.minsize(width=1300, height=650)

a = "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))
root.config(bg=a)


root.mainloop()
