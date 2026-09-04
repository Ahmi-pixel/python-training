from itertools import chain, count, islice, groupby, product, starmap, accumulate, cycle, repeat
from collections import defaultdict
from pathlib import Path

class Counter:
    def __init__(self, maximum):
        self.current = 0
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.maximum:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

def multiply(a, b):
    return a * b

def first():
    yield 1
    yield 2

def second():
    yield 3
    yield 4

def combined():
    yield from first()
    yield from second()

def greeter():
    name = yield "What is your name?"
    yield f"Hello, {name}!"

def worker():
    try:
        while True:
            yield "working..."
    finally:
        print("Worker cleaned up")

def worker():
    try:
        while True:
            yield "working..."
    except ValueError:
        yield "Error received!"

def calculate_total(price, quantity):
    return price * quantity
    

orders = [
    (1000, 2),
    (500, 3),
    (2500, 1),
    (750, 4),
]

# a = starmap(calculate_total, orders)
# b = accumulate(a)
# print(list(b))

workers = ["worker-A", "worker-B", "worker-C"]

jobs = ["job-1", "job-2", "job-3", "job-4"]

# a = repeat("High")
# b = zip(jobs, a)
# print(list(b))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# a = cycle(workers)
# for n in range(1,11):
#     print("Job",n, next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



data = [
    ("Ali", "A"),
    ("Ahmed", "A"),
    ("Sara", "B"),
    ("Fatima", "B"),
]

orders = [
    ("Ali", "Laptop"),
    ("Ahmed", "Monitor"),
    ("Ali", "Mouse"),
    ("Ahmed", "Keyboard"),
]

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]
storage = ["128GB", "256GB"]

methods = ["GET", "POST", "DELETE"]
auth = ["authenticated", "unauthenticated"]
status = [200, 400, 500]

endpoints = ["/users", "/orders"]
methods = ["GET", "POST"]
auth = ["valid", "invalid"]

values = [
    (2, 3),
    (4, 5),
    (10, 2),
]


# a = starmap(multiply, values)
# print(list(a))



# test_cases = []
# for item in product(endpoints, methods, auth):
#     test_cases.append(item)
# print(test_cases)
# a = {}
# for endpoint, method, auth in test_cases:
#     a.update({"endpoints": endpoint, "method": method, "auth": auth})
# print(a)
# a = []
# for method, auth_type, expected_status in test_cases:
#     a.append(f"Test: {method} | {auth_type} | {expected_status}")
# print(a)
# print(configurations)
# print(len(configurations))



# a = sorted(orders, key=lambda x: x[0])

# for key, group in groupby(a, key=lambda x: x[0]):
#     print(key, list(group))

# print(orders)
# print(a)

# numbers = count(1)

# ten = islice(numbers, 10)
# print(list(ten))

# a = ["Ali", "Ahmad"]
# b = ["Fatima", "Sara"]

# for value in chain(a, b):
#     print(value)

# w = worker()
# print(next(w))
# print(w.throw(ValueError("Something went wrong.")))

# w = worker()
# print(next(w))
# print(w.close())

# g = greeter()
# print(next(g))
# print((g.send("Ahmad")))

# print(list(combined()))

# a = (n * 2 for n in range(5))

# for number in a:
#     print(number)

# max = int(input("Enter max number: "))
# counter = Counter(max)
# for n in counter:
#     print(n)

# counter = Counter(3)

# iterator = iter(counter)

# print(iterator is counter)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# values = iter(input, "stop")

# for value in values:
#     print("You entered:", value)

def source():
    for number in range(10):
        print("Producing:", number)
        yield number

def chunked(iterable, size):
    iterator = iter(iterable)

    while True:
        chunk = list(islice(iterator, size))

        if not chunk:
            return

        yield chunk

chunks = chunked(source(), 3)

# print("First Chunk:")
# print(next(chunks))
# print("Second Chunk:")
# print(next(chunks))

def double(numbers):
    for number in numbers:
        yield number * 2

def add_ten(numbers):
    for number in numbers:
        yield number + 10

def stringify(numbers):
    for number in numbers:
        yield str(number)

def pipeline(source, *stages):
    current = source
    for stage in stages:
        current = stage(current)
    yield from current

# result = pipeline([1, 2, 3], double, add_ten, stringify)

# print(list(result))

path = Path("day13/logs.txt")

def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line

a = read_lines(path)
print(next(a))
print(next(a))
print(next(a))



