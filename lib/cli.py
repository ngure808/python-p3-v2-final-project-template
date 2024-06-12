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
        print("8. Exit")
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
            exit_program()
            break

        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
