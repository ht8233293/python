import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db

def add_coach(name, age):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO coaches (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def update_coach(coach_id, name, age):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE coaches SET name = ?, age = ? WHERE id = ?", (name, age, coach_id))
    conn.commit()
    conn.close()


def delete_coach(coach_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM coaches WHERE id = ?", (coach_id,))
    conn.commit()
    conn.close()


def load_coaches(tree):
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM coaches")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()


def coach_ui(frame):
    coach_frame = ttk.LabelFrame(frame, text="Add/Update Coach")
    coach_frame.grid(row=0, column=0, padx=10, pady=10)

    tk.Label(coach_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    coach_name_entry = tk.Entry(coach_frame)
    coach_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(coach_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
    coach_age_entry = tk.Entry(coach_frame)
    coach_age_entry.grid(row=1, column=1, padx=5, pady=5)

    def add_coach_command():
        name = coach_name_entry.get()
        age = coach_age_entry.get()
        if name and age:
            add_coach(name, age)
            load_coaches(coach_tree)
            coach_name_entry.delete(0, tk.END)
            coach_age_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Coach added successfully!")

        else:
            messagebox.showerror("Error", "All fields are required")

    def update_coach_command():
        selected_item = coach_tree.selection()[0]
        coach_id = coach_tree.item(selected_item)['values'][0]
        name = coach_name_entry.get()
        age = coach_age_entry.get()
        if name and age:
            update_coach(coach_id, name, age)
            load_coaches(coach_tree)
            coach_name_entry.delete(0, tk.END)
            coach_age_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Coach updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def delete_coach_command():
        selected_item = coach_tree.selection()[0]
        coach_id = coach_tree.item(selected_item)['values'][0]
        delete_coach(coach_id)
        load_coaches(coach_tree)
        messagebox.showinfo("Success", "Coach deleted successfully!")

    def select_coach(event):
        selected_item = coach_tree.selection()[0]
        coach_id, name, age = coach_tree.item(selected_item)['values']
        coach_name_entry.delete(0, tk.END)
        coach_name_entry.insert(0, name)
        coach_age_entry.delete(0, tk.END)
        coach_age_entry.insert(0, age)

    add_coach_button = tk.Button(coach_frame, text="Add Coach", command=add_coach_command)
    add_coach_button.grid(row=2, column=0, padx=5, pady=10)

    update_coach_button = tk.Button(coach_frame, text="Update Coach", command=update_coach_command)
    update_coach_button.grid(row=2, column=1, padx=5, pady=10)

    delete_coach_button = tk.Button(coach_frame, text="Delete Coach", command=delete_coach_command)
    delete_coach_button.grid(row=2, column=2, padx=5, pady=10)

    coach_list_frame = ttk.LabelFrame(frame, text="Coach List")
    coach_list_frame.grid(row=1, column=0, padx=10, pady=10)

    coach_tree = ttk.Treeview(coach_list_frame, columns=("ID", "Name", "Age"), show="headings")
    coach_tree.heading("ID", text="ID")
    coach_tree.heading("Name", text="Name")
    coach_tree.heading("Age", text="Age")
    coach_tree.pack()
    coach_tree.bind('<ButtonRelease-1>', select_coach)

    load_coaches(coach_tree)