import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db

def add_team(name, coach_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO teams (name, coach_id) VALUES (?, ?)", (name, coach_id))
    conn.commit()
    conn.close()

def update_team(team_id, name, coach_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE teams SET name = ?, coach_id = ? WHERE id = ?", (name, coach_id, team_id))
    conn.commit()
    conn.close()

def delete_team(team_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM teams WHERE id = ?", (team_id,))
    conn.commit()
    conn.close()

def load_teams(tree):
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM teams")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def team_ui(root):
    team_frame = ttk.LabelFrame(root, text="Add/Update Team")
    team_frame.grid(row=0, column=2, padx=10, pady=10)

    tk.Label(team_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    team_name_entry = tk.Entry(team_frame)
    team_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(team_frame, text="Coach ID:").grid(row=1, column=0, padx=5, pady=5)
    team_coach_entry = tk.Entry(team_frame)
    team_coach_entry.grid(row=1, column=1, padx=5, pady=5)

    def add_team_command():
        name = team_name_entry.get()
        coach_id = team_coach_entry.get()
        if name and coach_id:
            add_team(name, coach_id)
            load_teams(team_tree)
            team_name_entry.delete(0, tk.END)
            team_coach_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Team added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def update_team_command():
        selected_item = team_tree.selection()[0]
        team_id = team_tree.item(selected_item)['values'][0]
        name = team_name_entry.get()
        coach_id = team_coach_entry.get()
        if name and coach_id:
            update_team(team_id, name, coach_id)
            load_teams(team_tree)
            team_name_entry.delete(0, tk.END)
            team_coach_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Team updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def delete_team_command():
        selected_item = team_tree.selection()[0]
        team_id = team_tree.item(selected_item)['values'][0]
        delete_team(team_id)
        load_teams(team_tree)
        messagebox.showinfo("Success", "Team deleted successfully!")

    def select_team(event):
        selected_item = team_tree.selection()[0]
        team_id, name, coach_id = team_tree.item(selected_item)['values']
        team_name_entry.delete(0, tk.END)
        team_name_entry.insert(0, name)
        team_coach_entry.delete(0, tk.END)
        team_coach_entry.insert(0, coach_id)

    add_team_button = tk.Button(team_frame, text="Add Team", command=add_team_command)
    add_team_button.grid(row=2, column=0, padx=5, pady=10)

    update_team_button = tk.Button(team_frame, text="Update Team", command=update_team_command)
    update_team_button.grid(row=2, column=1, padx=5, pady=10)

    delete_team_button = tk.Button(team_frame, text="Delete Team", command=delete_team_command)
    delete_team_button.grid(row=2, column=2, padx=5, pady=10)

    team_list_frame = ttk.LabelFrame(root, text="Team List")
    team_list_frame.grid(row=1, column=2, padx=10, pady=10)

    team_tree = ttk.Treeview(team_list_frame, columns=("ID", "Name", "Coach ID"), show="headings")
    team_tree.heading("ID", text="ID")
    team_tree.heading("Name", text="Name")
    team_tree.heading("Coach ID", text="Coach ID")
    team_tree.pack()
    team_tree.bind('<ButtonRelease-1>', select_team)

    load_teams(team_tree)
