class Product:
    def display(self) -> str:
        pass


# Concrete product classes for different variants
class SmallRedShirt(Product):
    def display(self) -> str:
        return 'Small Red Shirt'


class MediumBluePants(Product):
    def display(self) -> str:
        return 'Medium Blue Pants'


class LargeGreenHat(Product):
    def display(self) -> str:
        return 'Large Green Hat'


# Product Factory to create specific product variants
class ProductFactory:
    @staticmethod
    def create_product(variant: str) -> Product:
        if variant == 'SmallRedShirt':
            return SmallRedShirt()
        elif variant == 'MediumBluePants':
            return MediumBluePants()
        elif variant == 'LargeGreenHat':
            return LargeGreenHat()
        else:
            raise ValueError(f'Unknown product variant: {variant}')


# Usage
variants = ['SmallRedShirt', 'MediumBluePants', 'LargeGreenHat']
for variant in variants:
    product = ProductFactory.create_product(variant)
    print(product.display())
