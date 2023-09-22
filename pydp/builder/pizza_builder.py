class Pizza:
    def __init__(self):
        self._size = None
        self._cheese = False
        self._pepperoni = False
        self._mushrooms = False

    def __str__(self):
        toppings = [name for name, value in vars(self).items() if value and name != '_size']
        return f'{self._size} inch Pizza with {", ".join(toppings)}.'


class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza()
        self.pizza._size = size

    def add_cheese(self):
        self.pizza._cheese = True
        return self

    def add_pepperoni(self):
        self.pizza._pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza._mushrooms = True
        return self

    def build(self):
        return self.pizza


# Usage
builder = PizzaBuilder(12)
custom_pizza = (builder.add_cheese()
                .add_pepperoni()
                .build())
print(custom_pizza)  # Outputs: 12 inch Pizza with _cheese, _pepperoni.
