import pulp

class MultiPeriodInventoryModel:
    def __init__(self, demand, holding_cost, order_cost, capacity):
        self.demand = demand
        self.holding_cost = holding_cost
        self.order_cost = order_cost
        self.capacity = capacity
        self.periods = len(demand)
        
        self.model = pulp.LpProblem("MultiPeriod_Inventory", pulp.LpMinimize)
        self.order_vars = {}
        self.inventory_vars = {}
        self.order_decision_vars = {}  # Binary variable to indicate if an order is made

    def _create_variables(self):
        for t in range(self.periods):
            self.order_vars[t] = pulp.LpVariable(f"order_{t}", 0)
            self.inventory_vars[t] = pulp.LpVariable(f"inventory_{t}", 0, self.capacity)
            self.order_decision_vars[t] = pulp.LpVariable(f"order_decision_{t}", 0, 1, pulp.LpBinary)

    def _set_objective_function(self):
        total_holding_cost = pulp.lpSum(self.holding_cost * self.inventory_vars[t] for t in range(self.periods))
        total_order_cost = pulp.lpSum(self.order_cost * self.order_decision_vars[t] for t in range(self.periods))
        
        self.model += total_holding_cost + total_order_cost

    def _set_constraints(self):
        for t in range(self.periods):
            if t == 0:
                self.model += self.order_vars[t] - self.demand[t] == self.inventory_vars[t]
            else:
                self.model += self.inventory_vars[t-1] + self.order_vars[t] - self.demand[t] == self.inventory_vars[t]
            
            # Link order decision to order amount
            self.model += self.order_vars[t] <= self.capacity * self.order_decision_vars[t]

    def solve(self):
        self._create_variables()
        self._set_objective_function()
        self._set_constraints()
        self.model.solve()

    def display_results(self):
        for t in range(self.periods):
            print(f"Period {t}: Order Amount: {self.order_vars[t].varValue}, End Inventory: {self.inventory_vars[t].varValue}")
        print(f"Total Cost: ${pulp.value(self.model.objective)}")

# Example Usage:

demand = [20, 30, 10, 40]
holding_cost = 2
order_cost = 100
capacity = 50

inventory_model = MultiPeriodInventoryModel(demand, holding_cost, order_cost, capacity)
inventory_model.solve()
inventory_model.display_results()
