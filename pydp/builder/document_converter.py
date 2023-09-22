class Document:
    def __init__(self, content):
        self._content = content

    def __str__(self):
        return self._content


class DocumentConverter:
    def __init__(self, document):
        self._document = document

    def to_uppercase(self):
        self._document._content = self._document._content.upper()
        return self

    def to_lowercase(self):
        self._document._content = self._document._content.lower()
        return self

    def add_prefix(self, prefix):
        self._document._content = prefix + self._document._content
        return self

    def add_suffix(self, suffix):
        self._document._content += suffix
        return self

    def build(self):
        return self._document


# Usage
original_document = Document('Hello, World!')
converter = DocumentConverter(original_document)
converted_document = (converter.to_uppercase()
                       .add_prefix('Greeting: ')
                       .add_suffix(' Have a nice day.')
                       .build())
print(converted_document)  # Outputs: Greeting: HELLO, WORLD! Have a nice day.
