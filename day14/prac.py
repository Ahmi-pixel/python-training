from functools import wraps
import time
from functools import lru_cache


def retry(times, delay):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempts in range(times):
                try:
                    print("Wrapper called.")
                    return function(*args, **kwargs)
                except:
                    if attempts == times - 1:
                        raise
                    else:
                        time.sleep(delay)
        return wrapper
    return decorator

@retry(times=4, delay=0.1)
def deploy(environment):
    """Deploying the application."""
    print(f"Deploying to {environment}")

# deploy("production")
# print(deploy.__name__)
# print(deploy.__doc__)
# print(deploy.__wrapped__)

def memoize(function):

    cached_function = lru_cache(maxsize=None)(function)
    @wraps(function)
    def wrapper(*args, **kwargs):
        return cached_function(*args, **kwargs)
    return wrapper

@memoize
def calculate(x):
    return x * x

# print(calculate(10))
# print(calculate(5))

# registry = {}

# def register(cls):
#     print("Creating class:", cls.__name__)
#     registry[cls.__name__] = cls
#     return cls

# @register
# class User:
#     pass
# @register
# class EmailPlugin:
#     pass
# @register
# class PaymentPlugin:
#     pass

# print(register)


class PluginMeta(type):
    
    registry = {}
    
    def __new__(mcls, name, bases, namespace):

        print("Before creating class")

        cls = super().__new__(mcls, name, bases, namespace)

        if bases:

            mcls.registry[name] = cls

        print("Class created:", cls)

        return cls

# class PluginMeta(type):

#     def __new__(mcls, name, bases, namespace):
#         print("META __new__:", name)

#         cls = super().__new__(mcls, name, bases, namespace)

#         print("META __new__ created:", cls)

#         return cls

#     def __init__(cls, name, bases, namespace):
#         print("META __init__:", name)

#         super().__init__(name, bases, namespace)

class Plugin(metaclass=PluginMeta):
    pass


class EmailPlugin(Plugin, metaclass=PluginMeta):
    pass


class PaymentPlugin(Plugin, metaclass=PluginMeta):
    pass


class SMSPlugin(Plugin, metaclass=PluginMeta):
    pass

# print(PluginMeta.registry)

plugin_class = PluginMeta.registry["EmailPlugin"]

# print(plugin_class)
# print(type(plugin_class))

# plugin = plugin_class()

# print(plugin)
# print(type(plugin))


from contextlib import contextmanager

@contextmanager
def demo():
    print("START")
    try:
        yield
    finally:
        print("END")
    

with demo():
    print("WORK")
    # raise ValueError("Something went wrong")

from contextlib import ExitStack

files = ["day14/a.txt", "day14/b.txt"]

with ExitStack() as stack:
    opened_files = []

    for filename in files:
        file = stack.enter_context(open(filename))
        opened_files.append(file)

    for file in opened_files:
        print(file.read())