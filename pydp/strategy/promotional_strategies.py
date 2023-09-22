class PromotionStrategy:
    def apply_discount(self, amount: float) -> float:
        pass

# Implement concrete strategies
class PercentageDiscount(PromotionStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount - (amount * self.percentage / 100)

class FixedDiscount(PromotionStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def apply_discount(self, amount: float) -> float:
        return amount - self.discount

class NoDiscount(PromotionStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount

# Context class
class Checkout:
    def __init__(self, strategy: PromotionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PromotionStrategy):
        self._strategy = strategy

    def finalize_order(self, amount: float) -> float:
        return self._strategy.apply_discount(amount)


# Usage
amount = 100.0

# Using PercentageDiscount
checkout = Checkout(PercentageDiscount(10))  # 10% discount
print(f'Final amount after applying PercentageDiscount: ${checkout.finalize_order(amount)}')

# Switching to FixedDiscount
checkout.set_strategy(FixedDiscount(15))  # $15 discount
print(f'Final amount after applying FixedDiscount: ${checkout.finalize_order(amount)}')

# Switching to NoDiscount
checkout.set_strategy(NoDiscount())
print(f'Final amount after applying NoDiscount: ${checkout.finalize_order(amount)}')
