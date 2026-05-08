class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,books):
        self.books.append(books)
        print(f"added book{books.title}")


    def show_all_books(self):
        print("\n--- Library Catalog ---")
        for book in self.books:
            print(book)

    def show_author(self, author):
        print("\n--- Showing all the Author Books ---")
        for book in self.books:
            if book.author.lower() == author.lower():
                print(book)
        
    def return_book (self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available != True:
                    book.is_available = True
                    print(f"\n Success! You returned '{book.title}'.")
                    return
                else:
                    print(f"\n Sorry '{book.title}' is already returned.")

            print(f"\n Error: '{title}' not found in catalog")
            
    def borrow_book (self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"\n Success! You Borrowed '{book.title}'.")
                    return
                else:
                    print(f"\n Sorry '{book.title}' is already checked out.")
                    return
            
            print(f"\n Error: '{title}' not found in catalog")

# --- Execution ---
my_library = Library()

# Create Books Object
b1 = Book("The Hobbit","Lebron")
b2 = Book("Resident Evil", "Ken")

# Adding them to the library
my_library.add_book(b1)
my_library.add_book(b2)

#use The system 
my_library.show_all_books()
my_library.borrow_book("The Hobbit")
my_library.show_all_books()

#return Function
my_library.return_book("The Hobbit")
my_library.show_all_books()

my_library.show_author("Ken")
