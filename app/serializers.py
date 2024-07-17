import json
import xml.etree.ElementTree as ET


class BookSerializer:

    @staticmethod
    def serialize_json(book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

    @staticmethod
    def serialize_xml(book, serialize_type: str) -> str:
        if serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = book.title
            content = ET.SubElement(root, "content")
            content.text = book.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
