import sqlite3
from .author import Author

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @staticmethod
    def get_articles_by_magazine_id(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (magazine_id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]

    @staticmethod
    def get_contributors_by_magazine_id(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT author_id FROM articles WHERE magazine_id = ?', (magazine_id,))
        author_ids = cursor.fetchall()
        conn.close()
        return [Author.get_author_by_id(author_id['author_id']) for author_id in author_ids]

