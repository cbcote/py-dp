class DataValidator:
    def __init__(self):
        self.next_validator = None

    def set_next_validator(self, next_validator):
        self.next_validator = next_validator

    def validate(self, data):
        pass

class EmailValidator(DataValidator):
    def validate(self, data):
        if "@" in data:
            print("EmailValidator: Email format is valid.")
        elif self.next_validator is not None:
            print("EmailValidator: Email format is invalid. Passing to the next validator.")
            self.next_validator.validate(data)

class PasswordValidator(DataValidator):
    def validate(self, data):
        if len(data) >= 8:
            print("PasswordValidator: Password length is valid.")
        elif self.next_validator is not None:
            print("PasswordValidator: Password length is invalid. Passing to the next validator.")
            self.next_validator.validate(data)

class UsernameValidator(DataValidator):
    def validate(self, data):
        if data.isalnum():
            print("UsernameValidator: Username format is valid.")
        else:
            print("UsernameValidator: Username format is invalid.")

# Create a chain of data validators
email_validator = EmailValidator()
password_validator = PasswordValidator()
username_validator = UsernameValidator()

email_validator.set_next_validator(password_validator)
password_validator.set_next_validator(username_validator)

# Validate data
data1 = "user@example.com"
data2 = "pass123"
data3 = "user123!"

email_validator.validate(data1)
print("---")
email_validator.validate(data2)
print("---")
email_validator.validate(data3)
