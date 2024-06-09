import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.id, 1)

    def test_author_name_validation(self):
        with self.assertRaises(ValueError):
            Author(2, "")  # Name must be longer than 0 characters

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsInstance(magazine.id, int)

    def test_magazine_name_validation(self):
        with self.assertRaises(ValueError):
            Magazine(2, "T", "Technology")  # Name must be between 2 and 16 characters

        with self.assertRaises(ValueError):
            Magazine(3, "This name is way too long", "Technology")  # Name must be between 2 and 16 characters

    def test_magazine_category_validation(self):
        with self.assertRaises(ValueError):
            Magazine(4, "Tech Weekly", "")  # Category must be longer than 0 characters

    def test_magazine_name_setter(self):
        magazine = Magazine(5, "Tech Weekly", "Technology")
        magazine.name = "New Name"
        self.assertEqual(magazine.name, "New Name")

    def test_magazine_category_setter(self):
        magazine = Magazine(6, "Tech Weekly", "Technology")
        magazine.category = "Science"
        self.assertEqual(magazine.category, "Science")

    def test_magazine_database_interaction(self):
        magazine = Magazine(None, "Tech Today", "Technology")
        self.assertIsNotNone(magazine.id)

        retrieved_magazine = Magazine.get_magazine_by_id(magazine.id)
        self.assertEqual(retrieved_magazine.name, "Tech Today")
        self.assertEqual(retrieved_magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()
