from tkinter import *

def showFullname():
    fullname = fname.get() + " " + lname.get()
    fullname_lbl = Label(root, text=fullname, font=("Arial", 16))
    fullname_lbl.place(x=140, y=130)

def new_tab():
    window = Tk()
    window.mainloop()

root = Tk()  # Create the main window
root.geometry("500x500")
fname_lbl = Label(root, text="First Name:", font=("Arial", 16))
fname_lbl.place(x=20, y=20)
fname = Entry(root, font=("Arial", 12, "bold"))
fname.place(x=140, y=24)

lname_lbl = Label(root, text="Last Name:", font=("Arial", 16))
lname_lbl.place(x=20, y=70)
lname = Entry(root, font=("Arial", 12))
lname.place(x=140, y=74)

fullname = Label(root, text="", font=("Arial", 16))
fullname.place(x=140, y=130)
showFullname_btn = Button(root, text="Submit", font=("Arial", 16), command=showFullname)
showFullname_btn.place(x=140, y=180)

root.mainloop()  # Start the main event loop
