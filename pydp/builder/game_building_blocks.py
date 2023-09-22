class GameObject:
    def __init__(self):
        self._properties = {}

    def set_property(self, key, value):
        self._properties[key] = value

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in self._properties.items())


class GameObjectBuilder:
    def __init__(self, object_type):
        self.game_object = GameObject()
        self.game_object.set_property('Type', object_type)

    def set_position(self, x, y):
        self.game_object.set_property('Position', (x, y))
        return self

    def set_size(self, width, height):
        self.game_object.set_property('Size', (width, height))
        return self

    def set_color(self, color):
        self.game_object.set_property('Color', color)
        return self

    def build(self):
        return self.game_object


# Usage
builder = GameObjectBuilder('Platform')
custom_game_object = (builder.set_position(10, 20)
                      .set_size(100, 20)
                      .set_color('Green')
                      .build())
print(custom_game_object)  # Outputs: Type: Platform, Position: (10, 20), Size: (100, 20), Color: Green
