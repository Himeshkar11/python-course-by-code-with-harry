class Library:
    def __init__(self, booklists, lib_name):
        self.books = booklists
        self.lib_name = lib_name
        self.book_lend = {}   # key = book, value = borrower

    def Display_book(self):
        for book in self.books:
            if book in self.book_lend:
                print(f"{book} already lent to {self.book_lend[book]}")
            else:
                print(f"{book} is available")

    def Lend_book(self, book_name, user):
        if book_name not in self.books:
            print(f"This {book_name} does not exist in library")
        elif book_name not in self.book_lend:
            self.book_lend[book_name] = user
            print(f"{user} borrowed {book_name}")
        else:
            print(f"Sorry, the book is already lent to {self.book_lend[book_name]}")

    def Add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            print(f"{book_name} added to the library")
        else:
            print(f"{book_name} is already in library")

    def Return_book(self, book_name):
        if book_name in self.book_lend:
            user = self.book_lend.pop(book_name)
            print(f"{user} has returned {book_name}")
        else:
            print("This book was not lent out")


if __name__ == "__main__":
    my_books = ["Python Basics", "Harry Potter", "Algorithms"]
    myLibrary = Library(my_books, "Harry Library")

    while True:
        print("\nSelect an option:")
        print("1 - Display Books")
        print("2 - Add Book")
        print("3 - Lend Book")
        print("4 - Return Book")
        print("5 - Exit")

        n = int(input("Enter your choice: "))

        if n == 1:
            myLibrary.Display_book()
        elif n == 2:
            book = input("Enter book name to add: ")
            myLibrary.Add_book(book)
        elif n == 3:
            book = input("Enter book name to lend: ")
            user = input("Enter your name: ")
            myLibrary.Lend_book(book, user)
        elif n == 4:
            book = input("Enter book name to return: ")
            myLibrary.Return_book(book)
        elif n == 5:
            print("Exiting...")
            break
        else:
            print("Please choose a correct number")
