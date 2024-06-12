# lib/cli.py
from models.model_functions import EditorDB
from helpers import exit_program

def main():

    db = EditorDB()

    while True:
        print("\n1. Add Magazine")
        print("2. Add Author")
        print("3. Add Article")
        print("4. Assign magazine to an author")
        print("5. Assign article to an magazine")
        print("6. List of Magazines")
        print("7. List of Authors")
        print("8. List of Articles")
        print("9. Find Magazine by ID")
        print("10. Find Author by ID")
        print("11. Find Article by ID")
        print("12. Exit")
        choice = input("Enter Choice: ")

        if choice == "1":
            main_title = input("Enter Magazine's Main Title: ")
            genre = input("Enter Magazine's Genre: ")
            db.add_magazine(main_title,genre)

        elif choice == "2":
            name = input("Enter Author's Name: ")
            db.add_author(name)

        elif choice == "3":
            title = input("Enter Article's Title: ")
            category = input("Enter Article category: ")
            db.add_article(title,category)

        elif choice == "4":
            magazines_id = int(input("Enter Magazine's ID: "))
            authors_id = int(input("Enter Author's ID: "))
            db.assign_magazine_to_author(magazines_id,authors_id)
        
        elif choice == "5":
            article_id = int(input("Enter Article's ID: "))
            magazines_id = int(input("Enter Magazine's ID: "))
            db.assign_article_to_magazine(article_id,magazines_id) 

        elif choice == "6":
            magazines = db.list_magazines()
            if magazines:
                print(f"{'Magazine ID':<15}{'Main Title':<20}{'Genre':<15}{'Author ID':<15}{'Author Name':<20}")
                print("-" * 85)
                for magazine in magazines:
                    print(f"{magazine[0]:<15}{magazine[1]:<20}{magazine[2]:<15}{magazine[3] if magazine[3] is not None else 'N/A':<15}{magazine[4] if magazine[4] is not None else 'N/A':<20}")
            else:
                print("No magazines found.") 
        
        elif choice == "7":
            authors = db.list_authors()
            if authors:
                print(f"{'Author ID':<15}{'Author Name':<20}")
                print("-" * 35)
                for author in authors:
                    print(f"{author[0]:<15}{author[1]:<20}")
            else:
                print("No authors found.")
        
        elif choice == "8":
            articles = db.list_articles()
            if articles:
                print(f"{'Article ID':<15}{'Article Title':<20}{'Category':<20}{'Magazine ID':<15}{'Magazine Title':<25}")
                print("-" * 100)
                for article in articles:
                    print(f"{article[0]:<15}{article[1]:<20}{article[2]:<20}{article[3]:<15}{article[4]:<25}")
                else:
                    print("No articles found.")
        
        elif choice == "9":
            magazine_id = int(input("Enter magazine ID to find: "))
            magazine = db.find_magazine_by_id(magazine_id)
            if magazine:
                print(f"{'Magazine ID':<15}{'Title':<25}{'Genre':<20}")
                print("-" * 100)
                print(f"{magazine[0]:<15}{magazine[1]:<25}{magazine[2]:<20}")

        elif choice == "10":
            author_id = int(input("Enter author ID to find: "))
            author = db.find_author_by_id(author_id)
            if author:
                print(f"{'Author ID':<15}{'Name':<25}")
                print("-" * 40)
                print(f"{author[0]:<15}{author[1]:<25}")

        elif choice == "11":
            article_id = int(input("Enter article ID to find: "))
            article = db.find_article_by_id(article_id)
            if article:
                print(f"{'Article ID':<15}{'Title':<20}{'Category':<20}")
                print("-" * 55)
                print(f"{article[0]:<15}{article[1]:<20}{article[2]:<20}")

        elif choice == "12":
            exit_program()
            break

        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
