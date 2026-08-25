

### Lambda:


import time

from functools import reduce

# A lambda is a small, unnamed function written on one line.
from functools import partial

# This lambda receives x and returns x multiplied by itself.

sqr = lambda x: x * x
# This lambda triples a number.

print(sqr(5))

# This second call is commented out to keep the output shorter.
# print(sqr(10))

# A lambda can also triple a number.
triple = lambda x: x * 3

# filter keeps only the values that make the condition True.
# print(triple(5))  # Commented out because the square example already demonstrates output.

numbers = [2, 5, 8, 11, 14, 17]

# reduce combines the items step by step: (((2 * 5) * 8) * 11).
print(list(map(lambda x: x * 3, numbers)))

n = (map(lambda x: x * 3, numbers))
# n is an iterator of squared numbers.

# Converting map to a list immediately stores all its results.
print(list(filter(lambda x: x > 30, n)))

# l is an iterator that will keep values greater than 10 from n.
numbers = [2, 5, 8, 11]

# reduce multiplies all numbers in the list into one final result.
print(reduce(lambda x, y: x * y, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    # Return base raised to the given exponent.

n = map(lambda x: x * x, numbers)
# partial fixes exponent at 2, creating a square function.

m = list(map(lambda x: x * x, numbers))

    # Build and return a student information dictionary.
l = filter(lambda x: x > 10, n)

q = list(filter(lambda x: x > 10, n))

# partial fills in role and active, leaving only name to provide later.
# q contains the filtered values; keep this print commented out to reduce duplicate output.
# print(q)

print(m)
    # These nested functions remember the value x from compose.

print(reduce(lambda x, y: x + y, q))

def power(base, exponent):
    return base ** exponent

sqr = partial(power, exponent = 2) 

print(sqr(5))
    # Return the functions so they can be called outside compose.

def dev(name, role, active):
    return {"name": name,
             "role": role, 
# f is a tuple containing three function objects.
             "active": active}

create = partial(dev, role = "Developer", active = True)
    # Each function receives a value and returns a new value.

print(create("Ahmad"))


def compose(x):
    # Accept any number of functions and combine them into one function.
    def add_one():
        # reduce passes each result into the next function in order.
        return x + 1

    def double():
        return x * 2

    def square():
        return x * x

    return add_one, square, double

    # Save the time when the timer is created.
f = compose(3)

print(f)

        # Return the number of seconds since test_timer was called.
def add_one(x):
    return x + 1

def double(x):
    return x * 2

# Calling t later measures the elapsed time.
def square(x):
    return x * x

p = add_one(3)
    # These variables belong to rate_limiter and persist between calls.

# These intermediate results are commented out because the final result is printed below.
# print(p)

q = double(p)
        # nonlocal allows check to update the outer variables.

# print(q)

l = square(q)
        # Reset the counter after the time window has ended.

# print(l)


def compose(*fns):

    def composed(x):
            # Block the call if the limit has already been reached.
        return reduce(lambda x, fn: fn(x), fns, x)

    return composed
                # Otherwise count this call and allow it.

f = compose(add_one, double, square, add_one)

# The composed function is the important result, so this call remains visible.
print(f(3))

def test_timer():

    start = time.time()
# Save the creation time so we can measure elapsed seconds later.

    def check():

        current = time.time()

        return current - start

    return check
# Wait long enough for the current window to expire.
t = test_timer()

print(t())

# print(t())

def rate_limiter(max_calls, window):

    # Keep track of calls made during the current time window.
    count = 0
    # Start the timer when the limiter is created.
    start = time.time()

    def check():
        # nonlocal allows this nested function to update the outer variables.
        nonlocal count
        nonlocal start
        current = time.time()

        # When the window ends, reset the counter and allow a new call.
        if current - start >= window:
            print("Window Expired")
            count = 0
            start = current
            count += 1
            return "Allowed"
        else:
            # Refuse the call after the maximum has been reached.
            if count >= max_calls:
                return "Blocked"
            else:
                # Count the call and allow it while the limit is available.
                count += 1
                print(count)
                return "Allowed"
    return check

# Allow two calls during every three-second window.
limiter  = rate_limiter(2, 3)

# The first two calls are allowed.
print(limiter())
print(limiter())
# This call is blocked because the limit of two has been reached.
print(limiter())
# These extra calls are commented out to avoid repeating the same "Blocked" output.
# print(limiter())
# print(limiter())

# Wait four seconds so the limiter's three-second window expires.
time.sleep(4)

# A new window has started, so this call is allowed again.
print(limiter())

