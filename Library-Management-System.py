Library-Management-System
# library_management_system.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")


# Example usage
library = Library()
library.add_book("Introduction to Python")
library.add_book("Data Structures and Algorithms")
library.add_book("Database Management")
library.display_books()
library.remove_book("Introduction to Python")
library.remove_book("Artificial Intelligence")
library.display_books()
