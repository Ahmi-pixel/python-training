

### Lambda:

from functools import reduce

from functools import partial


sqr = lambda x: x * x

print(sqr(5))

print(sqr(10))

triple = lambda x: x * 3

print(triple(5))

numbers = [2, 5, 8, 11, 14, 17]

print(list(map(lambda x: x * 3, numbers)))

n = (map(lambda x: x * 3, numbers))

print(list(filter(lambda x: x > 30, n)))

numbers = [2, 5, 8, 11]

print(reduce(lambda x, y: x * y, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

n = map(lambda x: x * x, numbers)

m = list(map(lambda x: x * x, numbers))

l = filter(lambda x: x > 10, n)

q = list(filter(lambda x: x > 10, n))

print(q)

print(m)

print(reduce(lambda x, y: x + y, q))

def power(base, exponent):
    return base ** exponent

sqr = partial(power, exponent = 2) 

print(sqr(5))

def dev(name, role, active):
    return {"name": name,
             "role": role, 
             "active": active}

create = partial(dev, role = "Developer", active = True)

print(create("Ahmad"))


# def compose(x):
#     def add_one():
#         return x + 1

#     def double():
#         return x * 2

#     def square():
#         return x * x

#     return add_one, square, double

# f = compose(3)

# print(f)

def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x * x

# p = add_one(3)

# print(p)

# q = double(p)

# print(q)

# l = square(q)

# print(l)

def compose(*fns):

    def composed(x):

        for n in fns:
            
            x = n(x)

        return x
        
    return composed
    
f = compose(add_one, double, square, add_one)

print(f(3))

result = reduce(lambda x, fn: fn(x), (add_one, double, square), 3)

print(result)