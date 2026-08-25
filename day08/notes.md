# Day 8: Functions, Closures, and Higher-Order Functions

## Objective

Treat functions as first-class objects that close over their enclosing scope.

This is the foundation of:

- Decorators
- Callbacks
- Functional programming patterns

## Core Concepts

### 1. Function Objects

Python functions are objects and contain useful metadata.

#### `__name__`

A function's name.

```python
def add(x):
    return x + 1

print(add.__name__)
# add
```

#### `__doc__`

A function's documentation string.

```python
def add(x):
    """Add one to x."""
    return x + 1

print(add.__doc__)
```

#### `__annotations__`

Type annotations attached to the function.

```python
def add(x: int) -> int:
    return x + 1

print(add.__annotations__)
```

#### `__defaults__`

Default argument values.

```python
def greet(name="Ahmad"):
    pass

print(greet.__defaults__)
# ('Ahmad',)
```

#### `__code__`

Contains the function's compiled code information.

```python
print(add.__code__)
```

### 2. Function Signatures

A signature describes how a function accepts arguments.

#### Positional arguments

```python
def user(name, age):
    pass

user("Ahmad", 22)
```

#### Keyword arguments

```python
user(name="Ahmad", age=22)
```

#### `*args`

Collects extra positional arguments into a tuple.

```python
def test(*args):
    print(args)

test(1, 2, 3)
# (1, 2, 3)
```

#### `**kwargs`

Collects extra keyword arguments into a dictionary.

```python
def test(**kwargs):
    print(kwargs)

test(name="Ahmad", age=22)
# {'name': 'Ahmad', 'age': 22}
```

#### Keyword-only arguments

Everything after `*` must be passed by keyword.

```python
def user(name, *, age):
    pass

user("Ahmad", age=22)
```

#### Positional-only arguments

Everything before `/` must be passed positionally.

```python
def user(name, /, age):
    pass

user("Ahmad", 22)
```

### 3. LEGB Rule

When Python looks for a name, it searches in this order:

1. **Local**: inside the current function
2. **Enclosing**: inside an outer function
3. **Global**: at module level
4. **Built-in**: Python's built-in names, such as `len()`, `print()`, `sum()`, and `type()`

### 4. `global` and `nonlocal`

#### `global`

Use `global` when modifying a variable from the global scope.

```python
count = 0

def increase():
    global count
    count += 1
```

#### `nonlocal`

Use `nonlocal` when an inner function modifies a variable in an enclosing function.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

### 5. Closures

A closure is an inner function that remembers variables from its enclosing function.

```python
def multiplier(n):
    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)

print(double(5))
# 10
```

Even after `multiplier()` finishes, `multiply()` remembers `n`.

#### `__closure__`

You can inspect the captured values:

```python
print(double.__closure__)
print(double.__closure__[0].cell_contents)
# 2
```

### 6. Lambda

A lambda is an anonymous, single-expression function.

```python
triple = lambda x: x * 3

print(triple(5))
# 15
```

A lambda cannot contain normal statements or assignments.

### 7. `map()`

Applies a function to every item.

```python
numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)

print(list(result))
# [2, 4, 6]
```

### 8. `filter()`

Keeps items for which the function returns true.

```python
numbers = [5, 10, 15, 20]
result = filter(lambda x: x > 10, numbers)

print(list(result))
# [15, 20]
```

### 9. `functools.reduce()`

Repeatedly combines values into one result.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)

print(result)
# 10
```

### 10. `functools.partial`

Pre-fills some arguments of a function.

```python
from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)

print(square(5))
# 25
```

## Agentic Mission

### 1. Configurable Rate Limiter

Build a rate limiter using:

- Closures
- `nonlocal`
- Configurable `max_calls`
- Configurable `window`
- No classes

```python
limiter = rate_limiter(2, 3)

limiter()  # Allowed
limiter()  # Allowed
limiter()  # Blocked
```

After the configured window expires, the counter resets.

### 2. `compose(*fns)`

Build a utility that combines multiple functions using `functools.reduce`.

```python
def compose(*fns):
    def composed(x):
        return reduce(
            lambda x, fn: fn(x),
            fns,
            x,
        )

    return composed
```

This version applies functions from left to right.

For example:

```text
3 -> add_one -> 4 -> double -> 8 -> square -> 64
```

### 3. Partial-Application Pipeline

Use `partial()` to configure functions and then pass them through a pipeline.

```python
add_role = partial(
    add_field,
    key="role",
    value="developer",
)

set_active = partial(
    add_active,
    active=True,
)
```

```python
def pipeline(record, *steps):
    for step in steps:
        record = step(record)

    return record
```

Example:

```python
record = {"name": "Ahmad"}

result = pipeline(
    record,
    add_role,
    set_active,
    uppercase_name,
)
```

## Validation Metrics

### Rate limiter

The implementation must:

- Throttle calls after `max_calls`
- Reset after the configured window

### Compose

The implementation must correctly compose arbitrary functions according to its defined composition order.

For this implementation:

```python
compose(f, g, h)(x)
```

means:

```text
x -> f -> g -> h
```

### Closure inspection

Verify that `function.__closure__` contains the expected captured values.

```python
captured = [
    cell.cell_contents
    for cell in limiter.__closure__
]
```

### Pytest parametrization

`pytest.mark.parametrize(...)` runs the same test function multiple times with different input data. Each tuple provides values for the named parameters.

```python
import pytest


@pytest.mark.parametrize(
    "x, expected",
    [
        (1, 17),
        (2, 37),
        (3, 65),
        (5, 145),
    ],
)
def test_compose(x, expected):
    f = compose(add_one, double, square, add_one)

    assert f(x) == expected
```

## Final Day 8 Checklist

- [x] Functions as objects
- [x] Function attributes
- [x] Function signatures
- [x] `*args` and `**kwargs`
- [x] Keyword-only and positional-only arguments
- [x] LEGB rule
- [x] `global` and `nonlocal`
- [x] Closures
- [x] `__closure__` and `cell_contents`
- [x] Lambda
- [x] `map()`
- [x] `filter()`
- [x] `reduce()`
- [x] `partial()`
- [x] Higher-order functions
- [x] Rate limiter
- [x] `compose()`
- [x] Partial pipeline
- [x] Pytest parametrization
