# ==========================================
# 2. TUPLES
# ==========================================

from collections import namedtuple

point = ("Ahmad", 25, "Python", "Pakistan")

print("Tuple:", point)

print("Name:", point[0])

print("Country:", point[-1])

print("Language:", point[2])

print(point[0:2])

print(point[1:])

print(point[::-1])

N, A, L, C = point

print("Name: ", N)

print("Age: ", A)

print("Language: ", L)

print("Country: ", C)

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("first: ", first)

print("middle: ", *middle)

print("last: ", last)

single = (100, )

print(single)

print(type(single))

# single.append(20)

a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)

#this is also true because python may use same immutable objects when it can safely do so 
print(a is b)

#Namedtuples:

Person = namedtuple('Person', ['name', 'age', 'city', 'profession'])

person = Person("Ahmad", 25, "Lahore", "Python Developer")

print(person)

print("Name: ", person.name)

print("Age: ", person.age)

print("City:", person.city)

print("Profession: ", person.profession)

print("Name: ", person[0])

print("Age: ", person[1])

print("City:", person[2])

print("Profession: ", person[3])

print(type(person))

print(isinstance(person, tuple))

#person.age = 26

print(person)