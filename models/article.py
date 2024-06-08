from database.connection import get_db_connection
from models.magazine import Magazine

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title  
        self._content = content 
        self._author_id = author_id
        self._magazine_id = magazine_id
        if self._id is None:  
            self._save_to_db()

    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self._title, self._content, self._author_id, self._magazine_id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change the title after the article is instantiated.")
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if hasattr(self, '_content'):
            raise AttributeError("Cannot change the content after the article is instantiated.")
        if not isinstance(value, str):
            raise ValueError("Content must be a string.")
        self._content = value

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    @property
    def author(self):
        return Author.get_author_by_id(self._author_id)

    @property
    def magazine(self):
        return Magazine.get_magazine_by_id(self._magazine_id)


    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self._title, self._content, self._author_id, self._magazine_id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_article_by_id(article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        article_data = cursor.fetchone()
        conn.close()
        if article_data:
            return Article(
                article_data['id'], 
                article_data['title'], 
                article_data['content'], 
                article_data['author_id'], 
                article_data['magazine_id'])
        else:
            return None

    def __repr__(self):
        return f'<Article {self.title}>'


if __name__ == "__main__":
    author_id = 1
    magazine_id = 1
    new_article = Article(id=None, title="The Future of Tech", content="Content of the article", author_id=author_id, magazine_id=magazine_id)
    print(new_article)

    retrieved_article = Article.get_article_by_id(new_article.id)
    print(retrieved_article)

    try:
        new_article.title = "New Title"
    except AttributeError as e:
        print(e)

    try:
        new_article.content = "New Content"
    except AttributeError as e:
        print(e)
from models.author import Author