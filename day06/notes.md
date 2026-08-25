# Day 6: The Python Object Model and Dynamic Typing

> **Theme:** Names point to objects, and objects have types.

## Learning Objective

By the end of this lesson, you should understand that:

- Every Python name is a reference to an object.
- Objects have types and identities.
- Python is dynamically typed, but it is still strongly typed.
- Mutable objects can change; immutable objects cannot.
- Aliasing, copying, and default arguments can affect program behavior.

This mental model explains many surprising Python behaviors.

## 1. Everything Is an Object

In Python, values such as integers, functions, classes, modules, lists, and strings are all objects. Every object has a type.

```python
x = 10

print(type(x))
# <class 'int'>
```

Even classes are objects. The type of the `int` class is `type`:

```python
print(type(int))
# <class 'type'>
```

### Beginner idea

A name is like a label. The label does not contain the object; it points to the object.

## 2. `id()`, `type()`, and `isinstance()`

| Tool | Purpose |
| --- | --- |
| `id(obj)` | Returns an identity number for an object during its lifetime |
| `type(obj)` | Shows the object's exact type |
| `isinstance(obj, Class)` | Checks whether an object belongs to a class or its inheritance hierarchy |

```python
x = 10

print(id(x))
print(type(x))
# <class 'int'>
print(isinstance(x, int))
# True
```

Use `isinstance()` when you want to ask whether a value can be treated as an instance of a particular class.

## 3. Dynamic Typing

Names are not permanently tied to one type. The object currently referenced by a name determines its type.

```python
x = 10
x = "hello"
x = [1, 2, 3]
```

The name `x` points to an integer first, then a string, and finally a list. Each object still has its own type.

### Reassignment versus mutation

**Reassignment** makes a name point to a different object:

```python
x = 10
x = 20
```

**Mutation** changes an existing mutable object:

```python
numbers = [1, 2]
numbers.append(3)

print(numbers)
# [1, 2, 3]
```

The list stayed the same object, but its contents changed.

## 4. Mutability

| Mutable objects | Immutable objects |
| --- | --- |
| `list` | `int` |
| `dict` | `str` |
| `set` | `tuple` |
|  | `frozenset` |

### Mutable objects

A mutable object can be changed after it is created.

```python
numbers = [1, 2]
numbers.append(3)
print(numbers)
# [1, 2, 3]
```

### Immutable objects

An immutable object cannot be changed after creation.

```python
x = 10
# The integer object 10 cannot be edited.
# Assigning x = 20 makes x point to a new integer object.
```

This distinction matters when several names refer to the same object.

## 5. References, Aliasing, and Copying

Python names reference objects. **Aliasing** happens when two names point to the same object.

```python
a = [1, 2]
b = a

b.append(3)

print(a)
# [1, 2, 3]
print(a is b)
# True
```

Because `a` and `b` refer to the same list, changing the list through `b` is visible through `a`.

### Shallow copy

`copy.copy()` creates a new outer object. Nested objects may still be shared.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
```

### Deep copy

`copy.deepcopy()` creates independent copies of nested objects too.

```python
deep = copy.deepcopy(original)
```

Use a deep copy when nested data must not be shared with the original.

## 6. `is` versus `==`

| Operator | Question it answers |
| --- | --- |
| `==` | Do these objects have equal values? |
| `is` | Are these references pointing to the same object? |

```python
a = [1, 2]
b = [1, 2]

print(a == b)
# True: the contents are equal
print(a is b)
# False: these are different list objects
```

### Important rule

Use `==` to compare ordinary values. Use `is` mainly for identity checks, especially `value is None`.

CPython commonly reuses small integers, often from `-5` to `256`:

```python
a = 100
b = 100

print(a is b)
# May be True in CPython, but do not rely on this.
```

Integer caching is an implementation detail, so it is not a reason to use `is` for number comparisons.

## 7. Python's Memory Model

Python primarily uses two cleanup mechanisms:

### Reference counting

Objects keep track of how many references point to them. When an object's reference count reaches zero, Python can clean it up.

### Cyclic garbage collector

Reference counting alone cannot clean up objects that refer to one another in a cycle. Python's cyclic garbage collector handles these cases.

You can inspect garbage-collector information with the `gc` module:

```python
import gc

print(gc.get_count())
```

The exact numbers depend on what the Python process has already done.

## 8. Exploring Objects in the REPL

The following tools are useful when learning or debugging:

### `dir()`

Shows the attributes and methods available on an object.

```python
x = [1, 2, 3]
print(dir(x))
```

### `help()`

Shows documentation for an object or class.

```python
help(list)
```

### `vars()`

Returns an object's `__dict__` when it has one.

```python
class User:
    name = "Ahmad"

print(vars(User))
```

### `__dict__`

Shows an object's stored namespace when the object provides one.

```python
class User:
    pass


user = User()
user.name = "Ahmad"

print(user.__dict__)
# {'name': 'Ahmad'}
```

## Agentic Mission

### 1. Demonstrate the Mutable Default Argument Bug

Default argument values are created once, when Python defines the function. A list used as a default is therefore shared between calls.

```python
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("Python"))
# ['Python']
print(add_item("Django"))
# ['Python', 'Django']
```

The second call reuses the list from the first call. This is usually surprising and is considered a bug when independent lists are expected.

### 2. Fix the Bug with `None`

Use `None` as a sentinel value. A new list is created inside the function for each call that does not provide `items`.

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now separate calls receive separate lists:

```python
print(add_item("Python"))
# ['Python']
print(add_item("Django"))
# ['Django']
```

### 3. Compare Shallow and Deep Copies

Use a nested list to see the difference:

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0].append(99)
print(original)
# [[1, 2, 99], [3, 4]]

deep[0].append(100)
print(original)
# [[1, 2, 99], [3, 4]]
```

The shallow copy shares the inner list with `original`; the deep copy does not.

## Validation Checklist

Your Day 6 tests should verify the following:

### Mutable default argument

Demonstrate that calls share state with the unsafe default-list version, then confirm the `None` version creates independent lists.

### Shallow versus deep copy

Confirm that:

- `copy.copy()` copies the outer object, but nested objects may be shared.
- `copy.deepcopy()` copies nested objects too.

### `id()` and aliasing

Confirm that two names point to the same object:

```python
a = []
b = a

assert id(a) == id(b)
assert a is b
```

### Assertions

Turn each demonstration into a test with `assert` statements. All assertions should pass.

## Day 6 Quick Revision

```text
Everything is an object
        ↓
Names reference objects
        ↓
Objects have types and identities
        ↓
Dynamic typing
        ↓
Mutable versus immutable objects
        ↓
Aliasing versus copying
        ↓
is versus ==
        ↓
Reference counting and garbage collection
        ↓
dir(), help(), vars(), and __dict__
        ↓
Mutable default argument bug
        ↓
None sentinel fix
        ↓
Shallow versus deep copy
```