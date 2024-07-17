from app.book_model import Book


class BookPrint:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookPrintReverse:
    @staticmethod
    def print_book_reverse(book: Book, print_type: str) -> None:
        if print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")
