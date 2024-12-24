
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def list_books(self):
        return [{"title": book.title, "author": book.author, "status": "Available" if book.is_available else "Borrowed"} for book in self.books]

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.borrow()
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.return_book()
                return True
        return False


if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print("Book added successfully.")
        elif choice == "2":
            books = library.list_books()
            print("\nBooks in Library:")
            for idx, book in enumerate(books, start=1):
                print(f"{idx}. {book['title']} by {book['author']} - {book['status']}")
        elif choice == "3":
            title = input("Enter book title to borrow: ")
            if library.borrow_book(title):
                print("You have borrowed the book.")
            else:
                print("Book is not available.")
        elif choice == "4":
            title = input("Enter book title to return: ")
            if library.return_book(title):
                print("You have returned the book.")
            else:
                print("Book not found or already returned.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
