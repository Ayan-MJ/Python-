class User:
    def __init__(self, name):
        self.name= name 
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.append(book)
        else:
            print(f"You haven't borrowed '{book.title}'.")

    def __str__(self):
        return self.name