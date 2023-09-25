from abc import ABC, abstractmethod
import random

class MonteCarloSimulation(ABC):

    # Template method
    def perform_simulation(self):
        self.initialize_simulation()
        results = self.run_simulation()
        self.post_process(results)

    @abstractmethod
    def initialize_simulation(self):
        pass

    @abstractmethod
    def run_simulation(self):
        pass

    @abstractmethod
    def post_process(self, results):
        pass


# Concrete subclasses
class StockSimulation(MonteCarloSimulation):

    def initialize_simulation(self):
        self.initial_price = 150  # Let's say for a stock like Apple

    def run_simulation(self):
        # A simple random walk model for stock price evolution
        return self.initial_price * (1 + (random.random() - 0.5) * 0.02)

    def post_process(self, result):
        print(f"Stock Simulation Result: ${result:.2f}")

class BondSimulation(MonteCarloSimulation):

    def initialize_simulation(self):
        self.initial_value = 1000  # Let's say for a bond

    def run_simulation(self):
        # A simple interest model for bond valuation
        return self.initial_value * (1 + 0.03)  # assuming 3% interest

    def post_process(self, result):
        print(f"Bond Simulation Result: ${result:.2f}")

# Client
stock_simulator = StockSimulation()
bond_simulator = BondSimulation()

stock_simulator.perform_simulation()  # This will follow the steps as per StockSimulation
bond_simulator.perform_simulation()   # This will follow the steps as per BondSimulation
