class ConnectionPool:
    _instance = None

    def __new__(cls, size=5):
        if not cls._instance:
            cls._instance = super(ConnectionPool, cls).__new__(cls)
            cls._instance._pool = [f'Connection {i+1}' for i in range(size)]
        return cls._instance

    def acquire(self):
        if self._pool:
            return self._pool.pop()
        else:
            print('No available connections!')
            return None

    def release(self, connection):
        self._pool.append(connection)


# Usage
pool1 = ConnectionPool(3)
conn_a = pool1.acquire()
print(f'Acquired: {conn_a}')

pool2 = ConnectionPool(3)
conn_b = pool2.acquire()
print(f'Acquired: {conn_b}')

pool1.release(conn_a)
pool2.release(conn_b)

# Both pool1 and pool2 refer to the same instance, so the connections are shared.
