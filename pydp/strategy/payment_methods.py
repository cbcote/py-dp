class PaymentStrategy:
    def pay(self, amount: float) -> str:
        pass

# Implement concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float) -> str:
        return f'Paid ${amount} using Credit Card: {self.card_number[-4:]}'

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount: float) -> str:
        return f'Paid ${amount} using PayPal: {self.email}'

# Context class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float) -> str:
        return self._strategy.pay(amount)


# Usage
processor = PaymentProcessor(CreditCardPayment('1234567812345678', '123'))
print(processor.process_payment(100.0))  # Outputs: Paid $100.0 using Credit Card: 5678

# Switching to PayPalPayment
processor.set_strategy(PayPalPayment('user@example.com'))
print(processor.process_payment(50.0))  # Outputs: Paid $50.0 using PayPal: user@example.com
