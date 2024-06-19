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
