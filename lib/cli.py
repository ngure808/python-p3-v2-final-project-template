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
        print("6. Exit")
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
            exit_program()
            break

        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
