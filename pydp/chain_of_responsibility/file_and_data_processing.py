import os

class DataProcessor:
    def __init__(self):
        self.next_processor = None

    def set_next_processor(self, next_processor):
        self.next_processor = next_processor

    def process_data(self, data):
        pass

class FileLoader(DataProcessor):
    def process_data(self, data):
        if os.path.isfile(data):
            with open(data, 'r') as file:
                content = file.read()
            print(f"FileLoader: Loaded data from file: {content}")
        elif self.next_processor is not None:
            print("FileLoader: Data is not a file. Passing to the next processor.")
            self.next_processor.process_data(data)
        else:
            print("FileLoader: Data is not a file and no further processors available.")

class CSVParser(DataProcessor):
    def process_data(self, data):
        if data.endswith('.csv'):
            print("CSVParser: Parsing CSV data...")
            # Add CSV parsing logic here
        elif self.next_processor is not None:
            print("CSVParser: Data is not CSV. Passing to the next processor.")
            self.next_processor.process_data(data)
        else:
            print("CSVParser: Data is not CSV and no further processors available.")

class JSONParser(DataProcessor):
    def process_data(self, data):
        if data.endswith('.json'):
            print("JSONParser: Parsing JSON data...")
            # Add JSON parsing logic here
        elif self.next_processor is not None:
            print("JSONParser: Data is not JSON. Passing to the next processor.")
            self.next_processor.process_data(data)
        else:
            print("JSONParser: Data is not JSON and no further processors available.")

# Create a chain of data processors
file_loader = FileLoader()
csv_parser = CSVParser()
json_parser = JSONParser()

file_loader.set_next_processor(csv_parser)
csv_parser.set_next_processor(json_parser)

# Process data
data1 = "data.csv"
data2 = "data.json"
data3 = "not_data.txt"

print("Processing data 1:")
file_loader.process_data(data1)
print("---")

print("Processing data 2:")
file_loader.process_data(data2)
print("---")

print("Processing data 3:")
file_loader.process_data(data3)
