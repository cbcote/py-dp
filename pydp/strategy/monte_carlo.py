from abc import ABC, abstractmethod
import random
import numpy as np

# Strategy Interface
class RandomNumberGeneratorStrategy(ABC):

    @abstractmethod
    def generate_point(self) -> tuple:
        pass

# Concrete Strategy
class DefaultRandomNumberGenerator(RandomNumberGeneratorStrategy):
    
    def generate_point(self) -> tuple:
        return (random.random(), random.random())

class NumpyRandomNumberGenerator(RandomNumberGeneratorStrategy):
    
    def generate_point(self) -> tuple:
        return tuple(np.random.rand(2))

# Context
class PiEstimator:

    def __init__(self, generator_strategy: RandomNumberGeneratorStrategy, iterations: int):
        self.generator_strategy = generator_strategy
        self.iterations = iterations

    def estimate(self):
        inside_circle = 0

        for _ in range(self.iterations):
            x, y = self.generator_strategy.generate_point()
            if x*x + y*y <= 1:  # Check if point is inside the unit circle
                inside_circle += 1
        
        # Calculate and return the estimate for π
        return 4 * inside_circle / self.iterations

# Client
iterations = 100000

estimator_default_random = PiEstimator(DefaultRandomNumberGenerator(), iterations)
print(f"Estimation using Default Random: {estimator_default_random.estimate()}")

estimator_numpy_random = PiEstimator(NumpyRandomNumberGenerator(), iterations)
print(f"Estimation using Numpy Random: {estimator_numpy_random.estimate()}")
