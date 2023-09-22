class Book:
    def __init__(self, title, author, pages, genre):
        self._title = title
        self._author = author
        self._pages = pages
        self._genre = genre

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @property
    def genre(self):
        return self._genre

    def __str__(self):
        return f'"{self._title}" by {self._author}, {self._pages} pages, Genre: {self._genre}'


class BookBuilder:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._pages = 0
        self._genre = 'Unknown'

    def set_pages(self, pages):
        self._pages = pages
        return self

    def set_genre(self, genre):
        self._genre = genre
        return self

    def build(self):
        return Book(self._title, self._author, self._pages, self._genre)


# Usage
builder = BookBuilder('The Great Gatsby', 'F. Scott Fitzgerald')
book = (builder.set_pages(218)
        .set_genre('Novel')
        .build())
print(book)  # Outputs: "The Great Gatsby" by F. Scott Fitzgerald, 218 pages, Genre: Novel
