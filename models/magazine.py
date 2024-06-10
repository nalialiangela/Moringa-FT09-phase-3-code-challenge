import sqlite3
from .article import Article

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @staticmethod
    def get_magazine_by_id(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        magazine_data = cursor.fetchone()
        conn.close()
        if magazine_data:
            return Magazine(magazine_data["id"], magazine_data["name"], magazine_data["category"])
        else:
            return None

    
