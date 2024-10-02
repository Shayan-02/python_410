# This program is a 4 basic graphical calculator with buttons

from tkinter import *
# Import everything from the library tkinter
from tkinter import font as tkfont  # Import the font module

expression = ""


# for now the expression is empty but it is a
# Variable
# ........................................
# Function to update expression 
# in the text entry box 
def press(num):
    # point out the global expression variable
    global expression
    # joining of string
    expression = expression + str(num)
    # updating expression by set method
    equation.set(expression)


# Function to evaluate the final expression 
def equalpress():
    # Try and except statement is used for handling some errors like dividing by number which can't be devided by and so on.
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)

        # The initial value of the expression variable
        # with an empty string
        expression = str(total)

    # If you found error, then handle by except.
    except:

        equation.set(" ERROR! ")
        expression = ""

    # Function to clear the tings


# which are in the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


root = Tk()

# Set the background color of the root window.
root.config(bg="black")

# Set the title of the window.
root.title("ANITA CALCULATOR")
# set the size of the root window
root.geometry("1381x1389")

# In here we use StringVar() which is a veriable class which we creat instant of class
equation = StringVar()
button_font = tkfont.Font(size=50)  # Increase the font size as needed
text_font = tkfont.Font(size=55)

# Making an entry box for the expression
expression_field = Entry(root, textvariable=equation, font=text_font)

expression_field.grid(columnspan=50, ipadx=200)
# we place the widgets in positions which we want by grid
# now we start making the buttons and we put the command we have made in the buttons too.

button1 = Button(root, text=" 1 ", fg="white", bg="black",
                 command=lambda: press(1), font=button_font)
button1.grid(row=2, column=0, padx=0, pady=0, sticky='ew')

button2 = Button(root, text=" 2 ", fg="white", bg="black",
                 command=lambda: press(2), font=button_font)
button2.grid(row=2, column=1, padx=0, pady=0, sticky='ew')

button3 = Button(root, text=" 3 ", fg="white", bg="black",
                 command=lambda: press(3), font=button_font)
button3.grid(row=2, column=2, padx=0, pady=0, sticky='ew')

button4 = Button(root, text=" 4 ", fg="white", bg="black",
                 command=lambda: press(4), font=button_font)
button4.grid(row=3, column=0, padx=0, pady=0, sticky='ew')

button5 = Button(root, text=" 5 ", fg="white", bg="black",
                 command=lambda: press(5), font=button_font)
button5.grid(row=3, column=1, padx=0, pady=0, sticky='ew')

button6 = Button(root, text=" 6 ", fg="white", bg="black",
                 command=lambda: press(6), font=button_font)
button6.grid(row=3, column=2, padx=0, pady=0, sticky='ew')

button7 = Button(root, text=" 7 ", fg="white", bg="black",
                 command=lambda: press(7), font=button_font)
button7.grid(row=4, column=0, padx=0, pady=0, sticky='ew')

button8 = Button(root, text=" 8 ", fg="white", bg="black",
                 command=lambda: press(8), font=button_font)
button8.grid(row=4, column=1, padx=0, pady=0, sticky='ew')

button9 = Button(root, text=" 9 ", fg="white", bg="black",
                 command=lambda: press(9), font=button_font)
button9.grid(row=4, column=2, padx=0, pady=0, sticky='ew')

button0 = Button(root, text=" 0 ", fg="white", bg="black",
                 command=lambda: press(0), font=button_font)
button0.grid(row=5, column=0, padx=0, pady=0, sticky='ew')

plus = Button(root, text=" + ", fg="black", bg="yellow",
              command=lambda: press("+"), font=button_font)
plus.grid(row=2, column=3, padx=0, pady=0, sticky='ew')

minus = Button(root, text=" - ", fg="black", bg="yellow",
               command=lambda: press("-"), font=button_font)
minus.grid(row=3, column=3, padx=0, pady=0, sticky='ew')

multiply = Button(root, text=" * ", fg="black", bg="yellow",
                  command=lambda: press("*"), font=button_font)
multiply.grid(row=4, column=3, padx=0, pady=0, sticky='ew')

divide = Button(root, text=" / ", fg="black", bg="yellow",
                command=lambda: press("/"), font=button_font)
divide.grid(row=5, column=3, padx=0, pady=0, sticky='ew')

equal = Button(root, text=" = ", fg="black", bg="yellow", command=equalpress, font=button_font)
equal.grid(row=5, column=2, padx=0, pady=0, sticky='ew')

clear = Button(root, text=" C ", fg="white", bg="black", command=clear, font=button_font)
clear.grid(row=5, column=1, padx=0, pady=0, sticky='ew')

Decimal = Button(root, text=" . ", fg="white", bg="black", command=lambda: press("."), font=button_font)
Decimal.grid(row=6, column=0, padx=0, pady=0, sticky='ew')

root.mainloop()
