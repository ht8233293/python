import sqlite3

def connect_db():
    return sqlite3.connect('football_manager.db')

def create_database():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS coaches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            position TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            coach_id INTEGER,
            FOREIGN KEY (coach_id) REFERENCES coaches (id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS team_players (
            team_id INTEGER,
            player_id INTEGER,
            PRIMARY KEY (team_id, player_id),
            FOREIGN KEY (team_id) REFERENCES teams (id),
            FOREIGN KEY (player_id) REFERENCES players (id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team_id INTEGER,
            away_team_id INTEGER,
            date_time TEXT NOT NULL,
            location TEXT NOT NULL,
            FOREIGN KEY (home_team_id) REFERENCES teams (id),
            FOREIGN KEY (away_team_id) REFERENCES teams (id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER,
            home_score INTEGER,
            away_score INTEGER,
            FOREIGN KEY (match_id) REFERENCES matches (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
create_database()
