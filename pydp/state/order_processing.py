class OrderState:
    def process_order(self):
        pass

class Order:
    def __init__(self):
        self.state = OrderPending()

    def set_state(self, state):
        self.state = state

    def process(self):
        self.state.process_order()

class OrderPending(OrderState):
    def process_order(self):
        print("Processing pending order...")
        # Perform order processing logic
        self._change_state(OrderConfirmed())

    def _change_state(self, new_state):
        self.context.set_state(new_state)

class OrderConfirmed(OrderState):
    def process_order(self):
        print("Order is already confirmed. No further processing needed.")

class OrderShipped(OrderState):
    def process_order(self):
        print("Order has been shipped. Awaiting delivery.")

class OrderDelivered(OrderState):
    def process_order(self):
        print("Order has been delivered. Order processing complete.")

# Usage
order = Order()

# Processing a pending order
order.process()

# Attempting to process a confirmed order
order.set_state(OrderConfirmed())
order.process()

# Changing state to shipped and processing
order.set_state(OrderShipped())
order.process()

# Changing state to delivered and processing
order.set_state(OrderDelivered())
order.process()
