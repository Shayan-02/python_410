import random
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import random

def select_file():
    global participants
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            participants = file.read().splitlines()
            file_entry.delete(0, END)
            file_entry.insert(0, file_path)
            messagebox.showinfo("موفق", "!فایل بارگذاری شد")

def select_winner():
    try:
        num = int(winner_entry.get())
        if num<=0:
            messagebox.showwarning("عدد اشتباه", "یک عدد صحیح وارد کنید")
    except ValueError:
        messagebox.showwarning("عدد اشتباه", "یک عدد صحیح وارد کنید")
    file = file_entry.get()
    try:
        with open(file, 'r', encoding="utf-8") as f:
            name_list = f.read().splitlines()
            if len(name_list) < num:
                messagebox.showwarning("عدد اشتباه", "بیشتر از تعداد شرکت کنندگان وجود دارد")
            else:
                winner_list = random.sample(name_list, num)
                top_window = Tk()
                top_window.title("افراد برنده")
                top_window.geometry("300x400")
                winner_label = ttk.Label(top_window, text=":افراد برنده", font=font)
                winner_label.pack(pady=15)
                winner_list = [f"{i + 1} : {j}" for i, j in enumerate(winner_list)]
                winners = "\n".join(winner_list)
                show_winner_text = ttk.Label(top_window, text=winners, font=font)
                show_winner_text.pack()
                exit_button = ttk.Button(top_window, text="بستن", command=top_window.destroy)
                exit_button.pack()
                top_window.mainloop()
    except FileNotFoundError:
        messagebox.showerror("خطا", f"فایل {file} یافت نشد")

root = Tk()
root.title("برنامه قرعه کشی")
root.geometry("400x400")
root.configure(bg="#c1c1e1")

font=("Vazir", 14, "bold")

file_label = ttk.Label(
    root, text="فایل شرکت کنندگان را وارد کنید", 
    font=("Vazir", 14, "bold"), background="#c1c1e1", foreground="black"
).pack(pady=20)

style = ttk.Style()
style.configure("TFrame", font=("Vazir", 14, "bold"), background="#1e90ff", foreground="white")
file_frame = ttk.Frame(root, style="TFrame")
file_frame.pack(pady=5)

file_entry = ttk.Entry(file_frame, font=("Arial", 12, "bold"))
file_entry.grid(padx=5, pady=5, row=0, column=0)

file_button = ttk.Button(file_frame, text="انتخاب فایل", command= select_file)
file_button.grid(padx=5, pady=5, row=0, column=1)

winner_label = ttk.Label(root, text="تعداد برندگان را وارد کنید", background="#c1c1e1", font=font).pack(pady=20)

winner_entry = ttk.Entry(root, font=font, width=5)
winner_entry.pack()

select_button = ttk.Button(root, text="انتخاب برندگان", command=select_winner)
select_button.pack(pady=5)

root.mainloop()
