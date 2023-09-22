class Button:
    def render(self) -> str:
        pass


# Concrete button classes for different platforms
class WindowsButton(Button):
    def render(self) -> str:
        return 'Rendering a Windows-style button'


class MacOSButton(Button):
    def render(self) -> str:
        return 'Rendering a macOS-style button'


class LinuxButton(Button):
    def render(self) -> str:
        return 'Rendering a Linux-style button'


# GUI Factory to create platform-specific buttons
class GUIFactory:
    @staticmethod
    def create_button(platform: str) -> Button:
        if platform == 'Windows':
            return WindowsButton()
        elif platform == 'macOS':
            return MacOSButton()
        elif platform == 'Linux':
            return LinuxButton()
        else:
            raise ValueError(f'Unknown platform: {platform}')


# Usage
platforms = ['Windows', 'macOS', 'Linux']
for platform in platforms:
    button = GUIFactory.create_button(platform)
    print(button.render())
