from tkinter import *
from tkinter import filedialog, messagebox
import random

# Create the main window
root = Tk()
root.title("برنامه قرعه‌کشی")
root.geometry("400x300")
root.config(bg="#d3cfe5")

# Global variable to store participant names
participants = []


# Function to load participant names from a file
def load_file():
    global participants
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            participants = file.read().splitlines()
        entry_file.delete(0, END)
        entry_file.insert(0, file_path)
        messagebox.showinfo("موفق", "فایل بارگذاری شد!")


# Function to select random winners
def select_winners():
    if not participants:
        messagebox.showerror("خطا", "لطفا یک فایل شرکت‌کنندگان انتخاب کنید.")
        return

    try:
        num_winners = int(entry_winners.get())
    except ValueError:
        messagebox.showerror("خطا", "لطفا تعداد برندگان را به‌درستی وارد کنید.")
        return

    if num_winners > len(participants):
        messagebox.showerror("خطا", "تعداد برندگان بیشتر از تعداد شرکت‌کنندگان است")
        return

    winners = random.sample(participants, num_winners)
    messagebox.showinfo("برندگان", "\n".join(winners))



lbl_file = Label(root, text="فایل شرکت کنندگان را وارد کنید", bg="#d3cfe5")
lbl_file.pack(pady=10)

entry_file = Entry(root, width=30)
entry_file.pack()

btn_load = Button(root, text="انتخاب فایل", command=load_file)
btn_load.pack(pady=5)

lbl_winners = Label(root, text="تعداد برندگان را وارد کنید", bg="#d3cfe5")
lbl_winners.pack(pady=10)

entry_winners = Entry(root)
entry_winners.pack()

btn_select = Button(root, text="انتخاب برندگان", command=select_winners)
btn_select.pack(pady=20)


root.mainloop()
