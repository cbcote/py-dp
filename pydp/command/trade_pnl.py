# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Command Interface
class PnLCommand:
    def execute(self, trades):
        pass

# Concrete Command: FIFO Calculator
class FIFOPnLCommand(PnLCommand):
    def execute(self, trades):
        # Implement FIFO P&L calculation logic here
        return "FIFO P&L calculated"

# Concrete Command: LIFO Calculator
class LIFOPnLCommand(PnLCommand):
    def execute(self, trades):
        # Implement LIFO P&L calculation logic here
        return "LIFO P&L calculated"

# Invoker Class
class PnLCalculatorInvoker:
    def __init__(self, command):
        self._command = command

    def set_command(self, command):
        self._command = command

    def calculate(self, trades):
        return self._command.execute(trades)

# Client Code
trades = [Trade(100, 50, "2023-09-20"), Trade(-50, 55, "2023-09-25")]

fifo_command = FIFOPnLCommand()
lifo_command = LIFOPnLCommand()

calculator = PnLCalculatorInvoker(fifo_command)
print(calculator.calculate(trades))  # Executes FIFO P&L Calculation

calculator.set_command(lifo_command)
print(calculator.calculate(trades))  # Executes LIFO P&L Calculation
