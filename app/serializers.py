import json
from xml.etree import ElementTree

from app.book_model import Book


class BookSerializerJson:

    @staticmethod
    def serialize_json(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class BookSerializerXml:
    @staticmethod
    def serialize_xml(book: Book, serialize_type: str) -> str:
        if serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
