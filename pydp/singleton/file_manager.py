class MockFileManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MockFileManager, cls).__new__(cls)
            cls._instance._files = {}
        return cls._instance

    def create_file(self, filename, content):
        self._files[filename] = content

    def read_file(self, filename):
        return self._files.get(filename)

    def delete_file(self, filename):
        if filename in self._files:
            del self._files[filename]


# Usage
file_manager1 = MockFileManager()
file_manager1.create_file('document.txt', 'Hello, world!')

file_manager2 = MockFileManager()
print(file_manager2.read_file('document.txt'))  # Outputs: Hello, world!

# Both file_manager1 and file_manager2 refer to the same instance, so the files are shared.
