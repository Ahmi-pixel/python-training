# Day 7: Python's Built-in Data Structures

> **Theme:** Choose a data structure based on how you need to store, find, and change data.

## Learning Objective

By the end of this lesson, you should be able to:

- Explain the difference between lists, tuples, sets, and dictionaries.
- Recognize the average time complexity of common operations.
- Choose a structure based on the access pattern your program needs.
- Use specialized structures from the `collections` module.
- Unpack lists and dictionaries clearly.

## The Four Main Structures

| Structure | Ordered? | Mutable? | Main purpose |
| --- | --- | --- | --- |
| `list` | Yes | Yes | Ordered items and index-based access |
| `tuple` | Yes | No | Fixed groups of related values |
| `set` | No guaranteed order | Yes | Unique values and fast membership checks |
| `dict` | Insertion order | Yes | Key-value lookups |

## 1. Lists

A list is a mutable, ordered collection. It is useful when you need to keep items in sequence and access them by index.

### Common operation complexity

| Operation | Average complexity | Why |
| --- | --- | --- |
| `append()` | $O(1)$ | Adds an item at the end |
| Index access | $O(1)$ | Jumps directly to an index |
| `insert()` | $O(n)$ | May move many existing items |
| Delete from the middle | $O(n)$ | May shift remaining items |

```python
numbers = [1, 2, 3]

numbers.append(4)
print(numbers[0])
# 1
```

### Beginner tip

Use a list when order matters or when you need index-based access. A list can contain duplicate values.

## 2. Slicing

Slicing extracts part of a sequence using this syntax:

```python
sequence[start:stop:step]
```

The `stop` position is not included.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[:3])
# [0, 1, 2]

print(numbers[3:])
# [3, 4, 5]

print(numbers[::-2])
# [5, 3, 1]
```

Important facts:

- Slicing creates a new list.
- Negative indices count from the end.

```python
print(numbers[-1])
# 5
```

## 3. Tuples

A tuple is an ordered, immutable sequence. Once created, its items cannot be changed, added, or removed.

```python
point = (10, 20)
```

A tuple is hashable when all of its elements are hashable. This means it can be used as a dictionary key or a set element:

```python
point = (10, 20)

locations = {
    point: "location",
}
```

### `namedtuple`

`namedtuple` provides tuple-like data with readable field names.

```python
from collections import namedtuple


User = namedtuple("User", ["name", "age"])
user = User("Ahmad", 22)

print(user.name)
# Ahmad
print(user.age)
# 22
```

## 4. Dictionaries

A dictionary stores data as key-value pairs. Modern Python dictionaries preserve insertion order.

```python
user = {
    "name": "Ahmad",
    "age": 22,
}

print(user["name"])
# Ahmad
```

### Common operation complexity

Dictionary lookup, insertion, and deletion are $O(1)$ on average because dictionaries use a hash table.

| Operation | Average complexity |
| --- | --- |
| Lookup | $O(1)$ |
| Insert | $O(1)$ |
| Delete | $O(1)$ |

### Useful dictionary methods

#### `.get()`

Safely retrieves a value. It returns `None`, or a supplied default, when the key does not exist.

```python
user.get("name")
user.get("email", "Not found")
```

#### `.setdefault()`

Returns an existing value. If the key is missing, it creates the key with the supplied default.

```python
data = {}

data.setdefault("users", [])
data["users"].append("Ahmad")
```

#### `.update()`

Adds or replaces several key-value pairs.

```python
user.update({
    "age": 23,
    "active": True,
})
```

#### `.items()`, `.keys()`, and `.values()`

These methods provide views of the dictionary's pairs, keys, and values.

```python
for key, value in user.items():
    print(key, value)

print(user.keys())
print(user.values())
```

## 5. Sets and `frozenset`

A set stores unique elements. It is useful for removing duplicates and checking membership quickly.

Membership testing is $O(1)$ on average:

```python
numbers = {1, 2, 3}

print(2 in numbers)
# True
```

### Set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
```

| Operator | Meaning |
| --- | --- |
| `a \| b` | Union: items in either set |
| `a & b` | Intersection: items in both sets |
| `a - b` | Difference: items in `a` but not `b` |

### `frozenset`

`frozenset` is an immutable set. It can be used where a normal set cannot, such as inside another set or as a dictionary key.

```python
numbers = frozenset([1, 2, 3])
```

## 6. The `collections` Module

The `collections` module provides specialized data structures for common problems.

### `deque`

`deque` means double-ended queue. It efficiently adds and removes items from both ends.

| Operation | Average complexity |
| --- | --- |
| `append()` | $O(1)$ |
| `appendleft()` | $O(1)$ |
| `pop()` | $O(1)$ |
| `popleft()` | $O(1)$ |

```python
from collections import deque


queue = deque()
queue.append("A")
queue.append("B")

print(queue.popleft())
# A
```

### `Counter`

`Counter` counts how often each item occurs.

```python
from collections import Counter


words = ["python", "django", "python"]
counts = Counter(words)

print(counts)
# Counter({'python': 2, 'django': 1})
```

### `defaultdict`

`defaultdict` creates a default value when a missing key is accessed. It is especially useful for grouping data and building graph adjacency lists.

```python
from collections import defaultdict


graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")
```

### `OrderedDict`

Normal dictionaries already preserve insertion order in modern Python. `OrderedDict` is mainly useful for its extra ordering operations or compatibility with older code.

## 7. Unpacking

Unpacking assigns the contents of a collection to several names.

### List unpacking

`*rest` collects all remaining values into a list.

```python
a, *rest = [1, 2, 3, 4]

print(a)
# 1
print(rest)
# [2, 3, 4]
```

### Dictionary unpacking

`**` expands a dictionary into keyword arguments for a function.

```python
def user(name, age):
    print(name, age)


data = {
    "name": "Ahmad",
    "age": 22,
}

user(**data)
# Ahmad 22
```

## Agentic Mission

### 1. Word Frequency Counter

Create a class using `Counter` that counts how many times each word appears.

```python
words = ["python", "django", "python"]

# python -> 2
# django -> 1
```

The class should handle:

- Empty input
- A single element
- Ties, where multiple words have the same count

### 2. Task Queue

Create a task queue using `deque`. It should support:

- Adding a task to the right
- Processing a task from the left
- Adding a task to the left
- Processing a task from the right

The important queue concept is **FIFO**: First In, First Out. `deque` makes operations at both ends efficient.

### 3. Graph Adjacency List

Use `defaultdict(list)` to represent relationships between nodes.

```python
from collections import defaultdict


graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")
graph["C"].append("D")
```

This represents:

```text
A -> B
A -> C
C -> D
```

The graph must handle disconnected nodes and self-loops:

```python
graph["A"].append("A")
```

## Validation Checklist

### `Counter`

Tests should verify:

- Empty input
- A single element
- Tied frequencies

### `deque`

Verify that the task queue correctly supports:

- FIFO processing
- `appendleft()`
- `pop()`

### Graph

Verify that the adjacency list supports:

- Disconnected nodes
- Self-loops

### Testing

All three mission classes should have `pytest` tests.

Target: **100% coverage**, with all tests passing.

## Day 7 Quick Revision

```text
list
-> ordered, mutable, O(1) index and append

tuple
-> ordered, immutable

dict
-> key-value data, O(1) average lookup

set
-> unique values, O(1) average membership

deque
-> efficient operations at both ends

Counter
-> frequency counting

defaultdict
-> automatic default values

namedtuple
-> tuple-like data with named fields
```
