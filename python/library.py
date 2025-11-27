
import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # ---------------- FILE LOAD ----------------
    def load_data(self):
        try:
            with open("books.json", "r") as f:
                books_list = json.load(f)
                for b in books_list:
                    self.books.append(Book(b["title"], b["author"], b["isbn"], b["available"]))
        except:
            self.books = []

        try:
            with open("members.json", "r") as f:
                member_list = json.load(f)
                for m in member_list:
                    mem = Member(m["name"], m["member_id"])
                    mem.borrowed_books = m["borrowed_books"]
                    self.members.append(mem)
        except:
            self.members = []

    # ---------------- FILE SAVE ----------------
    def save_data(self):
        books_list = []
        for b in self.books:
            books_list.append({
                "title": b.title,
                "author": b.author,
                "isbn": b.isbn,
                "available": b.available
            })

        members_list = []
        for m in self.members:
            members_list.append({
                "name": m.name,
                "member_id": m.member_id,
                "borrowed_books": m.borrowed_books
            })

        with open("books.json", "w") as f:
            json.dump(books_list, f, indent=4)

        with open("members.json", "w") as f:
            json.dump(members_list, f, indent=4)

    # ---------------- BASIC OPS ----------------
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    def lend_book(self, member_id, isbn):
        for m in self.members:
            if m.member_id == member_id:
                for b in self.books:
                    if b.isbn == isbn:
                        if m.borrow_book(b):
                            self.save_data()
                            return True
        return False

    def take_return(self, member_id, isbn):
        for m in self.members:
            if m.member_id == member_id:
                for b in self.books:
                    if b.isbn == isbn:
                        if m.return_book(b):
                            self.save_data()
                            return True
        return False

    # ---------------- ANALYTICS ----------------
    def analytics(self):
        borrowed_count = 0
        for b in self.books:
            if not b.available:
                borrowed_count += 1

        return f"Total books currently borrowed: {borrowed_count}"



