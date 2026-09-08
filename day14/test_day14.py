import pytest
from day14.mission import retry, memoize, PluginMeta

def test_retry_times():
    calls = []
    @retry(times=3, delay=0)
    def unstable():
        calls.append(1)
        raise ValueError("failed")
    with pytest.raises(ValueError):
        unstable()

    assert len(calls) == 3

def test_metadata():
    @retry(times=3, delay=0)
    def deploy():
        """Deploy the application"""
        pass

    assert deploy.__name__ == "deploy"
    assert deploy.__doc__ == "Deploy the application"
    assert deploy.__wrapped__ is not None

def test_memoization_cache():
    calls = []

    @memoize
    def calculate(x):
        calls.append(1)
        return x * x

    assert calculate(10) == 100
    assert calculate(10) == 100
    assert len(calls) == 1

def test_register_classes():
    registry = {}
    def register(cls):
        registry[cls.__name__] = cls
        return cls

    @register
    class EmailPlugin:
        pass

    assert registry["EmailPlugin"] is EmailPlugin

def test_plugin_meta_registers_subclasses():
    class Plugin(metaclass=PluginMeta):
        pass

    class EmailPlugin(Plugin, metaclass=PluginMeta):
        pass

    class PaymentPlugin(Plugin, metaclass=PluginMeta):
        pass

    assert PluginMeta.registry["EmailPlugin"] is EmailPlugin
    assert PluginMeta.registry["PaymentPlugin"] is PaymentPlugin