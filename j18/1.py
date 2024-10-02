import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)"""
)

# GUI Application
root = tk.Tk()
root.title("To-Do List")


def add_task():
    task = task_entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        task_entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")


def load_tasks():
    task_list.delete(0, tk.END)
    for row in cursor.execute("SELECT * FROM tasks"):
        task_list.insert(tk.END, row[1])


def delete_task():
    """Delete selected task from the list"""
    try:
        # Get selected task from the listbox
        selected_task = task_list.get(task_list.curselection())
        # Delete the task from the database
        cursor.execute("DELETE FROM tasks WHERE task = ?", (selected_task,))
        conn.commit()
        # Reload the tasks from the database
        load_tasks()
    except:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "Please select a task to delete")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(root, height=10, width=50)
task_list.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

load_tasks()
root.mainloop()

conn.close()
