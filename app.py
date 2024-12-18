def main():
    create_tables()

    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO authors (name) VALUES (?)', ("IRINE KIMETO",))
    author_id = cursor.lastrowid

    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', ("ARUASA", "Food and Nutrition"))
    magazine_id = cursor.lastrowid

    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                   ("Different Types of Beverages in Kenya", 
                    "The different types of beverages in Kenya; both alcoholic and non-alcoholic beverages.", 
                    author_id, 
                    magazine_id))

    conn.commit()
    conn.close()

   
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
    author_data = cursor.fetchone()
    author = Author(author_data["id"], author_data["name"])

    cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
    magazine_data = cursor.fetchone()
    magazine = Magazine(magazine_data["id"], magazine_data["name"], magazine_data["category"])

    print("\nAuthor's Articles:")
    for article in author.articles():
        print(article)

    print("\nAuthor's Magazines:")
    for mag in author.magazines():
        print(mag)

    print("\nMagazine's Articles:")
    for article in magazine.articles():
        print(article)

    print("\nMagazine's Contributors:")
    for contributor in magazine.contributors():
        print(contributor)

    conn.close()

if __name__ == "__main__":
    main()
