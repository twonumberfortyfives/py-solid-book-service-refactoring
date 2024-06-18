import json
import xml.etree.ElementTree as ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        if display_type == "console":
            self._display_console()
        elif display_type == "reverse":
            self._display_reverse()
        else:
            raise ValueError(f"Invalid display type: {display_type}")

    def _display_console(self) -> None:
        print(self.content)

    def _display_reverse(self) -> None:
        print(self.content[::-1])

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            self._print_console_book()
        elif print_type == "reverse":
            self._print_reverse_book()
        else:
            raise ValueError(f"Invalid print type: {print_type}")

    def _print_console_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        self._display_console()

    def _print_reverse_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        self._display_reverse()

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return self._serialize_json()
        elif serialize_type == "xml":
            return self._serialize_xml()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

    def _serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def _serialize_xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
