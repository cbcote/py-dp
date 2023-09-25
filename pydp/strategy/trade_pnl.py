class Trade:
    """
    Represents a buy or sell transaction.
    """
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

class Inventory:
    """
    - Maintains list of trades
    - methods to add trades
    - calculates unit cost
    - calculates realized PnL
    """
    def __init__(self, pnl_calculator):
        self.trades = []
        self.pnl_calculator = pnl_calculator

    def add_trade(self, trade):
        self.trades.append(trade)

    def calculate_realized_pnl(self):
        return self.pnl_calculator.calculateRealizedPnL(self.trades)

    # Add method to calculate unit cost as needed

class PnLCalculator:
    def calculateRealizedPnL(self, trades):
        pass

class FIFOCalculator(PnLCalculator):
    def calculateRealizedPnL(self, trades):
        # Implement FIFO logic
        pass

class LIFOCalculator(PnLCalculator):
    def calculateRealizedPnL(self, trades):
        # Implement LIFO logic
        pass

# Client code
fifo_inventory = Inventory(FIFOCalculator())
fifo_inventory.add_trade(Trade(100, 50, "2023-09-20"))
fifo_inventory.add_trade(Trade(-50, 55, "2023-09-25"))
print(fifo_inventory.calculate_realized_pnl())

lifo_inventory = Inventory(LIFOCalculator())
lifo_inventory.add_trade(Trade(100, 50, "2023-09-20"))
lifo_inventory.add_trade(Trade(-50, 55, "2023-09-25"))
print(lifo_inventory.calculate_realized_pnl())
