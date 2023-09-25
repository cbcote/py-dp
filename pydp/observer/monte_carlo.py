from abc import ABC, abstractmethod
import random

class Observer(ABC):
    
    @abstractmethod
    def update(self, inside_circle: int, total: int):
        pass

class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class PiEstimation(Subject):

    def __init__(self, iterations):
        self._iterations = iterations
        self._inside_circle = 0
        self._observers = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._inside_circle, self._iterations)

    def estimate(self):
        for _ in range(self._iterations):
            x, y = random.random(), random.random()
            if x*x + y*y <= 1:
                self._inside_circle += 1
            # Notify observers for each iteration
            self.notify_observers()


class ConsoleLogger(Observer):

    def update(self, inside_circle: int, total: int):
        pi_estimate = 4 * inside_circle / total
        print(f"Current π estimation after {total} iterations: {pi_estimate:.5f}")

class Analytics(Observer):

    def update(self, inside_circle: int, total: int):
        if total % 1000 == 0:  # For every 1000 iterations
            accuracy = abs((3.14159 - 4 * inside_circle / total) / 3.14159) * 100
            print(f"Accuracy after {total} iterations: {accuracy:.2f}%")


pi_estimator = PiEstimation(5000)

console_logger = ConsoleLogger()
analytics = Analytics()

pi_estimator.register_observer(console_logger)
pi_estimator.register_observer(analytics)

pi_estimator.estimate()
