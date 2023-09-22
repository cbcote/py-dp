import re

# Define the Strategy interface
class ValidationStrategy:
    def validate(self, data: str) -> bool:
        pass

# Implement concrete strategies
class EmailValidation(ValidationStrategy):
    def validate(self, data: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, data))

class PhoneNumberValidation(ValidationStrategy):
    def validate(self, data: str) -> bool:
        pattern = r'^\+?\d{1,3}?[- .]?\(?\d{1,4}?\)?[- .]?\d{1,4}[- .]?\d{1,4}[- .]?\d{1,9}$'
        return bool(re.match(pattern, data))

# Context class
class Validator:
    def __init__(self, strategy: ValidationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy):
        self._strategy = strategy

    def execute_validation(self, data: str) -> bool:
        return self._strategy.validate(data)


# Usage
data_email = 'user@example.com'
data_phone = '+123-456-7890'

# Using EmailValidation
validator = Validator(EmailValidation())
print(f'Is "{data_email}" a valid email? {validator.execute_validation(data_email)}')

# Switching to PhoneNumberValidation
validator.set_strategy(PhoneNumberValidation())
print(f'Is "{data_phone}" a valid phone number? {validator.execute_validation(data_phone)}')
