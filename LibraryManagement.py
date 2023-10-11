class LibraryManagement:
    def __init__(self,no_of_books,books):
        self.no_of_books = no_of_books
        self.books = books

    def no_of_books(self):
        print(f"Number of books in the Library is {self.no_of_books} ")

    def books_in_library(self):
        self.books = ['Gods of Water','Dragon Ball','Naruto','Attack on Titan']
        print(self.books)

    def add_books(self,name):
        (self.books).append(self.name)
        self.no_of_books = self.no_of_books + 1

    
L = LibraryManagement(4,)