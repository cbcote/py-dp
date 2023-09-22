class Car:
    def __init__(self):
        self._wheels = None
        self._color = None
        self._engine = None

    def __str__(self):
        return f'Car with {self._wheels} wheels, {self._color} color, and {self._engine} engine.'


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_wheels(self, wheels):
        self.car._wheels = wheels
        return self

    def set_color(self, color):
        self.car._color = color
        return self

    def set_engine(self, engine):
        self.car._engine = engine
        return self

    def build(self):
        return self.car


# Usage
builder = CarBuilder()
complex_car = (builder.set_wheels(4)
               .set_color('red')
               .set_engine('V8')
               .build())
print(complex_car)  # Outputs: Car with 4 wheels, red color, and V8 engine.
