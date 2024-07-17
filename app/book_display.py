from app.book_model import Book


class BookDisplay:
    @staticmethod
    def display_book(book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookDisplayReverse:
    @staticmethod
    def display_book_reverse(book: Book, display_type: str) -> None:
        if display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")
