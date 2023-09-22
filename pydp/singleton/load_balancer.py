import random


class MockLoadBalancer:
    _instance = None

    def __new__(cls, servers=None):
        if not cls._instance:
            cls._instance = super(MockLoadBalancer, cls).__new__(cls)
            cls._instance._servers = servers or []
        return cls._instance

    def add_server(self, server):
        if server not in self._servers:
            self._servers.append(server)

    def get_server(self):
        return random.choice(self._servers) if self._servers else None


# Usage
load_balancer1 = MockLoadBalancer(['Server1', 'Server2'])
print(load_balancer1.get_server())  # Outputs: Server1 or Server2 (randomly)

load_balancer2 = MockLoadBalancer()
load_balancer2.add_server('Server3')
print(load_balancer2.get_server())  # Outputs: Server1, Server2, or Server3 (randomly)

# Both load_balancer1 and load_balancer2 refer to the same instance, so the server list is shared.
