class TestObject:
    def operation(self) -> str:
        pass


# Concrete test objects and their mock counterparts
class RealService(TestObject):
    def operation(self) -> str:
        return 'Real service operation'


class MockService(TestObject):
    def operation(self) -> str:
        return 'Mock service operation'


class RealDatabase(TestObject):
    def operation(self) -> str:
        return 'Real database operation'


class MockDatabase(TestObject):
    def operation(self) -> str:
        return 'Mock database operation'


# Test Factory to create specific test or mock objects
class TestFactory:
    @staticmethod
    def create_test_object(object_type: str, use_mock: bool = False) -> TestObject:
        if object_type == 'Service':
            return MockService() if use_mock else RealService()
        elif object_type == 'Database':
            return MockDatabase() if use_mock else RealDatabase()
        else:
            raise ValueError(f'Unknown object type: {object_type}')


# Usage
object_types = ['Service', 'Database']
for object_type in object_types:
    real_object = TestFactory.create_test_object(object_type)
    mock_object = TestFactory.create_test_object(object_type, use_mock=True)
    print(f'Real {object_type} operation:', real_object.operation())
    print(f'Mock {object_type} operation:', mock_object.operation())
    print('---')
