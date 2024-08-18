from tkinter import *

root = Tk()

root.title("first app")
root.geometry("500x500")
root.resizable(0, False)

root.config(bg="gray")
# lb1 = Label(root, text="hello", fg="black", bg= "gray", font=("arial", 75)).pack()
lb2 = Label(root, text="hello", fg="black", bg= "gray", font=("arial", 75)).place(x=50, y=30)
lb3 = Label(root, text="hello", fg="black", bg= "gray", font=("arial", 75)).pack()


root.mainloop()