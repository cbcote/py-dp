# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Abstract class defining the template method
class PnLCalculator:
    def calculate_realized_pnl(self, trades):
        selected_trades = self.select_trades(trades)
        return self.compute_pnl(selected_trades)

    # Abstract methods to be overridden by concrete classes
    def select_trades(self, trades):
        pass

    def compute_pnl(self, selected_trades):
        pass

# Concrete class for FIFO
class FIFOCalculator(PnLCalculator):
    def select_trades(self, trades):
        # Sort trades based on date and select them
        sorted_trades = sorted(trades, key=lambda x: x.date)
        return sorted_trades

    def compute_pnl(self, selected_trades):
        # Calculate P&L based on FIFO logic
        pass

# Concrete class for LIFO
class LIFOCalculator(PnLCalculator):
    def select_trades(self, trades):
        # Sort trades based on date in reverse and select them
        sorted_trades = sorted(trades, key=lambda x: x.date, reverse=True)
        return sorted_trades

    def compute_pnl(self, selected_trades):
        # Calculate P&L based on LIFO logic
        pass

# Inventory class that uses a PnLCalculator
class Inventory:
    def __init__(self, calculator):
        self.trades = []
        self.calculator = calculator

    def add_trade(self, trade):
        self.trades.append(trade)

    def calculate_realized_pnl(self):
        return self.calculator.calculate_realized_pnl(self.trades)

# Client Code
fifo_calculator = FIFOCalculator()
lifo_calculator = LIFOCalculator()

inventory = Inventory(fifo_calculator)  # Initialize with FIFO
inventory.add_trade(Trade(100, 50, "2023-09-20"))
inventory.add_trade(Trade(-50, 55, "2023-09-25"))
print(inventory.calculate_realized_pnl())

inventory = Inventory(lifo_calculator)  # Initialize with LIFO
inventory.add_trade(Trade(100, 50, "2023-09-20"))
inventory.add_trade(Trade(-50, 55, "2023-09-25"))
print(inventory.calculate_realized_pnl())
