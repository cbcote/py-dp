class CacheManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CacheManager, cls).__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def set(self, key, value):
        self._cache[key] = value

    def get(self, key):
        return self._cache.get(key)

    def has_key(self, key):
        return key in self._cache


# Usage
cache1 = CacheManager()
cache1.set('user_123', {'name': 'John', 'age': 30})

cache2 = CacheManager()
print(cache2.get('user_123'))  # Outputs: {'name': 'John', 'age': 30}

# Both cache1 and cache2 refer to the same instance, so the cached data is shared.
