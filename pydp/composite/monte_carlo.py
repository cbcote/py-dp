from abc import ABC, abstractmethod
import random

# Component Interface
class FinancialComponent(ABC):

    @abstractmethod
    def simulate(self, iterations: int) -> float:
        pass

# Leaf Node
class Stock(FinancialComponent):

    def __init__(self, symbol: str, price: float):
        self._symbol = symbol
        self._price = price

    def simulate(self, iterations: int) -> float:
        # A simple random walk model for illustration
        simulated_price = self._price
        for _ in range(iterations):
            simulated_price += simulated_price * (random.random() - 0.5) * 0.02
        return simulated_price

# Composite Node
class InvestmentBundle(FinancialComponent):

    def __init__(self):
        self._components = []

    def add(self, component: FinancialComponent):
        self._components.append(component)

    def remove(self, component: FinancialComponent):
        self._components.remove(component)

    def simulate(self, iterations: int) -> float:
        return sum(component.simulate(iterations) for component in self._components)

# Client

# Individual stocks
apple = Stock("AAPL", 150)
google = Stock("GOOGL", 2800)
amazon = Stock("AMZN", 3400)

# Investment bundles
tech_bundle = InvestmentBundle()
tech_bundle.add(apple)
tech_bundle.add(google)

diverse_bundle = InvestmentBundle()
diverse_bundle.add(tech_bundle)
diverse_bundle.add(amazon)

# Simulating the value of individual stocks and bundles
print(f"Apple stock after simulation: ${apple.simulate(365):.2f}")
print(f"Tech bundle after simulation: ${tech_bundle.simulate(365):.2f}")
print(f"Diverse bundle after simulation: ${diverse_bundle.simulate(365):.2f}")
