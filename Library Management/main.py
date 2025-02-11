from book import Book
from user import User
from library import Library

library = Library()

book1 = Book("To kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The great Gatsby", "F. Scott Fitzgerald")
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

user1 = User("Alice")

library.list_books()

user1.borrow_book(book1)

library.list_books()

user1.return_book(book1)

library.list_books()