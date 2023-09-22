class UserInterface:
    def __init__(self):
        self._components = []

    def add_component(self, component):
        self._components.append(component)

    def __str__(self):
        return ' -> '.join(self._components)


class InterfaceBuilder:
    def __init__(self):
        self.ui = UserInterface()

    def add_button(self, label):
        self.ui.add_component(f'Button({label})')
        return self

    def add_label(self, text):
        self.ui.add_component(f'Label({text})')
        return self

    def add_textbox(self, placeholder):
        self.ui.add_component(f'Textbox({placeholder})')
        return self

    def build(self):
        return self.ui


# Usage
builder = InterfaceBuilder()
custom_ui = (builder.add_label('Username')
            .add_textbox('Enter username')
            .add_label('Password')
            .add_textbox('Enter password')
            .add_button('Login')
            .build())
print(custom_ui)  # Outputs: Label(Username) -> Textbox(Enter username) -> Label(Password) -> Textbox(Enter password) -> Button(Login)
