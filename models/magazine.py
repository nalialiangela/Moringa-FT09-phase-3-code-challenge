from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._id = id
        self._name = name
        self._category = category
        self._save_to_db()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name
        self._update_db()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category
        self._update_db()

    def _save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    def _update_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE magazines SET name = ?, category = ? WHERE id = ?', (self._name, self._category, self._id))
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
            return Magazine(magazine_data["id"], magazine_data["name"], magazine_data["category"])
        else:
            return None

    def __repr__(self):
        return f'<Magazine {self.name}>'
