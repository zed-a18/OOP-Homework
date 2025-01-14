# Build simple library system


class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} is currently {self.availability_status}"


class Member:
    def __init__(self, name, member_id, borrowed_book):
        self.name = name
        self.member_id = member_id
        self.borrowed_book = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}, has borrowed: {self.borrowed_books}"


class Library:
    def __init__(self, book, member):
        self.book = []
        self.member = []

    def add_book(self, book):
        self.book.append(book)

    def register_member(self, member):
        self.member.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_book.append(book)
            print(f"{book.title} has been lent to {member.name}")
        else:
            print(f"Sorry, {book.title} is not available for lending")

    def return_book(self, book, member):
        if book in member.borrowed_book:
            book.available = True
            member.borrowed_book.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book.title}")

    def __str__(self):
        return f"Book: {self.book} is being borrowed by Member: {self.member}"


book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1)

member1 = Member("John", 101, 0)
member2 = Member("Alice", 102, 0)

library = Library(Book, Member)

library.add_book(book1)
library.add_book(book2)

library.register_member(member1)
library.register_member(member2)

library.lend_book(book1, member1)
library.lend_book(book2, member2)
library.return_book(book1, member1)
library.return_book(book2, member1)
