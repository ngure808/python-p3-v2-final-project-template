import sqlite3

DATABASE_NAME = 'editor.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

CONN = sqlite3.connect(DATABASE_NAME)
CURSOR = CONN.cursor()
