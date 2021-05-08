# import required packages
import math
from tkinter import *
import tkinter.font as font

btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666"
}

########################################################################################################################
# ==================================================== Create Class ====================================================
class MyCalculator:
    def __init__(self):
        pass

    def addition(self, x, y):
        sum_of_variables = x + y
        return sum_of_variables

    def subtraction(self, x, y):
        diff_of_variables = x - y
        return diff_of_variables

    def multiplication(self, x, y):
        prod_of_variables = x * y
        return prod_of_variables

    def division(self, x, y):
        div = x / y
        return div

    def modulo_division(self, x, y):
        div = x % y
        return div

    def power_of_num(self, x, y):
        return math.pow(x, y)

    def square_root_of_num(self, x):
        return math.sqrt(x)

    def gcd(self, x, y):
        return math.gcd(x, y)

########################################################################################################################
# ========================================== Trigonometric Functions ===================================================
    def sine(self, k):
        return math.sin(math.radians(k))

    def cosine(self, k):
        return math.cos(math.radians(k))

    def tangent(self, k):
        return math.tan(math.radians(k))
########################################################################################################################
# ============================================ Creating the GUI Interface ==============================================


def center_window(width, height):
    # Gets the requested values of the height and width.
    window_width = width
    window_height = height
    # print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, position_right, position_down))


def scientific():
    global toggle_hide

    new_height = 650
    new_width = 1050
    if toggle_hide:
        center_window(650, 650)
        # root.geometry("{}x{}".format(650, new_height))
        btn_panel.config(text=">>")
        toggle_hide = FALSE
        # hide the scientific panel
        pass
    else:
        center_window(new_width, new_height)
        # root.geometry("{}x{}".format(new_width, new_height))
        btn_panel.config(text="<<")
        toggle_hide = TRUE
        # show the scientific panel
        pass
    #  if raw_width == new_width:
    #      root.geometry("{}x{}".format(new_height, new_height))
    #  else:

#######################################################################################################################


root = Tk()
root.title("All in one Utility Calculator")


width = 650
height = 650
center_window(width, height)
root.resizable(width=False, height=False)

# Utility Variables
toggle_hide = FALSE
count = 0

# Define Fonts
fonts_heading = ""
fonts_body = ""
myFont = font.Font(family='Helvetica', size=20, weight='bold')





#######################################################################################################################
# ================================================= Menu Bar  =========================================================

menuBar = Menu(root)
contents_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Contents", menu=contents_menu)
contents_menu.add_command(label="Calculator")
contents_menu.add_command(label="Convertor")
contents_menu.add_command(label="Currency")
contents_menu.add_separator()
contents_menu.add_command(label="Exit")


# =============================================== Menu Bar Finished ===================================================
#######################################################################################################################
#######################################################################################################################
# =========================================== Control TOGGLE Button ===================================================
buttonFrame = Frame(root)
buttonFrame.pack(side=RIGHT)

btn_panel = Button(buttonFrame, text=">>", pady=height, command=scientific)
btn_panel.config(bg="cyan")
btn_panel.pack(side=RIGHT)

# ========================================= Control TOGGLE Button Finished ============================================
#######################################################################################################################
# ============================================= Calculator Keypad =====================================================

buttonFrame1 = Frame(root)
buttonFrame1.pack(side=BOTTOM)

btn_zero = Button(buttonFrame1, text=str(count))
count += 1
btn_zero.config(**btn_params)
btn_zero.grid(row=4, column=0)


for i in range(3, 0, -1):
    for j in range(0, 3):
        btn = Button(buttonFrame1, text=str(count))
        btn.config(**btn_params)

        btn.grid(row=i, column=j)
        count += 1


btn_dot = Button(buttonFrame1, text='\u2022')
btn_dot.config(**btn_params)
btn_dot.grid(row=4, column=1)

# ========================================= Calculator Keypad Finished =============================================
####################################################################################################################
# ========================================= Calculator Function Keys ===============================================
btn_sign = Button(buttonFrame1, text="\u00B1")
btn_sign.config(**btn_params)
btn_sign.grid(row=4, column=2)

btn_add = Button(buttonFrame1, text="\uFF0B")
btn_add.config(**btn_params)
btn_add.grid(row=2, column=3)

btn_sub = Button(buttonFrame1, text="\uFF0D")
btn_sub.config(**btn_params)
btn_sub.grid(row=1, column=3)

btn_mul = Button(buttonFrame1, text="\u00D7")
btn_mul.config(**btn_params)
btn_mul.grid(row=0, column=3)

btn_div = Button(buttonFrame1, text="\uFF0F")
btn_div.config(**btn_params)
btn_div.grid(row=0, column=2)

# ====================================== Calculator Function Keys Finished ==========================================
#####################################################################################################################
# ============================================== Calculate (=) Key ==================================================

btn_equals = Button(buttonFrame1, text="\uFF1D")
btn_equals.config(**btn_params)
btn_equals.grid(row=4, column=3)

# ========================================== Calculate (=) Key Finished ==============================================
######################################################################################################################
# =========================================== Calculator Clear Keys ==================================================

btn_clear = Button(buttonFrame1, text=chr(67))
btn_clear.config(**btn_params)
btn_clear.grid(row=0, column=1)

btn_clear_all = Button(buttonFrame1, text=chr(67)+chr(69))
btn_clear_all.config(**btn_params)
btn_clear_all.grid(row=0, column=0)

# ======================================== Calculator Clear Keys Finished ============================================
######################################################################################################################

root.mainloop()
