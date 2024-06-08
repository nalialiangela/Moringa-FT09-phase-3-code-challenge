from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))
    article_id = cursor.lastrowid # Use this to fetch the id of the newly created article

    conn.commit()

    # Query the database for inserted records.
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine[0], magazine[1], magazine[2]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author[0], author[1]))

    print("\nArticles:")
    for article in articles:
        print(Article(article[0], article[1], article[2], article[3], article[4]))

    # Display results for user input
    print("\nNewly Created Records:")
    print("Author ID:", author_id)
    print("Magazine ID:", magazine_id)
    print("Article ID:", article_id)

    # Test the relationship methods
    print("\nTesting the Relationship Methods:")

    # Assuming the above created author_id and magazine_id are used
    new_article = Article(id=article_id, title=article_title, content=article_content, author_id=author_id, magazine_id=magazine_id)
    print(new_article)

    retrieved_article = Article.get_article_by_id(new_article.id)
    print(retrieved_article)
    print(retrieved_article.author)
    print(retrieved_article.magazine)

    author = Author.get_author_by_id(author_id)
    print(author.articles())
    print(author.articles())

    magazine = Magazine.get_magazine_by_id(magazine_id)
    print(magazine.articles())
    print(magazine.contributors())

if __name__ == "__main__":
    main()
