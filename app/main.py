from app.abstract_classes import IBookDisplay, IBookPrint, IBookSerializer
from app.book_display import ConsoleBookDisplay, ReverseBookDisplay
from app.book_model import Book
from app.book_print import ConsoleBookPrint, ReverseBookPrint
from app.serializers import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy: IBookDisplay
            if method_type == "console":
                display_strategy = ConsoleBookDisplay()
            elif method_type == "reverse":
                display_strategy = ReverseBookDisplay()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            display_strategy.display(book)
        elif cmd == "print":
            print_strategy: IBookPrint
            if method_type == "console":
                print_strategy = ConsoleBookPrint()
            elif method_type == "reverse":
                print_strategy = ReverseBookPrint()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            print_strategy.print(book)
        elif cmd == "serialize":
            serialize_strategy: IBookSerializer
            if method_type == "json":
                serialize_strategy = JSONBookSerializer()
            elif method_type == "xml":
                serialize_strategy = XMLBookSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serialize_strategy.serialize(book)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
