import copy
from collections import Counter

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# print(id(a))
# print(id(b))

def add_item(item, bucket=[]):

    bucket.append(item)
    return bucket

print(id(add_item("items")))
print(id(add_item("apple")))
print(id(add_item("bannana")))

x = [1, [2, 3], 4]

c = copy.copy(x)
d = copy.deepcopy(x)

print(x[0])
print(c[0])
print(d[0])
print(x[1])
print(c[1])
print(d[1])
c[1].append(9)
print(c)
d[1].append(5)
print(d)
# c[0].append(9)
# print(c)
# d[0].append(5)
# print(d)
print(x)

assert c[1] is x[1]
assert c[0] is x[0]
assert d[0] is x[0]
assert d[1] is not x[1]

a = 200

b = 200

print(a is b)

a = 200

b = 300

print(a is b)

words = ["apple", "apple", "bannana", "pear"]

count = Counter(words)

print(count.most_common(2))

person = {
    "name": "Ahmad",
    "age": 25,
    "city": "Lahore"
}

print(person.values())
print(person.help())






