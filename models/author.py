import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_author_by_id(author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author_data = cursor.fetchone()
        conn.close()
        if author_data:
            return Author(author_data["id"], author_data["name"])
        else:
            return None

