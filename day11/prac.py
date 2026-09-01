from abc import ABC, abstractmethod
import sys


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Vehicle.total_vehicles += 1

    def describe(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"

#Using classmethod, it works directly wit the class not the instance
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @staticmethod
    def is_valid_year(year):
        return year >= 1886

class Car(Vehicle):

    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def honk(self):
        return "beep beep"

    def describe(self):
        return super().describe() + f"\nDoors: {self.doors}"

# MRO and super() method

class A():
    def __init__(self):
        print("A")
        super().__init__()

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

class E(D, C):
    def __init__(self):
        print("E")
        super().__init__()

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Engine started"

class Electricar(Vehicle):
    def start(self):
        return "Electric motor started."

class VehicleDict:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        

class VehicleSlots:
    __slots__ = ("brand", "model", "year")

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        

v1 = VehicleDict("Toyota", "Corolla", 2023)
v2 = VehicleSlots("Honda", "City", 2023)     

print(v1.__dict__)
# print(v2.__dict__)

v1.color = "red"
try:
    v2.color = "red"
except:

    print("Vehicle object: ", sys.getsizeof(v1))
    print("Vehicle dict: ", sys.getsizeof(v1.__dict__))
    print("Vehicle slots object: ", sys.getsizeof(v2))

# car = Vehicle()

# car1 = Car()
# print(car1.start())

# car2 = Electricar()
# print(car2.start())

# d = E()

# print(E.__mro__)

# print(type(d))

# print(isinstance(d, A))

# class A:
#     def hello(self):
#         print("A")


# class B(A):
#     def hello(self):
#         print("B")
#         super().hello()


# class C(A):
#     def hello(self):
#         print("C")
#         super().hello()


# class D(B, C):
#     def hello(self):
#         print("D")
#         super().hello()

# d = D()

# d.hello()
# car = Car("Toyota", "Corolla", 2006, 4)

# print(car.describe())
# print(car.honk())
# print(car.doors)

# car1 = Vehicle("Toyota", "Corolla", 2000)

# print(car1.describe())

# car2 = Vehicle("Honda", "Civic", 2003)

# print(car2.describe())

# print(Vehicle.get_total_vehicles())

# print(Vehicle.is_valid_year(2026))

# print(Vehicle.is_valid_year(1800))

class User:
    def __init__(self, name, email, pwd):
        self.name = name
        self._email = email
        self.__pwd = pwd

    def show_info(self):
        return f"Name: {self.name}\nEmail: {self._email}"

user = User("Ali", "something@gmail.com", 1234)

print(user.show_info())


print(user.name)
print(user._email)
print(user._User__pwd)