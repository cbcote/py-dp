import pulp

class TransportationModel:
    def __init__(self, supply, demand, costs):
        self.supply = supply
        self.demand = demand
        self.costs = costs
        self.model = pulp.LpProblem("Transportation_Model", pulp.LpMinimize)
        self.variables = {}

    def _create_decision_variables(self):
        for factory in self.supply:
            self.variables[factory] = {}
            for warehouse in self.demand:
                self.variables[factory][warehouse] = pulp.LpVariable(f"x_{factory}_{warehouse}", 0)

    def _set_objective_function(self):
        self.model += pulp.lpSum(self.costs[factory][warehouse] * self.variables[factory][warehouse] 
                                 for factory in self.supply for warehouse in self.demand)

    def _set_constraints(self):
        for factory in self.supply:
            self.model += pulp.lpSum(self.variables[factory][warehouse] for warehouse in self.demand) == self.supply[factory], f"Supply_{factory}"

        for warehouse in self.demand:
            self.model += pulp.lpSum(self.variables[factory][warehouse] for factory in self.supply) == self.demand[warehouse], f"Demand_{warehouse}"

    def solve(self):
        self._create_decision_variables()
        self._set_objective_function()
        self._set_constraints()
        self.model.solve()

    def display_results(self):
        for factory in self.supply:
            for warehouse in self.demand:
                print(f"Amount transported from {factory} to {warehouse}: {self.variables[factory][warehouse].varValue}")
        print(f"Total Cost: ${pulp.value(self.model.objective)}")

supply = {'Factory1': 20, 'Factory2': 30}
demand = {'Warehouse1': 25, 'Warehouse2': 25}
costs = {
    'Factory1': {'Warehouse1': 8, 'Warehouse2': 6},
    'Factory2': {'Warehouse1': 10, 'Warehouse2': 4}
}

transportation = TransportationModel(supply, demand, costs)
transportation.solve()
transportation.display_results()
