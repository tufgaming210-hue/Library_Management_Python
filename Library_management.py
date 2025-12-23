import json
import os

# storage file
FILE_NAME = "library.json"

# load books from file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# save books to file
def save_books(library):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)

# add a book
def add_book(library, title, author, quantity):
    book_id = len(library) + 1
    library.append({
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })
    save_books(library)
    print(f"Book '{title}' added!")

# remove a book
def remove_book(library, book_id):
    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            save_books(library)
            print(f"Book '{book['title']}' removed!")
            return
    print("Book not found!")

# search for books
def search_book(library, keyword):
    found = [book for book in library if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    if found:
        print("\nFound books:")
        for book in found:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Quantity: {book['quantity']}")
    else:
        print("No books found!")

# show all books
def show_books(library):
    if not library:
        print("No books available!")
    else:
        print("\nAll books in library:")
        for book in library:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Quantity: {book['quantity']}")

# main menu
def main():
    library = load_books()
    while True:
        print("\n--- Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            quantity = int(input("Quantity: "))
            add_book(library, title, author, quantity)
        elif choice == "2":
            book_id = int(input("Book ID to remove: "))
            remove_book(library, book_id)
        elif choice == "3":
            keyword = input("Keyword to search: ")
            search_book(library, keyword)
        elif choice == "4":
            show_books(library)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()