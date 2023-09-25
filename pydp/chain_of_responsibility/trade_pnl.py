# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Handler Interface
class PnLHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # Returning handler for convenient chaining

    def handle_request(self, trades):
        pass

# Concrete Handler: FIFO
class FIFOPnLHandler(PnLHandler):
    def handle_request(self, trades):
        # Check if can handle with FIFO logic
        if self.can_handle(trades):
            # Calculate and return P&L
            pass
        elif self.next_handler:
            return self.next_handler.handle_request(trades)

    def can_handle(self, trades):
        # Check conditions for FIFO, e.g., trades sorted by date
        return True  # Simplified for this example

# Concrete Handler: LIFO
class LIFOPnLHandler(PnLHandler):
    def handle_request(self, trades):
        # Check if can handle with LIFO logic
        if self.can_handle(trades):
            # Calculate and return P&L
            pass
        elif self.next_handler:
            return self.next_handler.handle_request(trades)

    def can_handle(self, trades):
        # Check conditions for LIFO
        return True  # Simplified for this example

# Client Code
fifo_handler = FIFOPnLHandler()
lifo_handler = LIFOPnLHandler()

# Set up the chain
fifo_handler.set_next(lifo_handler)

# Example trades
trades = [Trade(100, 50, "2023-09-20"), Trade(-50, 55, "2023-09-25")]

# Starting the chain
result = fifo_handler.handle_request(trades)
print(result)
