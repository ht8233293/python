import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db

def load_matches(tree):
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT matches.id, t1.name, t2.name, matches.date_time, matches.location
        FROM matches
        JOIN teams t1 ON matches.home_team_id = t1.id
        JOIN teams t2 ON matches.away_team_id = t2.id
    """)
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def save_result(match_id, home_score, away_score):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO results (match_id, home_score, away_score) VALUES (?, ?, ?)", (match_id, home_score, away_score))
    conn.commit()
    conn.close()

def result_ui(root):
    result_frame = ttk.LabelFrame(root, text="Enter Result")
    result_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    tk.Label(result_frame, text="Home Score:").grid(row=0, column=0, padx=5, pady=5)
    home_score_entry = tk.Entry(result_frame)
    home_score_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(result_frame, text="Away Score:").grid(row=1, column=0, padx=5, pady=5)
    away_score_entry = tk.Entry(result_frame)
    away_score_entry.grid(row=1, column=1, padx=5, pady=5)

    def save_result_command():
        selected_item = match_tree.selection()[0]
        match_id = match_tree.item(selected_item)['values'][0]
        home_score = home_score_entry.get()
        away_score = away_score_entry.get()
        if home_score and away_score:
            save_result(match_id, home_score, away_score)
            home_score_entry.delete(0, tk.END)
            away_score_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Result saved successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    save_result_button = tk.Button(result_frame, text="Save Result", command=save_result_command)
    save_result_button.grid(row=2, column=0, columnspan=2, pady=10)

    match_list_frame = ttk.LabelFrame(root, text="Match List")
    match_list_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    match_tree = ttk.Treeview(match_list_frame, columns=("ID", "Home Team", "Away Team", "Date", "Location"), show="headings")
    match_tree.heading("ID", text="ID")
    match_tree.heading("Home Team", text="Home Team")
    match_tree.heading("Away Team", text="Away Team")
    match_tree.heading("Date", text="Date")
    match_tree.heading("Location", text="Location")
    match_tree.pack()

    load_matches(match_tree)
