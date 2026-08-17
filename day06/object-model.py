import copy


# ============================================================
# 1. Mutable Default Argument — The Bug
# ============================================================

def add_item_bug(item, items=[]):
    items.append(item)
    return items


first = add_item_bug("A")
second = add_item_bug("B")

print("Mutable Default Argument Bug:")
print("first :", first)
print("second:", second)

# Both names point to the same list
assert first is second
assert first == ["A", "B"]
assert second == ["A", "B"]


# ============================================================
# 2. Mutable Default Argument — The Fix
# ============================================================

def add_item_fixed(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


first = add_item_fixed("A")
second = add_item_fixed("B")

print("\nNone Sentinel Fix:")
print("first :", first)
print("second:", second)

# Each call creates a separate list
assert first is not second
assert first == ["A"]
assert second == ["B"]


# ============================================================
# 3. Shallow Copy vs Deep Copy
# ============================================================

original = [["A", "B"], ["C", "D"]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# The outer lists are different
assert original is not shallow
assert original is not deep

# Shallow copy shares the inner lists
assert original[0] is shallow[0]

# Deep copy creates new inner lists
assert original[0] is not deep[0]

# Demonstrate the difference
shallow[0].append("X")
deep[1].append("Y")

print("\nShallow vs Deep Copy:")
print("original:", original)
print("shallow :", shallow)
print("deep    :", deep)

# Shallow copy changed the original's inner list
assert original == [["A", "B", "X"], ["C", "D"]]
assert shallow == [["A", "B", "X"], ["C", "D"]]

# Deep copy did NOT change the original
assert deep == [["A", "B"], ["C", "D", "Y"]]


print("\nAll Day 6 assertions passed!")