# Editor CLI Application
### Date 11/06/2024
### By *Ryan Mwangi*

### Intoduction
This CLI application allows you to manage magazines, authors, and articles in an SQLite database. You can add, list, find, assign, and delete records for magazines, authors, and articles.

### Setup
Create the necessary database and tables by running the following command:
```bash
python lib/models/create_tables.py
```
### Usage
To run the CLI application, execute:
```bash
python lib/cli.py
```
You will be presented with a menu of options:
```markdown
1. Add Magazine
2. Add Author
3. Add Article
4. Assign magazine to an author
5. Assign article to an magazine
6. List of Magazines
7. List of Authors
8. List of Articles
9. Find Magazine by ID
10. Find Author by ID
11. Find Article by ID
12. Magazine's articles
13. Author's magazines
14. Delete Author
15. Delete Magazine
16. Delete Article
17. Exit
Enter Choice: 
```
Then you are required to choose an option which will direct you as per your choice.

#### Technologies Used
- Python
- SQLite

#### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

