# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# State Interface
class PnLState:
    def calculate_realized_pnl(self, trades):
        pass

# Concrete State 1: FIFO
class FIFOPnLState(PnLState):
    def calculate_realized_pnl(self, trades):
        # Implement FIFO calculation logic
        pass

# Concrete State 2: LIFO
class LIFOPnLState(PnLState):
    def calculate_realized_pnl(self, trades):
        # Implement LIFO calculation logic
        pass

# Context Class: Inventory
class Inventory:
    """
    Delegates the work to the state object
    """
    def __init__(self):
        self._state = None  # Default state (can be set to a default P&L method if needed)
        self.trades = []

    def set_state(self, state):
        self._state = state

    def add_trade(self, trade):
        self.trades.append(trade)

    def calculate_realized_pnl(self):
        if self._state:
            return self._state.calculate_realized_pnl(self.trades)
        else:
            raise Exception("State not set")

# Client Code:
fifo_state = FIFOPnLState()
lifo_state = LIFOPnLState()

inventory = Inventory()

# Using FIFO
inventory.set_state(fifo_state)
inventory.add_trade(Trade(100, 50, "2023-09-20"))
inventory.add_trade(Trade(-50, 55, "2023-09-25"))
print(inventory.calculate_realized_pnl())

# Switching to LIFO
inventory.set_state(lifo_state)
print(inventory.calculate_realized_pnl())
