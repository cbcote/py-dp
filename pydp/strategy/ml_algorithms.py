class MLStrategy:
    def train(self, data: list) -> str:
        pass


# Implement concrete strategies
class LinearRegression(MLStrategy):
    def train(self, data: list) -> str:
        # This is a mock implementation. In a real-world scenario, you'd use a library like scikit-learn.
        return 'Trained using Linear Regression'


class DecisionTree(MLStrategy):
    def train(self, data: list) -> str:
        # Mock implementation
        return 'Trained using Decision Tree'


class NeuralNetwork(MLStrategy):
    def train(self, data: list) -> str:
        # Mock implementation
        return 'Trained using Neural Network'


# Context class
class MLModel:
    def __init__(self, strategy: MLStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: MLStrategy):
        self._strategy = strategy

    def execute_training(self, data: list) -> str:
        return self._strategy.train(data)


# Usage
sample_data = [1, 2, 3, 4, 5]

# Using LinearRegression
model = MLModel(LinearRegression())
print(model.execute_training(sample_data))

# Switching to DecisionTree
model.set_strategy(DecisionTree())
print(model.execute_training(sample_data))

# Switching to NeuralNetwork
model.set_strategy(NeuralNetwork())
print(model.execute_training(sample_data))
