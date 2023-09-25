from abc import ABC, abstractmethod
import random

# Command Interface
class MonteCarloCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class StockPriceCommand(MonteCarloCommand):
    
    def __init__(self, initial_price):
        self.price = initial_price

    def execute(self):
        # A simple random walk simulation
        return self.price * (1 + (random.random() - 0.5) * 0.02)

class PortfolioValuationCommand(MonteCarloCommand):

    def __init__(self, stocks):
        self.stocks = stocks

    def execute(self):
        return sum(stock.execute() for stock in self.stocks)

# Invoker
class SimulationInvoker:

    def __init__(self):
        self.commands = []

    def add_command(self, command: MonteCarloCommand):
        self.commands.append(command)

    def run_simulations(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results


# Client

# Initial stocks
apple = StockPriceCommand(150)
google = StockPriceCommand(2800)

# Portfolio valuation
portfolio = PortfolioValuationCommand([apple, google])

# Add simulations to the invoker
simulator = SimulationInvoker()
simulator.add_command(apple)
simulator.add_command(google)
simulator.add_command(portfolio)

# Run the simulations
results = simulator.run_simulations()
print(f"Apple Simulation Result: ${results[0]:.2f}")
print(f"Google Simulation Result: ${results[1]:.2f}")
print(f"Portfolio Valuation Result: ${results[2]:.2f}")
