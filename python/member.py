class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.isbn)
            return True
        return False

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            return True
        return False

    def list_books(self):
        return self.borrowed_books
