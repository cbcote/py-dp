class DatabaseConnection:
    _instance = None

    def __new__(cls, db_url=None):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._db_url = db_url
            cls._instance._connected = False
        return cls._instance

    def connect(self):
        if not self._connected:
            # Mock connection logic
            print(f'Connecting to database at {self._db_url}...')
            self._connected = True
            print('Connected!')
        else:
            print('Already connected!')

    def disconnect(self):
        if self._connected:
            # Mock disconnection logic
            print('Disconnecting...')
            self._connected = False
            print('Disconnected!')


# Usage
conn1 = DatabaseConnection('localhost:5432')
conn1.connect()

conn2 = DatabaseConnection('localhost:5432')
conn2.connect()  # Will print 'Already connected!'

# Both conn1 and conn2 refer to the same instance.
conn1.disconnect()
