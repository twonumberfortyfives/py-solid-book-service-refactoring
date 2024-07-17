from app.serializers import BookSerializer
from app.book_model import Book
from app.book_display import BookDisplay
from app.book_print import BookPrint


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> type(BookSerializer) | None:

    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display_book(book, method_type)
        elif cmd == "print":
            BookPrint.print_book(book, method_type)
        elif cmd == "serialize":
            if method_type == "json":
                return BookSerializer.serialize_json(book, method_type)
            elif method_type == "xml":
                return BookSerializer.serialize_xml(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
