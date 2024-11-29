import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db

def add_player(name, age, position):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO players (name, age, position) VALUES (?, ?, ?)", (name, age, position))
    conn.commit()
    conn.close()

def update_player(player_id, name, age, position):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE players SET name = ?, age = ?, position = ? WHERE id = ?", (name, age, position, player_id))
    conn.commit()
    conn.close()

def delete_player(player_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM players WHERE id = ?", (player_id,))
    conn.commit()
    conn.close()

def load_players(tree):
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def player_ui(root):
    player_frame = ttk.LabelFrame(root, text="Add/Update Player")
    player_frame.grid(row=0, column=0, padx=10, pady=10)

    tk.Label(player_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    player_name_entry = tk.Entry(player_frame)
    player_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(player_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
    player_age_entry = tk.Entry(player_frame)
    player_age_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(player_frame, text="Position:").grid(row=2, column=0, padx=5, pady=5)
    player_position_entry = tk.Entry(player_frame)
    player_position_entry.grid(row=2, column=1, padx=5, pady=5)

    def add_player_command():
        name = player_name_entry.get()
        age = player_age_entry.get()
        position = player_position_entry.get()
        if name and age and position:
            add_player(name, age, position)
            load_players(player_tree)
            player_name_entry.delete(0, tk.END)
            player_age_entry.delete(0, tk.END)
            player_position_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Player added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def update_player_command():
        selected_item = player_tree.selection()[0]
        player_id = player_tree.item(selected_item)['values'][0]
        name = player_name_entry.get()
        age = player_age_entry.get()
        position = player_position_entry.get()
        if name and age and position:
            update_player(player_id, name, age, position)
            load_players(player_tree)
            player_name_entry.delete(0, tk.END)
            player_age_entry.delete(0, tk.END)
            player_position_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Player updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def delete_player_command():
        selected_item = player_tree.selection()[0]
        player_id = player_tree.item(selected_item)['values'][0]
        delete_player(player_id)
        load_players(player_tree)
        messagebox.showinfo("Success", "Player deleted successfully!")

    def select_player(event):
        selected_item = player_tree.selection()[0]
        player_id, name, age, position = player_tree.item(selected_item)['values']
        player_name_entry.delete(0, tk.END)
        player_name_entry.insert(0, name)
        player_age_entry.delete(0, tk.END)
        player_age_entry.insert(0, age)
        player_position_entry.delete(0, tk.END)
        player_position_entry.insert(0, position)

    add_player_button = tk.Button(player_frame, text="Add Player", command=add_player_command)
    add_player_button.grid(row=3, column=0, padx=5, pady=10)

    update_player_button = tk.Button(player_frame, text="Update Player", command=update_player_command)
    update_player_button.grid(row=3, column=1, padx=5, pady=10)

    delete_player_button = tk.Button(player_frame, text="Delete Player", command=delete_player_command)
    delete_player_button.grid(row=3, column=2, padx=5, pady=10)

    player_list_frame = ttk.LabelFrame(root, text="Player List")
    player_list_frame.grid(row=1, column=0, padx=10, pady=10)

    player_tree = ttk.Treeview(player_list_frame, columns=("ID", "Name", "Age", "Position"), show="headings")
    player_tree.heading("ID", text="ID")
    player_tree.heading("Name", text="Name")
    player_tree.heading("Age", text="Age")
    player_tree.heading("Position", text="Position")
    player_tree.pack()
    player_tree.bind('<ButtonRelease-1>', select_player)

    load_players(player_tree)
