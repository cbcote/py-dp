class Computer:
    def __init__(self):
        self._components = {}

    def add_component(self, key, value):
        self._components[key] = value

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in self._components.items())


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.add_component('Processor', processor)
        return self

    def set_ram(self, ram):
        self.computer.add_component('RAM', ram)
        return self

    def set_storage(self, storage):
        self.computer.add_component('Storage', storage)
        return self

    def set_graphics_card(self, graphics_card):
        self.computer.add_component('Graphics Card', graphics_card)
        return self

    def build(self):
        return self.computer


# Usage
builder = ComputerBuilder()
custom_computer = (builder.set_processor('Intel i7')
                   .set_ram('16GB')
                   .set_storage('1TB SSD')
                   .set_graphics_card('NVIDIA RTX 3070')
                   .build())
print(custom_computer)  # Outputs: Processor: Intel i7, RAM: 16GB, Storage: 1TB SSD, Graphics Card: NVIDIA RTX 3070
