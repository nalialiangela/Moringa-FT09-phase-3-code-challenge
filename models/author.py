from database.connection import get_db_connection


class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name  
        if id is None:  
            self._save_to_db()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the author is instantiated.")
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = value

    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_author_by_id(author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author_data = cursor.fetchone()
        conn.close()
        if author_data:
            return Author(author_data['id'], author_data['name'])
        else:
            return None

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self._id,))
        articles_data = cursor.fetchall()
        conn.close()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles_data]

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self._id,))
        magazines_data = cursor.fetchall()
        conn.close()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines_data]

    def __repr__(self):
        return f'<Author {self.name}>'

if __name__ == "__main__":
    new_author = Author(id=None, name="John Doe")
    print(new_author)
    retrieved_author = Author.get_author_by_id(new_author.id)
    print(retrieved_author)

    try:
        new_author.name = "Jane Doe"
    except AttributeError as e:
        print(e)
from models.article import Article