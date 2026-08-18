class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"You borrowed {self.title}")

    def return_book(self):
        self.is_borrowed = False
        print(f"You returned {self.title}")


b1 = Book("Book A", "Author A")
b2 = Book("Book B", "Author B")
b3 = Book("Book C", "Author C")

b1.borrow()
b1.return_book()

b2.borrow()
b3.borrow()