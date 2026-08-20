# ==========================================
# 4. SETS
# ==========================================

s = {1, 2, 3, 4, 4, 5}

print(s)

print(type(s))

#list
l = [1, 2, 2, 3, 3, 4, 5, 5]

print(l)

print(type(l))

#turning from list to set
numbers = set(l)

print(numbers)

print(type(numbers))

#adding in sets
numbers.add(10)

numbers.add(10)

print(numbers)

#removing in sets
numbers.remove(10)

#this wouldn't produce a keyerror if the number isn't present
numbers.discard(100)

print(numbers)

#O(1)
print(3 in numbers)

#O(n)
print(100 in numbers)

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

#this will print union
print(A | B)

#this will print intersection
print(A & B)

#this will print all values of a minus b
print(A - B)

#this will print all values of b minus a
print(B - A)

#making an empty set
empty = set( )

print(empty)

print(type(empty))

#making a frozenset
s2 = frozenset([1, 2, 3, 4, 4, 4, 5])

print(s2)

#s2.add(6), frozensets are immutable
