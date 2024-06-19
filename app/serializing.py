from book import Book
import json
import xml.etree.ElementTree as ElementTree


class Serializer:
    def __init__(self, book: Book):
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return self._serialize_json()
        elif serialize_type == "xml":
            return self._serialize_xml()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

    def _serialize_json(self) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})

    def _serialize_xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
