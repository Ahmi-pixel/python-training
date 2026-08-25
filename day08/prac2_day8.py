

### LEGB Rule ###

# LEGB is the order Python uses when it looks for a variable name:
# Local, Enclosing, Global, and Built-in.

name = "Ahmad"

def greet():
    print(name)

greet()

# 1. Local: a variable created inside a function belongs to that function.

def greet():
    name = "Ahmad"
    print(name)

greet()

# This name is local to greet(), so it is not available outside the function.

# 2. Global: a variable created outside a function can be read inside it.

name = "Ahmad"

def greet():
    print(name)

greet()

# greet() has no local name, so Python finds the global name instead.

# 3. Built-in: Python already provides names such as these.

# print()
# len()
# type()
# sum()

# 4. Enclosing: an inner function can read a variable from its outer function.

# This creates a closure because inner remembers the name from outer.

def outer():
    name = "Pizza"

    def inner():
        print(name)

    inner()

outer()

name = "Global"

def show_name():
    # The local name hides the global name while this function runs.
    name = "Local"
    print(name)

show_name()
print(name)

def outer():
    # inner can use this enclosing variable.
    name = "Outer"

    def inner():
        print(name)

    inner()

outer()

# global lets a function change a variable defined outside that function.
score = 0

def add_score():
    global score
    for _ in range(3):
        score += 3
    print(score)
# This first version is kept as a reference but disabled to avoid duplicate output.
# add_score()

score = 0

def add_score():
    global score
    for _ in range(3):
        score += 10
        print(score)

add_score()    


def outer():
    # score belongs to outer, so inner needs nonlocal to change it.
    score = 0
    name = "Sam"

    def inner():
        nonlocal score
        for _ in range(3):
            score += 10

    return inner
counter = outer()
# This shorter closure example is kept for comparison but disabled because
# the next example shows the changing value more clearly.
# counter()

# __closure__ stores the values remembered by the inner function.
# print(counter.__closure__[1].cell_contents)

def outer():
    # These values are remembered after outer() has finished.
    score = 0
    name = "ahmad"

    def inner():
        # nonlocal changes the score stored in the enclosing function.
        nonlocal score
        score += 10
        print(score, name)

    return inner

counter = outer()

counter()
counter()
counter()

# Display the closure cells to see the remembered values.
print(counter.__closure__)
# Each cell contains one value captured from outer().
print(counter.__closure__[0].cell_contents)
print(counter.__closure__[1].cell_contents)

