from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self.name = name 
        self.category = category 
        self._save_to_db()  

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_magazine_by_id(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        magazine_data = cursor.fetchone()
        conn.close()
        if magazine_data:
            return Magazine(magazine_data['id'], magazine_data['name'], magazine_data['category'])
        else:
            return None

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self._id,))
        articles_data = cursor.fetchall()
        conn.close()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles_data]

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self._id,))
        contributors_data = cursor.fetchall()
        conn.close()
        return [Author(author['id'], author['name']) for author in contributors_data]


    def __repr__(self):
        return f'<Magazine {self.name}>'


if __name__ == "__main__":
    new_magazine = Magazine(id=None, name="Tech Today", category="Technology")
    print(new_magazine)

    
    retrieved_magazine = Magazine.get_magazine_by_id(new_magazine.id)
    print(retrieved_magazine)
