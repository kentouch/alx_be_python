### Create a book class that implements __init__ (constructor), __del__ (destructor), __str__ (string representation) methods
## and __repr__ (official string representation)

class Book:
    # constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # destructor
    def __del__(self):
        print(f"Deleting {self.title}")

    # string representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # official string representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"