# Existing Trade Class
class Trade:
    def __init__(self, quantity, price, date):
        self.quantity = quantity
        self.price = price
        self.date = date

# Third-party Trade Data (just a different format for the sake of the example)
class ThirdPartyTrade:
    def __init__(self, volume, value, timestamp):
        self.volume = volume
        self.value = value
        self.timestamp = timestamp

# Adapter for Third-party Trade Data
class TradeAdapter(Trade):
    def __init__(self, third_party_trade):
        # Convert third party trade data format to the one our system uses
        super().__init__(third_party_trade.volume, third_party_trade.value, third_party_trade.timestamp)

# P&L Calculator (expects a list of our Trade objects)
class PnLCalculator:
    def calculate(self, trades):
        # Dummy implementation for simplicity
        return "P&L calculated for given trades"

# Client Code
third_party_trades = [ThirdPartyTrade(100, 50, "2023-09-20"), ThirdPartyTrade(-50, 55, "2023-09-25")]

# Convert third party trades to the format our P&L calculator expects using the adapter
adapted_trades = [TradeAdapter(t) for t in third_party_trades]

calculator = PnLCalculator()
print(calculator.calculate(adapted_trades))
