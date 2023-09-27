import pulp

class BlendingModelBase:
    def __init__(self):
        self.model = pulp.LpProblem("Blending_Problem", pulp.LpMinimize)
        self.variables = {}
    
    def create_variable(self, name):
        return pulp.LpVariable(name, lowBound=0, cat='Continuous')

    def set_objective(self, costs):
        self.model += pulp.lpSum(costs), "Total Cost"

    def solve(self):
        self.prepare_model()
        self.model.solve()

    def display_results(self, vars_to_display):
        for var_name, variable in vars_to_display:
            print(f"Optimal amount of {var_name}: {variable.varValue} grams")
        print(f"Total Cost: ${pulp.value(self.model.objective)}")

    def prepare_model(self):
        # This is an abstract method meant to be implemented by the subclasses
        pass


class SingleProductBlendingModel(BlendingModelBase):
    def __init__(self, raw_materials, requirements):
        super().__init__()
        self.raw_materials = raw_materials
        self.requirements = requirements

    def create_variables(self):
        for material in self.raw_materials.keys():
            self.variables[material] = self.create_variable(material)

    def add_constraints(self):
        for nutrient, value in self.requirements.items():
            self.model += pulp.lpSum([self.raw_materials[material][nutrient] * self.variables[material] 
                                      for material in self.raw_materials]) >= value, f"{nutrient} Requirement"

    def prepare_model(self):
        self.create_variables()
        self.set_objective([self.raw_materials[material]['cost'] * self.variables[material] for material in self.raw_materials])
        self.add_constraints()


class MultiProductBlendingModel(BlendingModelBase):
    def __init__(self, raw_materials, products):
        super().__init__()
        self.raw_materials = raw_materials
        self.products = products

    def create_variables(self):
        for product_name in self.products:
            self.variables[product_name] = {material: self.create_variable(f"{product_name}_{material}") for material in self.raw_materials.keys()}

    def add_constraints(self):
        for product_name, product_data in self.products.items():
            for nutrient, value in product_data['requirements'].items():
                self.model += pulp.lpSum([self.raw_materials[material][nutrient] * self.variables[product_name][material] 
                                          for material in self.raw_materials]) >= value, f"{product_name} {nutrient} Requirement"

    def prepare_model(self):
        self.create_variables()
        self.set_objective([self.raw_materials[material]['cost'] * var 
                            for product_vars in self.variables.values() 
                            for material, var in product_vars.items()])
        self.add_constraints()



# Data
raw_materials = {
    'Chicken': {'cost': 0.008, 'protein': 0.1, 'fat': 0.08},
    'Beef': {'cost': 0.005, 'protein': 0.2, 'fat': 0.1}
}

products = {
    'Dog Food': {
        'requirements': {'protein': 8, 'fat': 6}
    },
    'Cat Food': {
        'requirements': {'protein': 10, 'fat': 5}
    }
}

# Using the class
blend = MultiProductBlendingModel(raw_materials, products)
blend.solve()
blend.display_results()
