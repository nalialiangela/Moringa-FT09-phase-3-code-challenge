
from models.author import Author
from models.article import Article
from models.magazine import Magazine

def include_new_author():
    name = input("Enter author's name: ")
    try:
        author = Author(None, name)
        print(f"Author '{author.name}' included with ID {author.id}.")
    except ValueError as e:
        print(e)

def include_new_magazine():
    name = input("Enter magazine's name: ")
    category = input("Enter magazine's category: ")
    try:
        magazine = Magazine(None, name, category)
        print(f"Magazine '{magazine.name}' included with ID {magazine.id}.")
    except ValueError as e:
        print(e)

def include_new_article():
    title = input("Enter article's title: ")
    content = input("Enter article's content: ")
    author_id = int(input("Enter author's ID: "))
    magazine_id = int(input("Enter magazine's ID: "))
    try:
        article = Article(None, title, content, author_id, magazine_id)
        print(f"Article '{article.title}' included with ID {article.id}.")
    except ValueError as e:
        print(e)

def search_author_articles():
    author_id = int(input("Enter author ID: "))
    author = Author.get_author_by_id(author_id)
    if author:
        articles = Article.get_articles_by_author_id(author_id)
        if articles:
            print(f"Articles for author '{author.name}':")
            for article in articles:
                print(f" - {article.title}")
        else:
            print(f"No articles found for author '{author.name}'.")
    else:
        print(f"No author found with ID {author_id}.")

def search_magazine_articles():
    magazine_id = int(input("Enter magazine ID: "))
    magazine = Magazine.get_magazine_by_id(magazine_id)
    if magazine:
        articles = Article.get_articles_by_magazine_id(magazine_id)
        if articles:
            print(f"Articles for magazine '{magazine.name}':")
            for article in articles:
                print(f" - {article.title}")
        else:
            print(f"No articles found for magazine '{magazine.name}'.")
    else:
        print(f"No magazine found with ID {magazine_id}.")

def search_magazine_contributors():
    magazine_id = int(input("Enter magazine ID: "))
    magazine = Magazine.get_magazine_by_id(magazine_id)
    if magazine:
        authors = Article.get_contributors_by_magazine_id(magazine_id)
        if authors:
            print(f"Contributors for magazine '{magazine.name}':")
            for author in authors:
                print(f" - {author.name}")
        else:
            print(f"No contributors found for magazine '{magazine.name}'.")
    else:
        print(f"No magazine found with ID {magazine_id}.")

def main():
    while True:
        print("Menu:")
        print("1. Add new Author")
        print("2. Add new Magazine")
        print("3. Add new Article")
        print("4. Search Author's Articles")
        print("5. Search Magazine's Articles")
        print("6. Search Magazine's Contributors")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            include_new_author()
        elif choice == 2:
            include_new_magazine()
        elif choice == 3:
            include_new_article()
        elif choice == 4:
            search_author_articles()
        elif choice == 5:
            search_magazine_articles()
        elif choice == 6:
            search_magazine_contributors()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
