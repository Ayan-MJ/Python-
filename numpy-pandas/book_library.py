import pandas as pd

library_data = {
    "Title": ["Harry Potter 1", "Harry potter 2", "The Hobbit", "Modern AI", "Data Science 101"],
    "Author": ["J.K. Rowling", "J.K. Rowling", "J.R.R Tolkien", "John Doe", "Jane Smith"],
    "Year": [1997, 1998, 1937, 2021, 2018]
}

library_df = pd.DataFrame(library_data)
print(library_df)

# Book Published after 2010
published_book = library_df[library_df["Year"] > 2010]
print("Books after 2010:\n", published_book)

# Oldest book
oldest_book = library_df[library_df["Year"] == library_df["Year"].min()]
print("\nOldest book:\n", oldest_book)

# Count how many books each author has
author_count = library_df["Author"].value_counts()
print("\nNumber of books per author:\n", author_count)




