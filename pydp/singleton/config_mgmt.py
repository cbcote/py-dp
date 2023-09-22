class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config = {}
        return cls._instance

    def set_config(self, key, value):
        self._config[key] = value

    def get_config(self, key):
        return self._config.get(key)


# Usage
config1 = ConfigurationManager()
config1.set_config('database_url', 'localhost:5432')

config2 = ConfigurationManager()
print(config2.get_config('database_url'))  # Outputs: localhost:5432

# Both config1 and config2 refer to the same instance, so the configuration is shared.
