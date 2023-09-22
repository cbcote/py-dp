class ResourceManager:
    def allocate(self) -> str:
        pass

    def release(self) -> str:
        pass


# Concrete resource manager classes for different resources
class MemoryManager(ResourceManager):
    def allocate(self) -> str:
        return 'Allocated memory resource'

    def release(self) -> str:
        return 'Released memory resource'


class DiskManager(ResourceManager):
    def allocate(self) -> str:
        return 'Allocated disk resource'

    def release(self) -> str:
        return 'Released disk resource'


class NetworkManager(ResourceManager):
    def allocate(self) -> str:
        return 'Allocated network resource'

    def release(self) -> str:
        return 'Released network resource'


# Resource Factory to create specific resource managers
class ResourceFactory:
    @staticmethod
    def create_manager(resource_type: str) -> ResourceManager:
        if resource_type == 'Memory':
            return MemoryManager()
        elif resource_type == 'Disk':
            return DiskManager()
        elif resource_type == 'Network':
            return NetworkManager()
        else:
            raise ValueError(f'Unknown resource type: {resource_type}')


# Usage
resources = ['Memory', 'Disk', 'Network']
for resource_type in resources:
    manager = ResourceFactory.create_manager(resource_type)
    print(manager.allocate())
    print(manager.release())
    print('---')
