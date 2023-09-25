# Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Base Component Interface
class PnLCalculator:
    def calculate(self, trades):
        pass

# Concrete Component: FIFO Calculator
class FIFOCalculator(PnLCalculator):
    def calculate(self, trades):
        # Implement FIFO P&L calculation
        return "FIFO P&L calculated"

# Concrete Component: LIFO Calculator
class LIFOCalculator(PnLCalculator):
    def calculate(self, trades):
        # Implement LIFO P&L calculation
        return "LIFO P&L calculated"

# Base Decorator Class
class PnLDecorator(PnLCalculator):
    def __init__(self, calculator):
        self._calculator = calculator

    def calculate(self, trades):
        return self._calculator.calculate(trades)

# Concrete Decorator: Transaction Fee Adjuster
class TransactionFeeDecorator(PnLDecorator):
    def calculate(self, trades):
        base_result = super().calculate(trades)
        # Adjust base result for transaction fees
        return f"{base_result} with transaction fees adjusted"

# Concrete Decorator: Tax Adjuster
class TaxDecorator(PnLDecorator):
    def calculate(self, trades):
        base_result = super().calculate(trades)
        # Adjust base result for taxes
        return f"{base_result} with tax implications considered"

# Client Code
trades = [Trade(100, 50, "2023-09-20"), Trade(-50, 55, "2023-09-25")]

# Simple FIFO P&L Calculation
fifo_calculator = FIFOCalculator()
print(fifo_calculator.calculate(trades))

# FIFO P&L Calculation with Transaction Fees adjusted
fifo_with_fees = TransactionFeeDecorator(fifo_calculator)
print(fifo_with_fees.calculate(trades))

# FIFO P&L Calculation with Transaction Fees and Tax Implications adjusted
fifo_with_fees_and_tax = TaxDecorator(fifo_with_fees)
print(fifo_with_fees_and_tax.calculate(trades))
