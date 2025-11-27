class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True
