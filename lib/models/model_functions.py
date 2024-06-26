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
        print("Magazine successfully added")

    def add_author(self, name):
        self.CURSOR.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        self.CONN.commit()
        print("Author successfully added")
    
    def add_article(self, title, category):
        self.CURSOR.execute('INSERT INTO articles (title, category) VALUES (?, ?)', (title, category))
        self.CONN.commit()
        print("Article successfully added")
    
    def author_exists(self,author_id):
        self.CURSOR.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        return self.CURSOR.fetchone() is not None

    def magazine_exists(self,magazine_id):
        self.CURSOR.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        return self.CURSOR.fetchone() is not None

    def article_exists(self,article_id):
        self.CURSOR.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        return self.CURSOR.fetchone() is not None
    
    def update_magazine_main_title(self,old_main_title,new_main_title):
        self.CURSOR.execute("UPDATE magazines SET main_title=? WHERE main_title=?",
                            (new_main_title,old_main_title))
        self.CONN.commit()
        if self.CURSOR.rowcount == 0:
          print("Update failed: No magazine found with the provided main_title.")
        else:
         print(f"{old_main_title}'s name has been updated to {new_main_title}.")
    
    def assign_magazine_to_author(self, magazines_id, authors_id):
        if self.author_exists(authors_id):
           self.CURSOR.execute('UPDATE magazines SET authors_id = ? WHERE id = ?', (authors_id, magazines_id))
           self.CONN.commit()
           print(f'The Author of Magazine id: {magazines_id} has id: {authors_id}')
        else:
           print(f'Author of id: {authors_id} does not exist')

    def assign_article_to_magazine(self, magazines_id, article_id):
        if self.magazine_exists(magazines_id):
            self.CURSOR.execute('UPDATE articles SET magazines_id = ? WHERE id = ?', (magazines_id, article_id))
            self.CONN.commit()
            print(f'Article of id: {article_id} has been added to Magazine of id: {magazines_id}')
        else:
            print(f'Magazine of id: {magazines_id} does not exist')

    def list_magazines(self):
        sql = '''
            SELECT magazines.id, magazines.main_title, magazines.genre, authors.id, authors.name
            FROM magazines
            LEFT JOIN authors
            ON magazines.authors_id = authors.id
        '''
        self.CURSOR.execute(sql)
        return self.CURSOR.fetchall()
    
    def list_authors(self):
        self.CURSOR.execute('SELECT * FROM authors')
        return self.CURSOR.fetchall()
    
    def list_articles(self):
        sql = '''
            SELECT articles.id, articles.title, articles.category, magazines.id, magazines.main_title
            FROM articles
            LEFT JOIN magazines
            ON articles.magazines_id = magazines.id
        '''
        self.CURSOR.execute(sql)
        return self.CURSOR.fetchall()
    
    def find_magazine_by_id(self, magazines_id):
        if self.magazine_exists(magazines_id):
            self.CURSOR.execute('SELECT * FROM magazines WHERE id = ?', (magazines_id,))
            row = self.CURSOR.fetchone()
            if row:
               return row
        else:
            print("Magazine not found")
    def find_author_by_id(self, authors_id):
        if self.author_exists(authors_id):
            self.CURSOR.execute('SELECT * FROM authors WHERE id = ?', (authors_id,))
            row = self.CURSOR.fetchone()
            if row:
                return row
        else:
            print("Author not found")

    def find_article_by_id(self, article_id):
        if self.article_exists(article_id):
            self.CURSOR.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
            row = self.CURSOR.fetchone()
            if row:
                return row
        else:
            print("Article not found")
    
    def list_of_magazine_articles(self, magazines_id):
        if self.magazine_exists(magazines_id):
            sql = '''
                SELECT articles.id, articles.title, articles.category, magazines.id, magazines.main_title
                FROM articles
                INNER JOIN magazines
                ON articles.magazines_id = magazines.id
                WHERE magazines.id = ?
            '''
            self.CURSOR.execute(sql, (magazines_id,))
            return self.CURSOR.fetchall()
        else:
            print("Magazine not found")

    def list_of_author_magazines(self, authors_id):
        if self.author_exists(authors_id):
            sql = '''
                SELECT magazines.main_title, magazines.genre, authors.id, authors.name
                FROM magazines
                INNER JOIN authors
                ON magazines.authors_id = authors.id
                WHERE authors.id = ?
            '''
            self.CURSOR.execute(sql, (authors_id,))
            return self.CURSOR.fetchall()
        else:
            print("Author not found")
    
    def delete_magazine_by_id(self, magazines_id):
        if self.magazine_exists(magazines_id):
            self.CURSOR.execute('DELETE FROM magazines WHERE id = ?', (magazines_id,))
            self.CONN.commit()
            print(f"Magazine with ID {magazines_id} has been deleted.")
        else:
            print("Magazine not found.")

    def delete_article_by_id(self, article_id):
        if self.article_exists(article_id):
            self.CURSOR.execute('DELETE FROM articles WHERE id = ?', (article_id,))
            self.CONN.commit()
            print(f"Article with ID {article_id} has been deleted.")
        else:
            print("Article not found.")

    def delete_author_by_id(self, authors_id):
        if self.author_exists(authors_id):
            self.CURSOR.execute('DELETE FROM authors WHERE id = ?', (authors_id,))
            self.CONN.commit()
            print(f"Author with ID {authors_id} has been deleted.")
        else:
            print("Author not found.")
