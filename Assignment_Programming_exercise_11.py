# first one
"""
class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name, end="")


class Book(Publication):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_info(self):
        super().print_info()
        print(f" (author: {self.author}, {self.page} pages )")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print(f" (editor: {self.editor})")


publications = []
publications.append(Magazine("Akku Ankka", "Aki Hyyppa"))
publications.append(Book("Compartment No.9", "Roosa Liksom", 192))

for x in publications:
    x.print_info()
"""
# Second one
from Assignment_Programming_exercise_9 import Car


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, capacity):
        self.capacity = capacity  # Kw/hour
        super().__init__(reg_number, max_speed)


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, gas):
        self.gas = gas  # Litters
        super().__init__(reg_number, max_speed)


carElectric = ElectricCar("ABC123", 180, 52.5)
carGas = GasolineCar("CBA321", 165, 32.3)
carGas.accel(50)
carElectric.accel(50)
carGas.drive(3)
carElectric.drive(3)
print(f"car gas Drove {carGas.t_distance} and Electric car drove {carElectric.t_distance}")