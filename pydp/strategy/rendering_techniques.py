class RenderingStrategy:
    def render(self, content: str) -> str:
        pass

# Implement concrete strategies
class VectorRendering(RenderingStrategy):
    def render(self, content: str) -> str:
        return f'Rendering "{content}" using Vector Rendering technique.'

class RasterRendering(RenderingStrategy):
    def render(self, content: str) -> str:
        return f'Rendering "{content}" using Raster Rendering technique.'

class RayTracingRendering(RenderingStrategy):
    def render(self, content: str) -> str:
        return f'Rendering "{content}" using Ray Tracing technique.'

# Context class
class Renderer:
    def __init__(self, strategy: RenderingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RenderingStrategy):
        self._strategy = strategy

    def execute_rendering(self, content: str) -> str:
        return self._strategy.render(content)


# Usage
content = '3D Model'

# Using VectorRendering
renderer = Renderer(VectorRendering())
print(renderer.execute_rendering(content))

# Switching to RasterRendering
renderer.set_strategy(RasterRendering())
print(renderer.execute_rendering(content))

# Switching to RayTracingRendering
renderer.set_strategy(RayTracingRendering())
print(renderer.execute_rendering(content))
