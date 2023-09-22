class Meal:
    def __init__(self):
        self._courses = {}

    def add_course(self, course_name, dish):
        self._courses[course_name] = dish

    def __str__(self):
        return ', '.join(f'{course}: {dish}' for course, dish in self._courses.items())


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def set_starter(self, starter):
        self.meal.add_course('Starter', starter)
        return self

    def set_main_course(self, main_course):
        self.meal.add_course('Main Course', main_course)
        return self

    def set_dessert(self, dessert):
        self.meal.add_course('Dessert', dessert)
        return self

    def set_drink(self, drink):
        self.meal.add_course('Drink', drink)
        return self

    def build(self):
        return self.meal


# Usage
builder = MealBuilder()
custom_meal = (builder.set_starter('Soup')
               .set_main_course('Steak')
               .set_dessert('Ice Cream')
               .set_drink('Wine')
               .build())
print(custom_meal)  # Outputs: Starter: Soup, Main Course: Steak, Dessert: Ice Cream, Drink: Wine
