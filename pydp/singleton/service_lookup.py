class Service:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'Executing service: {self.name}')


class ServiceLocator:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ServiceLocator, cls).__new__(cls)
            cls._instance._services = {}
        return cls._instance

    def register_service(self, name, service):
        self._services[name] = service

    def get_service(self, name):
        return self._services.get(name)


# Usage
serviceA = Service('ServiceA')
serviceB = Service('ServiceB')

locator1 = ServiceLocator()
locator1.register_service('ServiceA', serviceA)

locator2 = ServiceLocator()
locator2.register_service('ServiceB', serviceB)

# Both locator1 and locator2 refer to the same instance, so the services are shared.
found_service = locator1.get_service('ServiceB')
found_service.execute()  # Outputs: Executing service: ServiceB
