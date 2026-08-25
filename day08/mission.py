
# Day 8 Agentic Mission

from functools import partial

import time

from functools import reduce

### A compose(*fns) utility using functools.reduce

# Add one to the input value.
def add_one(x):
    return x + 1


# Multiply the input value by two.
def double(x):
    return x * 2


# Multiply the input value by itself.
def square(x):
    return x * x


# Combine several functions into one function.
def compose(*fns):

    def composed(x):
        # Pass each result to the next function from left to right.
        return reduce(lambda x, fn: fn(x), fns, x)

    return composed


# Apply add_one, double, square, and add_one in sequence.
f = compose(add_one, double, square, add_one)

# print(f(3))


###  A configurable rate-limiter using closures

# Create a function that limits how many calls are allowed in a time window.
def rate_limiter(max_calls, window):

    # These values are shared by all calls to the nested check function.
    count = 0
    start = time.time()

    def check():
        # nonlocal lets this function update the variables from rate_limiter.
        nonlocal count
        nonlocal start
        current = time.time()

        # Start a new window when the current one has expired.
        if current - start >= window:
            # print("Window Expired")
            count = 0
            start = current
            count += 1
            return "Allowed"
        else:
            # Block the call when the maximum number has already been reached.
            if count >= max_calls:
                return "Blocked"
            else:
                # Otherwise, record and allow the call.
                count += 1
                # print(count)
                return "Allowed"
    return check

# Allow two calls during each three-second window.
limiter  = rate_limiter(2, 3)

# Test the limiter with five consecutive calls.
# print(limiter())

# print(limiter())

# print(limiter())

# print(limiter())

# print(limiter())

### Partial-application pipeline that transforms a data record through multiple steps

# Add a field to the record and return the updated record.
def add_field(record, key, value):
    record[key] = value
    return record

# Mark the record as active.
def add_active(record, active):
    record["active"] = active
    return record

# Convert the record's name to uppercase.
def uppercase_name(record):
    record["name"] = record["name"].upper()
    return record

# Preconfigure add_active so it always sets active to True.
set_active = partial(add_active, active=True)

# Preconfigure add_field so it adds the developer role.
add_role = partial(
    add_field,
    key="role",
    value="developer"
)

record = {"name": "Ahmad"}

# Apply each transformation to the record in sequence.
def pipeline(record, *steps):

    for step in steps:
        # Pass the result of one step into the next step.
        record = step(record)

    return record

record = {"name": "Ahmad"}

# Run all three record transformations through the pipeline.
result = pipeline(
    record,
    add_role,
    set_active,
    uppercase_name
)

# print(result)

