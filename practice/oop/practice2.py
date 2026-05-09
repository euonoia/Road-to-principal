class Book:
    def __init__(self, title, author, yearPublished, ):
        self.title =  title
        self.author = author
        self.yearPublished = yearPublished
        self.isBorrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"
    def information(self):
        print(f"the book {self.title} is published on {self.yearPublished} that written by {self.author} and published on {self.yearPublished} and its {self.isBorrowed}")
    
    def borrow_book(self):
        if self.isBorrowed == False:
            self.isBorrowed = True
            print(f"You can borrow the book {self.title} by {self.author}")
        else:
            print("The Book is Unavailable")
    
    def return_book(self):
        if self.isBorrowed == True:
            self.isBorrowed = False
            print(f"Thank you for returning the book named {self.title}")
        else:
            print("The Book Is Not Borrowed") 



class Library:

    def __init__(self):
        self.books = []
    
    def add_books(self,book):
        self.books.append(book)
   
    def display_all_books(self):
        for book in self.books:
            print(book)

            
        

my_book = Book("Lebroners","King James",2006)
my_library = Library()

my_book.information()

my_book.borrow_book()
my_book.borrow_book()

my_book.return_book()
my_book.return_book()

my_library.add_books(my_book)
my_library.display_all_books()