import tkinter as tk
from tkinter import messagebox
import sqlite3

# SQLite connection
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)"""
)


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email),
        )
        conn.commit()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        load_contacts()
    else:
        messagebox.showwarning("Warning", "Please fill all fields")


def load_contacts():
    contact_list.delete(0, tk.END)
    for row in cursor.execute("SELECT * FROM contacts"):
        contact_list.insert(tk.END, f"{row[1]} | {row[2]} | {row[3]}")


def delete_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        name = selected_contact.split("|")[0].strip()
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        conn.commit()
        load_contacts()
    except:
        messagebox.showwarning("Warning", "Please select a contact to delete")


# GUI Setup
root = tk.Tk()
root.title("Address Book")

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)
name_entry.insert(0, "Name")

phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)
phone_entry.insert(0, "Phone")

email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)
email_entry.insert(0, "Email")

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

contact_list = tk.Listbox(root, height=10, width=50)
contact_list.pack(pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

load_contacts()
root.mainloop()

conn.close()
