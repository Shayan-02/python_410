import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, category TEXT, amount REAL)"""
)


def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if category and amount:
        try:
            amount = float(amount)
            cursor.execute(
                "INSERT INTO expenses (category, amount) VALUES (?, ?)",
                (category, amount),
            )
            conn.commit()
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            load_expenses()
        except ValueError:
            messagebox.showwarning("Warning", "Amount must be a number")
    else:
        messagebox.showwarning("Warning", "Please fill all fields")


def load_expenses():
    expense_list.delete(0, tk.END)
    total = 0
    for row in cursor.execute("SELECT * FROM expenses"):
        expense_list.insert(tk.END, f"{row[1]} | ${row[2]:.2f}")
        total += row[2]
    total_label.config(text=f"Total: ${total:.2f}")


def delete_expense():
    try:
        selected_expense = expense_list.get(expense_list.curselection())
        category = selected_expense.split("|")[0].strip()
        cursor.execute("DELETE FROM expenses WHERE category = ?", (category,))
        conn.commit()
        load_expenses()
    except:
        messagebox.showwarning("Warning", "Please select an expense to delete")


# GUI Setup
root = tk.Tk()
root.title("Expense Tracker")

category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)
category_entry.insert(0, "Category")

amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)
amount_entry.insert(0, "Amount")

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack(pady=5)

expense_list = tk.Listbox(root, height=10, width=50)
expense_list.pack(pady=10)

delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.pack(pady=5)

total_label = tk.Label(root, text="Total: $0.00")
total_label.pack(pady=5)

load_expenses()
root.mainloop()

conn.close()
