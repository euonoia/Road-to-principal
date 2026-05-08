class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    # The Dunder (Double Under) Method __str__:
    # This is a pro move! It defines how the object looks when you print it.
    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        # Composition: The library 'has-a' list of Book objects.
        self.books = []
    
    def add_book(self, book_object):
        self.books.append(book_object)
        print(f"Added book: {book_object.title}")

    def show_all_books(self):
        print("\n--- Library Catalog ---")
        for book in self.books:
            # This calls the __str__ method you defined in the Book class!
            print(book)

    def show_author(self, author):
        print(f"\n--- Books by {author} ---")
        for book in self.books:
            if book.author.lower() == author.lower():
                print(book)
        
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Success! You returned '{book.title}'.")
                    return
                else:
                    print(f"Notice: '{book.title}' was already here.")
                    return
        print(f"Error: '{title}' not found.")
            
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"Success! You borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently checked out.")
                    return
        print(f"Error: '{title}' not found.")

# --- Execution ---
my_library = Library()
my_library.add_book(Book("The Hobbit", "Tolkien"))
my_library.add_book(Book("Resident Evil", "Ken"))

my_library.show_all_books()
my_library.borrow_book("The Hobbit")
my_library.show_all_books()