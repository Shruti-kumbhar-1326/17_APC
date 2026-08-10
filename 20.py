#20.	Create a list of books.Implement:
#•	Add a new book 
#•	Search a book 
#•	Remove a book 
#•	Display all books 
#•	Count total books
books = ["Python", "Java", "C++", "HTML", "SQL"]

# Add a new book
new_book = input("Enter a new book: ")
books.append(new_book)
print("Book added successfully.")

# Search a book
search = input("Enter book name to search: ")

if search in books:
    print("Book is available.")
else:
    print("Book is not available.")

# Remove a book
remove_book = input("Enter book name to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed successfully.")
else:
    print("Book not found.")

# Display all books
print("All books:", books)

# Count total books
print("Total books:", len(books))