class MockRegistry:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MockRegistry, cls).__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set_value(self, key, value):
        self._settings[key] = value

    def get_value(self, key):
        return self._settings.get(key)

    def delete_value(self, key):
        if key in self._settings:
            del self._settings[key]


# Usage
registry1 = MockRegistry()
registry1.set_value('background_color', 'blue')

registry2 = MockRegistry()
print(registry2.get_value('background_color'))  # Outputs: blue

# Both registry1 and registry2 refer to the same instance, so the settings are shared.
