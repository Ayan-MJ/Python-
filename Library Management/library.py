class Library:

    def __init__(self, days):
        self.books = []
        self.days = 30

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in library")
        else:
            print("Books in library")
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return  book
        return None
    
