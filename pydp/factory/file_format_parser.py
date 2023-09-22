class FileParser:
    def parse(self, content: str) -> dict:
        pass


# Concrete parser classes for different file formats
class JSONParser(FileParser):
    def parse(self, content: str) -> dict:
        # Mock implementation for JSON parsing
        return {'type': 'JSON', 'data': content}


class XMLParser(FileParser):
    def parse(self, content: str) -> dict:
        # Mock implementation for XML parsing
        return {'type': 'XML', 'data': content}


class CSVParser(FileParser):
    def parse(self, content: str) -> dict:
        # Mock implementation for CSV parsing
        return {'type': 'CSV', 'data': content}


# Parser Factory to create specific file format parsers
class ParserFactory:
    @staticmethod
    def create_parser(format_type: str) -> FileParser:
        if format_type == 'JSON':
            return JSONParser()
        elif format_type == 'XML':
            return XMLParser()
        elif format_type == 'CSV':
            return CSVParser()
        else:
            raise ValueError(f'Unknown format type: {format_type}')


# Usage
format_types = ['JSON', 'XML', 'CSV']
content = 'sample_content'
for format_type in format_types:
    parser = ParserFactory.create_parser(format_type)
    print(parser.parse(content))
