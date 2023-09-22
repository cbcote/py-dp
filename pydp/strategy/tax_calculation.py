class TaxStrategy:
    def calculate_tax(self, amount: float) -> float:
        pass

# Implement concrete strategies
class VATStrategy(TaxStrategy):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.20  # 20% VAT

class SalesTaxStrategy(TaxStrategy):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.07  # 7% Sales Tax

class NoTaxStrategy(TaxStrategy):
    def calculate_tax(self, amount: float) -> float:
        return 0.0  # No tax

# Context class
class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TaxStrategy):
        self._strategy = strategy

    def execute_tax_calculation(self, amount: float) -> float:
        return self._strategy.calculate_tax(amount)


# Usage
amount = 100.0

# Using VATStrategy
calculator = TaxCalculator(VATStrategy())
print(f'Tax for ${amount} using VATStrategy: ${calculator.execute_tax_calculation(amount)}')

# Switching to SalesTaxStrategy
calculator.set_strategy(SalesTaxStrategy())
print(f'Tax for ${amount} using SalesTaxStrategy: ${calculator.execute_tax_calculation(amount)}')

# Switching to NoTaxStrategy
calculator.set_strategy(NoTaxStrategy())
print(f'Tax for ${amount} using NoTaxStrategy: ${calculator.execute_tax_calculation(amount)}')
