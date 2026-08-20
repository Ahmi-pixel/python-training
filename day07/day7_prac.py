# ==========================================
# DAY 7 — BUILT-IN DATA STRUCTURES
# ==========================================


# ==========================================
# 1. LISTS
# ==========================================

numbers = [10, 20, 30, 40, 50]

print(numbers)

#index access O(1)
print(numbers[0])

print(numbers[2])

print(numbers[-1])

print(numbers[-2])

#append O(1) amortized
numbers.append(60)

print(numbers)

#insert from begining O(n)
numbers.insert(0, 5)

print(numbers)

#pop from end O(1), from begining O(n)
removed = numbers.pop()

print(numbers)

print(removed)

# remove O(n)
numbers.remove(30)

print(numbers)

#slicing O(k)
print(numbers[1:4])

print(numbers[0:3])

print(numbers[2:])

print(numbers[::2])

print(numbers[::-1])

slice = numbers[::-1]

print(slice)

print(numbers)

print(slice is numbers)

#i tried to try something new and appended a variable in sliced list :)
slice.append(removed)

print(slice)

print(slice, numbers)

#membership test O(n)
print(30 in numbers)

print(100 in numbers)

print(100 not in numbers)
