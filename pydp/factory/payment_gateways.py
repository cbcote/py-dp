class PaymentGateway:
    def process_payment(self, amount: float) -> str:
        pass


# Concrete payment gateway classes for different providers
class PayPalGateway(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f'Processed payment of ${amount} using PayPal'


class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f'Processed payment of ${amount} using Stripe'


class CreditCardGateway(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f'Processed payment of ${amount} using Credit Card'


# Payment Factory to create specific payment gateways
class PaymentFactory:
    @staticmethod
    def create_gateway(gateway_type: str) -> PaymentGateway:
        if gateway_type == 'PayPal':
            return PayPalGateway()
        elif gateway_type == 'Stripe':
            return StripeGateway()
        elif gateway_type == 'CreditCard':
            return CreditCardGateway()
        else:
            raise ValueError(f'Unknown gateway type: {gateway_type}')


# Usage
gateway_types = ['PayPal', 'Stripe', 'CreditCard']
amount = 100.0
for gateway_type in gateway_types:
    gateway = PaymentFactory.create_gateway(gateway_type)
    print(gateway.process_payment(amount))
