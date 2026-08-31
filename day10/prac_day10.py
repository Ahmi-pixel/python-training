from pathlib import Path
from contextlib import suppress
from contextlib import contextmanager
import time
import sys


# What is issubclass()?

# This:

issubclass(ValueError, Exception)

# asks:

# Is ValueError a subclass of Exception?

# isinstance()

# Works with objects:

error = ValueError("Something went wrong")

print(isinstance(error, ValueError))
print(isinstance(error, Exception))

# Result:

# True
# True

# Because this object:

# error = ValueError(...)

# is a ValueError, and a ValueError is also an Exception.

# try / except

try:
    number = int("hello")
except ValueError:
    print("That wasn't a valid integer")

# Multiple except Blocks

# try:
#     number = int(input("Enter a number to divide by 10: "))
#     result = 10 / number

# except ValueError:
#     print("You must enter a number.")

# except ZeroDivisionError:
#     print("You cannot divide by zero.")

# else:
#     print(f"{result:.2f}")

#Examples:

def divide(a, b):
    try:
        result = a/b

    except ZeroDivisionError:
        print("Cannot divide by zero")

    else:
        return f"Division succeeded: {result:.2f}"

    finally:
        print("divide() completed")

# divide(2,3)
# divide(0,3)
# divide(5,0)
# divide(15,10)
print(divide(50.3,20))

class ParseError(Exception):
    pass

try:
    try:
        number = int("abc")

    except ValueError as exc:
        raise ParseError("Could not parse number.") from exc
except ParseError as error:
    print("Error: ", error)
    print("Cause: ", error.__cause__)
    print("Cause type: ", type(error.__cause__))

class ParseError(Exception):
    def __init__(self, message, line_no):
        super().__init__(message)
        self.message = message
        self.line_no = line_no

    def __str__(self):
        super().__str__()
        return f"Line no: {self.line_no}, {self.message}"
        
    

error = ParseError("Invalid date", 8)

print(error)
print(error.message)
print(error.line_no)

path = Path("does.txt")

print("Before")

with suppress(FileNotFoundError):
    path.unlink()

print("After")

@contextmanager
def demo():
    print("Entering")

    yield

    print("Exiting")

@contextmanager
def timer():
    start = time.time()

    yield

    end = time.time()

    print(f"Elapsed: {end - start:.4f} seconds")

@contextmanager
def database_connection():
    print("Opening Database")

    try:
        yield
    finally:
        print("Cleaned up!")

with timer():
    time.sleep(1)


with demo():
    print("Doing work")

# with database_connection():
#     print("Database connected!")
#     raise ValueError("Database error")


for path in sys.path:
    print(path)