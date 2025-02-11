class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is alread borrowed")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Thank you for returning '{self.title}' by{self.author}.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"
    



    
