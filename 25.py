#25.	Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries
books = {
    "Python": True,
    "Java": True,
    "C++": True
}


def add_book(book_name):
    if book_name not in books:
        books[book_name] = True
        print("Book added successfully.")
    else:
        print("Book already exists.")


def issue_book(book_name):
    if book_name in books:
        if books[book_name]:
            books[book_name] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(book_name):
    if book_name in books:
        if not books[book_name]:
            books[book_name] = True
            print("Book returned successfully.")
        else:
            print("Book was not issued.")
    else:
        print("Book not found.")


def search_book(book_name):
    if book_name in books:
        if books[book_name]:
            print("Book found - Available")
        else:
            print("Book found - Not Available")
    else:
        print("Book not found.")


def display_available_books():
    print("\nAvailable Books:")

    for book, available in books.items():
        if available:
            print(book)


# Main program
add_book("HTML")

issue_book("Python")

search_book("Python")
search_book("Java")

return_book("Python")

display_available_books()