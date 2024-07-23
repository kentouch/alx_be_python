### class Book implements __init__ (constructor), 
# with atttributes title and author,
# and we build Ebook and PrintedBook classes inherites the Book class
# we have library system that implements Book, PrintedBook and Ebook classes


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
# Ebook class derived from Book class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Printbook class derived from Book class
class PrintBook(Book):
    # initialize attributes from base class __init__
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
# composition Library class
class Library:
    # initialize a list to store instance of Books, Ebooks and PrintBooks
    def __init__(self):
        self.books = []

    # add book instance method to add books in the list
    def add_book(self, book):
        self.book = book
        self.books.append(self.book)
    
    # list all the book in the library using list_books method
    def list_books(self):
        for b in self.books:
            print(b)
            
            
            
            
