from functools import total_ordering
from dataclasses import dataclass, field, InitVar
from typing import ClassVar

# @total_ordering
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"Name: {self.name}\nPrice: {self.price}"

#     def __str__(self):
#         return f"{self.name} costs {self.price}"

#     def __eq__(self, other):
#         return self.name == other.name and self.price == other.price

#     def __hash__(self):
#         return hash((self.name, self.price))

#     def __lt__(self, other):
#         return self.price < other.price
        

# p = Product("Bag", 2300)
# p2 = Product("Bag", 2300)
# p3 = Product("Shoes", 3000)

# print(p2 == p)
# print(p2 == p3)

# print(p)

# print(hash(p))

# print(p < p2)
# print(p < p3)
# print(p <= p2)
# print(p2 > p)
# print(repr(p))

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        result = self.value + other.value
        return Number(result)
    def __radd__(self, other):
        result = other + self.value
        return Number(result)
    def __iadd__(self, other):
        self.value = self.value + other.value
        return self
    def __mul__(self, other):
        result = self.value * other.value
        return Number(result)
class Collection:
    def __init__(self, items):
        self.items = items    
    def __len__(self):
        return len(self.items)
    def __getitem__(self, key):
        return self.items[key]
    def __setitem__(self, key, value):
        self.items[key] = value   
    def __contains__(self, item):
        return item in self.items
    def __iter__(self):
        return iter(self.items)
class MyContext:
    def __enter__(self):
        print("Entering")
    def __exit__(self, exc_type, exc, tb):
        print("Exiting")
        print(exc)
        print(exc_type)

class Descriptor:
    def __get__(self, instance, owner):
        print("Getting the value")
        return 42
    def __set__(self, instance, value):
        print("Setting the value")
        print(value)
    def __delete__(self, instance):
        print("Deleting value.")
class Product:
        def __init__(self, price):
            self._price = price

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, value):
            if value < 0:
                raise ValueError("Price cannot be negative.")
            self._price = value

@dataclass
class Product:
    name: str
    price: float

@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)

@dataclass
class User:
    username: str
    password: str = field(repr=False)

# @dataclass(frozen=True, order=True)
# class Product:
#     name: str
#     price: float
#     def __post_init__(self):
#         if self.price < 0:
#             raise ValueError("Price cannot be negative.")

@dataclass
class Product:
    name: str
    price: float
    category: ClassVar[str] = "Electonics"

@dataclass
class User:
    username: str
    password: InitVar[str]

    def __post_init__(self, password):
        print("Password Received.", password)

user = User("Ahmad", 1234)

print(user.username)
print(user.password)

# p = Product("Laptop", 1200)
# print(p)

# p1 = Product("Mobile", 3000)
# print(p1)

# print(Product.category)
# print(p.category)
# print(p)
# print(p>p1)
# print(p<p1)

# p1 = User("Ahmad", 1234)
# print(p1)


# order1 = Order("Ahmad")
# order2 = Order("Ali")

# order1.items.append("Laptop")

# print(order1.items)
# print(order2.items)

# p1 = Product("Bag", 2300)
# p2 = Product("Bag", 2300)

# print(p1)

# print(p1 == p2)


# p = Product(100)

# p.price = 200

# print(p.price)

# with MyContext():
#     print("Inside")
#     raise ValueError("Something went wrong.")

# c = Collection(["Python", "Django", "FastAPI"])
# for item in c:
#     print(item)
# c[1] = "Flask"
# print(c[1])
# print("Python" in c)
# print("Java" in c)
# print(len(c))
# print(c[2])
# print(c.items)

# a = Number(10)
# b = Number(5)

# result = a * b

# a = Number(10)
# b = Number(5)

# old_id = id(a)

# a += b

# print(a.value)
# print(type(a))
# print(id(a) == old_id)

# a = Number(10)
# b = Number(5)

# a += b

# print(a.value)
# print(type(a))
# a = Number(10)

# result = 5 + a

# print(result.value)
# print(type(result))   
# a = Number(2)

# b = Number(3)

# result = a + b

# print(result.value)
# print(type(result))
# print(a.value)
# print(b.value)

# food = "Pizzas"
# food = food.replace('z', 's')
# a = list(food)
# a[2] = 's'
# a[3] = 's'
# b = "".join(a)
# print(a)
# print(b)
# print(type(a))
