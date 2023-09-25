class ConnectionState:
    def handle(self, connection):
        pass


class Connected(ConnectionState):
    def handle(self, connection):
        print('Connection is already established.')


class Disconnected(ConnectionState):
    def handle(self, connection):
        print('Connection lost. Trying to reconnect...')
        connection.set_state(Reconnecting())


class Reconnecting(ConnectionState):
    def handle(self, connection):
        print('Reconnecting...')
        # Mock reconnection logic
        connection.set_state(Connected())
        print('Reconnected successfully.')


class Connection:
    def __init__(self):
        self.state = Disconnected()

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


# Usage
connection = Connection()
connection.request()  # Tries to reconnect
connection.request()  # Already connected
