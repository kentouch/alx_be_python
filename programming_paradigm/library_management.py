
###  Solidify understanding of basic OOP concepts in Python by 
###  implementing a system that tracks books in a library, 
###  focusing on classes, object instantiation, and method invocation.

## Implement a "Book" class with public attributes "title" and "author", 
## and a private attribute "_is_checked_out" to track its availability.
## Implement a "Library" class with a private "list _books" to store instances of Book. 
## Include methods to "add_book", "check_out_book(title)", 
## "return_book(title)", and "list_available_books".

# Book class
class Book:
    
    __is_checked_out = False
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # is abook checked out yes or no
    def is_checked_out(self):
        return self.__is_checked_out
        
    
    # Iis a book checked out or not
    """def checked_out(self, __is_checked_out):
        self.__is_checked_out = __is_checked_out"""

# Library class
class Library:

    # Creating an empty list
    __list_books = []
    # Adding a book in the Library
    def add_book(self, book):
        self.book = book
        # Adding the book in the list
        self.__list_books.append(self.book) 
    # Checked out a book in the Library
    def check_out_book(self, title):
        self.title = title
        self._is_checked_out = self.book.is_checked_out()
        # checking if the title corresponds to one of the books kept in the library
        if self._is_checked_out == False:
                self.__list_books.remove(self.book)
                self._is_checked_out = True
    # return book function is used to return the book back into the list of Books    
    def return_book(self, title):
        self.title = title
        if self._is_checked_out == True:
                self.__list_books.append(self.book)
    def list_available_books(self):
        for b in self.__list_books:
            print(b.title, b.author)
    


def main():
    book1 = Book("Harry Poter", "JK Rowling")
    book2 = Book("Superman", "Clark Kent")
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
 #   library.return_book("The Crystal")
    library.check_out_book("Harry Poter")
    library.list_available_books()
    print()
    library.return_book("Harry Poter")
    library.list_available_books()

if __name__=="__main__":
    main()



    

