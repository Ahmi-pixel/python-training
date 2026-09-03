from dataclasses import dataclass

class Matrix:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        result = len(self.data)
        return result

    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return iter(self.data)
    
    def __add__(self, other):
        result = []
        for index, row in enumerate(self.data):
            new_row = []
            for index_e, element in enumerate(row):
                new_row.append(other.data[index][index_e] + self.data[index][index_e])
            result.append(new_row)
        return Matrix(result)
    
    def __mul__(self, other):
        result = []
        for index, row in enumerate(self.data):
            new_row = []
            for index_e, element in enumerate(row):
                new_row.append(other.data[index][index_e] * self.data[index][index_e])
            result.append(new_row)
        return Matrix(result)

@dataclass(frozen=True)
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Cannot add negative number to price")

product = Product("Laptop", 1200)
# product1 = Product("Laptop", -1)
print(product)
print(hash(product))

a = Matrix([
    [1, 2],
    [3, 4]
])

b = Matrix([
    [5, 6],
    [7, 8]
])

added = a + b
multiplied = a * b

print("Addition:", added.data)
print("Multiplication:", multiplied.data)

print("A:", a.data)
print("B:", b.data)
