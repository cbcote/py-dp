class ApplicationState:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ApplicationState, cls).__new__(cls)
            cls._instance._state = {}
        return cls._instance

    def set_state(self, key, value):
        self._state[key] = value

    def get_state(self, key):
        return self._state.get(key)

    def delete_state(self, key):
        if key in self._state:
            del self._state[key]


# Usage
app_state1 = ApplicationState()
app_state1.set_state('user_id', 12345)

app_state2 = ApplicationState()
print(app_state2.get_state('user_id'))  # Outputs: 12345

# Both app_state1 and app_state2 refer to the same instance, so the application state is shared.
