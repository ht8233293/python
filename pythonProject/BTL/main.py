import tkinter as tk
from player_manager import player_ui
from coach_manager import coach_ui
from team_manager import team_ui
from schedule_manager import schedule_ui
from result_manager import result_ui

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_player_ui(root, frame):
    clear_frame(frame)
    player_ui(frame)

def show_coach_ui(root, frame):
    clear_frame(frame)
    coach_ui(frame)

def show_team_ui(root, frame):
    clear_frame(frame)
    team_ui(frame)

def show_schedule_ui(root, frame):
    clear_frame(frame)
    schedule_ui(frame)

def show_result_ui(root, frame):
    clear_frame(frame)
    result_ui(frame)

def main():
    root = tk.Tk()
    root.title("Football Tournament Manager")

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    content_frame = tk.Frame(root)
    content_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    player_button = tk.Button(button_frame, text="Manage Players", command=lambda: show_player_ui(root, content_frame))
    player_button.pack(side=tk.LEFT)

    coach_button = tk.Button(button_frame, text="Manage Coaches", command=lambda: show_coach_ui(root, content_frame))
    coach_button.pack(side=tk.LEFT)

    team_button = tk.Button(button_frame, text="Manage Teams", command=lambda: show_team_ui(root, content_frame))
    team_button.pack(side=tk.LEFT)

    schedule_button = tk.Button(button_frame, text="Schedule Matches", command=lambda: show_schedule_ui(root, content_frame))
    schedule_button.pack(side=tk.LEFT)

    result_button = tk.Button(button_frame, text="Manage Results", command=lambda: show_result_ui(root, content_frame))
    result_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
