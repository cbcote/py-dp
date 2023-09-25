import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, data):
        self.data = data

    def clone(self):
        # Create a shallow copy of the object
        return copy.copy(self)

# Create an instance of the prototype
prototype = ConcretePrototype("Initial Data")

# Clone the prototype to create new objects
clone1 = prototype.clone()
clone2 = prototype.clone()

# Modify the cloned objects
clone1.data = "Modified Data 1"
clone2.data = "Modified Data 2"

# Print the original and cloned data
print("Original Prototype Data:", prototype.data)
print("Clone 1 Data:", clone1.data)
print("Clone 2 Data:", clone2.data)
