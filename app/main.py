from app.serializing import Serializer
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        if cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            serializer = Serializer(book)
            return serializer.serialize(method_type)
