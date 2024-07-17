from app.serializers import BookSerializerJson, BookSerializerXml
from app.book_model import Book
from app.book_display import BookDisplay, BookDisplayReverse
from app.book_print import BookPrint, BookPrintReverse


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> type(BookSerializerXml) | type(BookSerializerJson) | None:

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                BookDisplayReverse.display_book_reverse(book, method_type)
            else:
                BookDisplay.display_book(book, method_type)
        elif cmd == "print":
            if method_type == "reverse":
                BookPrintReverse.print_book_reverse(book, method_type)
            else:
                BookPrint.print_book(book, method_type)
        elif cmd == "serialize":
            if method_type == "json":
                return BookSerializerJson.serialize_json(book, method_type)
            elif method_type == "xml":
                return BookSerializerXml.serialize_xml(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
