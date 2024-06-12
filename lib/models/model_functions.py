import os
import sqlite3
from . import CONN, CURSOR, get_db_connection

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the database file located in the 'database' folder
DATABASE_PATH = os.path.join(BASE_DIR, '..', '..', 'database', 'editor.db')

class EditorDB:

    def __init__(self):
        self.CONN = sqlite3.connect(DATABASE_PATH)
        self.CURSOR = self.CONN.cursor()

    def add_magazine(self, main_title, genre):
        self.CURSOR.execute('INSERT INTO magazines (main_title, genre) VALUES (?, ?)', (main_title, genre))
        self.CONN.commit()

    def add_author(self, name):
        self.CURSOR.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        self.CONN.commit()
    
    def add_article(self, title, category):
        self.CURSOR.execute('INSERT INTO articles (title, category) VALUES (?, ?)', (title, category))
        self.CONN.commit()
    
    def author_exists(self,author_id):
        self.CURSOR.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        return self.CURSOR.fetchone() is not None

    def magazine_exists(self,magazine_id):
        self.CURSOR.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        return self.CURSOR.fetchone() is not None

    def article_exists(self,article_id):
        self.CURSOR.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        return self.CURSOR.fetchone() is not None