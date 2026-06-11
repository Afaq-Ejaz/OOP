class Book:
    def __init__(self , title , author ):
        self.title = title
        self.author = author
        self.is_av = True

    def borrow(self):

        if(self.is_av == True):
           print(f"This book {self.title} has been borrowd")
           self.is_av = False
        else:
            print("This book has already been borrowwed")
    
    def returnb(self):
        print("This book has been returned...")
        self.is_av = True
        
# # Create an object
# my_book = Book("The Hobbit", "J.R.R. Tolkien")

# # Test methods
# my_book.borrow()  # Should say: "The Hobbit" has been borrowed.
# my_book.borrow()  # Should say: Sorry, "The Hobbit" is already borrowed.
# my_book.returnb()  # Should say: "The Hobbit" has been returned.

class Library:
    def __init__(self, name: str , books: list) -> None:
        self.name = name
        self.books = books
    
    def add_book(self , book_obj):
        self.books.append(book_obj)
    
    def display_available_books(self):
        for current_book in self.books:  # current_book is the Book object!
            if current_book.is_av == True:  # Check THAT book's availability
                print(f"{current_book.title} by {current_book.author}") # Get THAT book's data

# 1. Create a Library
my_library = Library("City Tech Library" , [])

# 2. Create Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("Dune", "Frank Herbert")

# 3. Add books to library (Combining objects)
my_library.add_book(book1)
my_library.add_book(book2)

# 4. Test functionality
book1.borrow()  # Borrow 1984
my_library.display_available_books()  # Should ONLY display "Dune by Frank Herbert"
