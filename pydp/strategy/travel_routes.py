class RouteStrategy:
    def calculate_route(self, start: str, destination: str) -> str:
        pass

# Implement concrete strategies
class ShortestRoute(RouteStrategy):
    def calculate_route(self, start: str, destination: str) -> str:
        return f'Shortest route from {start} to {destination} calculated.'

class ScenicRoute(RouteStrategy):
    def calculate_route(self, start: str, destination: str) -> str:
        return f'Scenic route from {start} to {destination} calculated.'

class LeastTrafficRoute(RouteStrategy):
    def calculate_route(self, start: str, destination: str) -> str:
        return f'Route with least traffic from {start} to {destination} calculated.'

# Context class
class RoutePlanner:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def plan_route(self, start: str, destination: str) -> str:
        return self._strategy.calculate_route(start, destination)


# Usage
start_point = 'Point A'
destination_point = 'Point B'

# Using ShortestRoute
planner = RoutePlanner(ShortestRoute())
print(planner.plan_route(start_point, destination_point))

# Switching to ScenicRoute
planner.set_strategy(ScenicRoute())
print(planner.plan_route(start_point, destination_point))

# Switching to LeastTrafficRoute
planner.set_strategy(LeastTrafficRoute())
print(planner.plan_route(start_point, destination_point))
