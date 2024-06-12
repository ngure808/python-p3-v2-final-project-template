import sqlite3
from __init__ import CONN, CURSOR

def create_tables():
    CONN = sqlite3.connect('editor.db')
    CURSOR = CONN.cursor()

    CURSOR.execute('''CREATE TABLE IF NOT EXISTS magazines (
                   id INTEGER PRIMARY KEY,
                   main_title TEXT,
                   genre TEXT,
                   authors_id INTEGER,
                   FOREIGN KEY (authors_id) REFERENCES authors(id)
    )''')
    
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS authors (
                   id INTEGER PRIMARY KEY,
                   name TEXT
    )''')
    
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS articles (
                   id INTEGER PRIMARY KEY,
                   title TEXT,
                   category TEXT,
                   magazines_id INTEGER,
                   FOREIGN KEY (magazines_id) REFERENCES magazines(id)
    )''')

    CONN.commit()
    CONN.close()

create_tables()