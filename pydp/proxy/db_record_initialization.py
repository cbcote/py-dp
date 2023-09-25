import copy

class DatabaseRecord:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def clone(self):
        pass

class EmployeeRecord(DatabaseRecord):
    def clone(self):
        return copy.copy(self)

class ProductRecord(DatabaseRecord):
    def clone(self):
        return copy.copy(self)

# Create prototype records for an employee and a product
employee_prototype = EmployeeRecord(1, "John Doe")
product_prototype = ProductRecord(101, "Widget")

# Clone the prototype records to initialize new records
employee_record1 = employee_prototype.clone()
employee_record2 = employee_prototype.clone()

product_record1 = product_prototype.clone()
product_record2 = product_prototype.clone()

# Modify the cloned records
employee_record1.id = 2
employee_record1.name = "Jane Smith"

product_record1.id = 102
product_record1.name = "Gadget"

# Print the original and cloned database records
print("Employee Prototype:", employee_prototype.id, employee_prototype.name)
print("Employee Record 1:", employee_record1.id, employee_record1.name)
print("Employee Record 2:", employee_record2.id, employee_record2.name)

print("Product Prototype:", product_prototype.id, product_prototype.name)
print("Product Record 1:", product_record1.id, product_record1.name)
print("Product Record 2:", product_record2.id, product_record2.name)
