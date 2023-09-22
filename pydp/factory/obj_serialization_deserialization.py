class Serializer:
    def serialize(self, obj: dict) -> str:
        pass

    def deserialize(self, data: str) -> dict:
        pass


# Concrete serializer classes for different formats
class JSONSerializer(Serializer):
    def serialize(self, obj: dict) -> str:
        # Mock implementation for JSON serialization
        return f'JSON({obj})'

    def deserialize(self, data: str) -> dict:
        # Mock implementation for JSON deserialization
        return {'type': 'JSON', 'data': data}


class XMLSerializer(Serializer):
    def serialize(self, obj: dict) -> str:
        # Mock implementation for XML serialization
        return f'XML({obj})'

    def deserialize(self, data: str) -> dict:
        # Mock implementation for XML deserialization
        return {'type': 'XML', 'data': data}


# Serializer Factory to create specific serializers
class SerializerFactory:
    @staticmethod
    def create_serializer(format_type: str) -> Serializer:
        if format_type == 'JSON':
            return JSONSerializer()
        elif format_type == 'XML':
            return XMLSerializer()
        else:
            raise ValueError(f'Unknown format type: {format_type}')


# Usage
formats = ['JSON', 'XML']
obj = {'name': 'John', 'age': 30}
for format_type in formats:
    serializer = SerializerFactory.create_serializer(format_type)
    serialized_data = serializer.serialize(obj)
    print(f'Serialized ({format_type}):', serialized_data)
    deserialized_data = serializer.deserialize(serialized_data)
    print(f'Deserialized ({format_type}):', deserialized_data)
    print('---')
