class Book:
    # define attribute tied to the class above 
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def display_books(self):
        print(self.books)
        # for book in self.books:
        #     print(book.title)
    
    def display_members(self):
        for member in self.members:
            print(member.name)

    def remove_book(self, book):
        if book in self.books:
            print(f"books found {book.title}")
            self.books.remove(book)
        else:
            print("Book not found")

book_one = Book("Rich dad, poor dad", "Robert Kiyosaki", "12345rfdskjnv")
print(book_one)
book_two = Book("48 Laws of power", "Robert Green", "2345tgdsje")
book_three = Book("River and the source", "Margaret Ogola", "12345rfdtfssv")
print(book_one.author) # Rich dad, poor dad
moringa_library = Library()

moringa_library.add_book(book_one)
moringa_library.add_book(book_two)

moringa_library.display_books() # Rich dad, poor dad
moringa_library.remove_book(book_three) # Rich dad, poor dad