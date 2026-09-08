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




def memoize(function):

    cached_function = lru_cache(maxsize=None)(function)
    @wraps(function)
    def wrapper(*args, **kwargs):
        return cached_function(*args, **kwargs)
    return wrapper

@memoize
def calculate(x):
    return x * x



class PluginMeta(type):
    
    registry = {}
    
    def __new__(mcls, name, bases, namespace):

        print("Before creating class")

        cls = super().__new__(mcls, name, bases, namespace)

        if bases:

            mcls.registry[name] = cls

        print("Class created:", cls)

        return cls

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

print(plugin_class)
print(type(plugin_class))

plugin = plugin_class()

print(plugin)
print(type(plugin))