from itertools import chain, count, islice, groupby, product, starmap, accumulate, cycle, repeat

from pathlib import Path


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

print("First Chunk:")
print(next(chunks))
print("Second Chunk:")
print(next(chunks))

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

result = pipeline([1, 2, 3], double, add_ten, stringify)

print(list(result))

path = Path("day13/logs.txt")

def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line

a = read_lines(path)
print(next(a))
print(next(a))
print(next(a))
