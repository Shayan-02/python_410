import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# اتصال به دیتابیس
conn = sqlite3.connect("finance.db")
c = conn.cursor()

# ایجاد جدول در صورت عدم وجود
c.execute(
    """CREATE TABLE IF NOT EXISTS finance
             (id INTEGER PRIMARY KEY, type TEXT, amount INTEGER, description TEXT)"""
)


# تابع افزودن درآمد/مخارج
def add_entry():
    entry_type = type_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if amount:
        c.execute(
            "INSERT INTO finance (type, amount, description) VALUES (?, ?, ?)",
            (entry_type, amount, description),
        )
        conn.commit()
        messagebox.showinfo("موفقیت", "مورد با موفقیت افزوده شد")
    else:
        messagebox.showwarning("خطا", "لطفاً تمام فیلدها را پر کنید")


# تابع رسم نمودار
def plot_chart():
    c.execute("SELECT type, amount FROM finance")
    data = c.fetchall()
    types = [d[0] for d in data]
    amounts = [d[1] for d in data]

    plt.figure(figsize=(6, 4))
    plt.bar(types, amounts, color=["green", "red"])
    plt.xlabel("نوع")
    plt.ylabel("مقدار")
    plt.title("نمودار درآمد و مخارج")
    plt.show()


# رابط کاربری
root = tk.Tk()
root.title("مدیریت مخارج شخصی")

type_var = tk.StringVar(value="درآمد")

tk.Label(root, text="نوع:").grid(row=0, column=0)
tk.Radiobutton(root, text="درآمد", variable=type_var, value="درآمد").grid(
    row=0, column=1
)
tk.Radiobutton(root, text="مخارج", variable=type_var, value="مخارج").grid(
    row=0, column=2
)

tk.Label(root, text="مقدار:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="توضیحات:").grid(row=2, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1)

tk.Button(root, text="افزودن", command=add_entry).grid(row=3, column=0)
tk.Button(root, text="نمایش نمودار", command=plot_chart).grid(row=3, column=1)

root.mainloop()
