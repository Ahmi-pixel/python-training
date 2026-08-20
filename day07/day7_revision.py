#importing collections
from collections import Counter

from collections import deque

from collections import defaultdict

#making a list for Counter
words = ["Python", "Python", "Django", "Python", "Django"]

counts = Counter(words)

print(counts)

#printing the count of Python in Words
print(counts["Python"])

#printing the most common word
print(counts.most_common(1))

#this will print 0, instead of throwing error
print(counts["Flask"])

#Deque

d = deque()

d.append("A")

print(d)

d.append("B")

d.append("C")

print(d)

#adding to the left
d.appendleft("URGENT")

print(d)

#popping from right
d.pop()

print(d)

d.popleft()

print(d)

#making a defuault dictionary
default = defaultdict(list)

default["A"].append("B")

default["A"].append("C")

default["B"].append("D")

print(default)

print(default["X"])

print(default)