# Function to add a book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


# Function to search for a book
def search_book():
    search_id = input("Enter Book ID to search: ")

    file = open("books.txt", "r")
    found = False

    for record in file:
        book_id, title, author, status = record.strip().split(",")

        if book_id == search_id:
            print("\nBook Found!")
            print("Book ID:", book_id)
            print("Title:", title)
            print("Author:", author)
            print("Status:", status)

            found = True
            break

    file.close()

    if not found:
        print("Book not found.")


# Function to issue a book
def issue_book():
    issue_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    records = file.readlines()
    file.close()

    found = False

    for i in range(len(records)):
        book_id, title, author, status = records[i].strip().split(",")

        if book_id == issue_id:
            found = True

            if status == "Available":
                records[i] = book_id + "," + title + "," + author + ",Issued\n"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            break

    if not found:
        print("Book not found.")

    file = open("books.txt", "w")
    file.writelines(records)
    file.close()


# Function to return a book
def return_book():
    return_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    records = file.readlines()
    file.close()

    found = False

    for i in range(len(records)):
        book_id, title, author, status = records[i].strip().split(",")

        if book_id == return_id:
            found = True

            if status == "Issued":
                records[i] = book_id + "," + title + "," + author + ",Available\n"
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            break

    if not found:
        print("Book not found.")

    file = open("books.txt", "w")
    file.writelines(records)
    file.close()


# Function to display available books
def display_available_books():
    file = open("books.txt", "r")

    print("\nAvailable Books:")
    print("----------------")

    for record in file:
        book_id, title, author, status = record.strip().split(",")

        if status == "Available":
            print("Book ID:", book_id)
            print("Title:", title)
            print("Author:", author)
            print()

    file.close()


# Main menu
while True:
    print("\n===== BOOK MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_available_books()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")