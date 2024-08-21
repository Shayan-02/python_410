from tkinter import *
from tkinter import filedialog, messagebox


def open_file(self):
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        messagebox.showinfo("File Selected", f"File: {file_path}")

root = Tk()  # Create the main window

messagebox.showinfo("Title", "Info message")
messagebox.showwarning("Title", "Warning message")
messagebox.showerror("Title", "Error message")


file_path = filedialog.askopenfilename(title="Select a file")

canvas = Canvas(root, width=400, height=300)
canvas.create_line(0, 0, 200, 100, fill="blue")
canvas.create_rectangle(50, 25, 150, 75, fill="red")
canvas.pack()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=open_file)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

frame = Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

label = Label(frame, text="Inside Frame")
label.pack()


root.mainloop()  # Start the main event loop
