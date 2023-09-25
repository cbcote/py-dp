import copy

class Prototype:
    def clone(self):
        pass

class ExpensiveObject(Prototype):
    def __init__(self, data):
        # Simulate the expensive initialization process
        self.data = data
        self.initialize_expensive_resource()

    def initialize_expensive_resource(self):
        # Simulate the costly initialization process
        print("Initializing expensive resource...")

    def clone(self):
        # Create a shallow copy of the object
        return copy.copy(self)

# Create an instance of the expensive object
expensive_instance = ExpensiveObject("Initial Data")

# Clone the expensive object to avoid costly reinitialization
cheap_clone = expensive_instance.clone()

# Modify the clone
cheap_clone.data = "Modified Data"

# Print the original and cloned data
print("Original Expensive Data:", expensive_instance.data)
print("Cheap Clone Data:", cheap_clone.data)
