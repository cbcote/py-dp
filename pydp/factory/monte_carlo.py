from abc import ABC, abstractmethod
import random

# Simulation Interface
class MonteCarloSimulation(ABC):

    @abstractmethod
    def run_simulation(self):
        pass

# Concrete Simulation
class StockPriceSimulation(MonteCarloSimulation):

    def run_simulation(self):
        # Simple random walk model
        price = 100
        for _ in range(10):
            price += price * (random.random() - 0.5) * 0.02
        return price


class WeatherSimulation(MonteCarloSimulation):

    def run_simulation(self):
        # Simple model: 0 for rain, 1 for sun
        return "Sunny" if random.random() > 0.3 else "Rainy"

# Simulation Factory 
class SimulationFactory:

    @staticmethod
    def create_simulation(simulation_type):
        if simulation_type == "stock":
            return StockPriceSimulation()
        elif simulation_type == "weather":
            return WeatherSimulation()
        else:
            raise ValueError(f"Unknown simulation type: {simulation_type}")

def main():
    # User or some part of the program specifies the type of simulation
    simulation_type = input("Enter type of simulation (stock/weather): ")

    # Factory creates the required simulation
    simulation = SimulationFactory.create_simulation(simulation_type)

    # Running the simulation
    result = simulation.run_simulation()
    print(f"Simulation result for {simulation_type}: {result}")

if __name__ == "__main__":
    main()
