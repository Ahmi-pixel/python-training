from abc import ABC, abstractmethod
import sys


class Vehicle(ABC):
    def __init__(self, brand, model, year, **kwargs):
        self.brand = brand
        self.model = model
        self.year =year
        super().__init__(**kwargs)

    @abstractmethod
    def start(self):
        pass

    def describe(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"

class Chargablemixin:

    def __init__(self, battery, **kwargs):
        self.battery = battery
        super().__init__(**kwargs)

    def charge(self):
        return f"Charging: {self.battery} kwH Battery." 

class ElectricCar(Vehicle, Chargablemixin):
    def __init__(self, brand, model, year, battery):
        super().__init__(brand=brand, model=model, year=year, battery=battery)

    def start(self):
        return "Electric car started."
class Car(Vehicle):

    def start(self):
        return "Car started."

car1= Car("Honda", "City", 2022)
print(car1.start())
print(car1.describe())

car = ElectricCar("Tesla", "Cybertruck", 2025, 96)

print(car.describe())
print(car.start())
print(car.charge())

print(ElectricCar.__mro__)

class NormalVehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class SlottedVehicle:

    __slots__ = ("brand", "model", "year")

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

normal = NormalVehicle("Toyota", "Corolla", 2025)
slotted = SlottedVehicle("Toyota", "Corolla", 2025)

print("Normal object:", sys.getsizeof(normal))
print("Normal __dict__:", sys.getsizeof(normal.__dict__))

print("Slotted object:", sys.getsizeof(slotted))
