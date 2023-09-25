# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Abstract P&L Calculator
class PnLCalculator:
    def calculate(self, trades):
        pass

# Concrete P&L Calculator: FIFO
class FIFOCalculator(PnLCalculator):
    def calculate(self, trades):
        # Implement FIFO P&L calculation logic here
        return "FIFO P&L calculated"

# Concrete P&L Calculator: LIFO
class LIFOCalculator(PnLCalculator):
    def calculate(self, trades):
        # Implement LIFO P&L calculation logic here
        return "LIFO P&L calculated"

# P&L Calculator Factory
class PnLCalculatorFactory:
    @staticmethod
    def create_calculator(method):
        if method == "FIFO":
            return FIFOCalculator()
        elif method == "LIFO":
            return LIFOCalculator()
        else:
            raise ValueError(f"Unknown method: {method}")

# Client Code
trades = [Trade(100, 50, "2023-09-20"), Trade(-50, 55, "2023-09-25")]

calculator = PnLCalculatorFactory.create_calculator("FIFO")
print(calculator.calculate(trades))  # Executes FIFO P&L Calculation

calculator = PnLCalculatorFactory.create_calculator("LIFO")
print(calculator.calculate(trades))  # Executes LIFO P&L Calculation
