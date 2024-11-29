import sqlite3
from database import connect_db
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

def create_round_robin_schedule(teams):
    schedule = []
    n = len(teams)
    if n % 2 == 1:
        teams.append(None)
        n += 1
    mid = n // 2
    for i in range(n - 1):
        round = []
        for j in range(mid):
            t1 = teams[j]
            t2 = teams[n - 1 - j]
            if t1 and t2:
                round.append((t1, t2))
        teams.insert(1, teams.pop())
        schedule.append(round)
    return schedule

def save_schedule(schedule):
    conn = connect_db()
    c = conn.cursor()
    for round in schedule:
        for match in round:
            home_team, away_team = match
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            location = "Stadium"
            c.execute("INSERT INTO matches (home_team_id, away_team_id, date_time, location) VALUES (?, ?, ?, ?)",
                      (home_team[0], away_team[0], date_time, location))
    conn.commit()
    conn.close()

def load_teams():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT id, name FROM teams")
    teams = c.fetchall()
    conn.close()
    return teams

def generate_schedule():
    teams = load_teams()
    if len(teams) < 2:
        messagebox.showerror("Error", "Not enough teams to create a schedule.")
        return
    schedule = create_round_robin_schedule(teams)
    save_schedule(schedule)
    messagebox.showinfo("Success", "Schedule generated successfully!")

def schedule_ui(root):
    schedule_frame = ttk.LabelFrame(root, text="Generate Schedule")
    schedule_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    generate_schedule_button = tk.Button(schedule_frame, text="Generate Schedule", command=generate_schedule)
    generate_schedule_button.pack(pady=10)
