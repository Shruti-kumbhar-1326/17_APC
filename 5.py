class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID =", self.book_id)
        print("Title =", self.title)
        print("Author =", self.author)
        print("Price =", self.price)


b = Book(101, "Python", "John", 500)

b.display()