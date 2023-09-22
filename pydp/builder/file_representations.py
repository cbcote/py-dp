class FileRepresentation:
    def __init__(self):
        self._attributes = {}

    def set_attribute(self, key, value):
        self._attributes[key] = value

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in self._attributes.items())


class FileBuilder:
    def __init__(self, filename):
        self.file_repr = FileRepresentation()
        self.file_repr.set_attribute('Filename', filename)

    def set_filetype(self, filetype):
        self.file_repr.set_attribute('Filetype', filetype)
        return self

    def set_size(self, size):
        self.file_repr.set_attribute('Size', size)
        return self

    def set_creation_date(self, date):
        self.file_repr.set_attribute('Creation Date', date)
        return self

    def set_permissions(self, permissions):
        self.file_repr.set_attribute('Permissions', permissions)
        return self

    def build(self):
        return self.file_repr


# Usage
builder = FileBuilder('document.txt')
custom_file_repr = (builder.set_filetype('Text')
                    .set_size('5MB')
                    .set_creation_date('2023-09-21')
                    .set_permissions('Read-Write')
                    .build())
print(custom_file_repr)  # Outputs: Filename: document.txt, Filetype: Text, Size: 5MB, Creation Date: 2023-09-21, Permissions: Read-Write
