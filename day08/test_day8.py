import time

from mission import rate_limiter

from mission import compose


# Test Rate Limitter

def test_rate_limiter_blocks_after_limit():
    # The limiter allows two calls, then blocks the third call.
    limiter = rate_limiter(2, 10)

    assert limiter() == "Allowed"
    assert limiter() == "Allowed"
    assert limiter() == "Blocked"

def test_rate_limiter_resets():
    # After the time window expires, the limiter allows calls again.
    limiter = rate_limiter(2, 0.01)

    assert limiter() == "Allowed"
    assert limiter() == "Allowed"
    assert limiter() == "Blocked"

    time.sleep(0.02)

    assert limiter() == "Allowed"

# Test Compose()

def add_one(x):
    # Increase the value by one for the composition test.
    return x + 1


def double(x):
    # Double the value for the composition test.
    return x * 2


def square(x):
    # Square the value for the composition test.
    return x * x


def test_compose():
    # Compose functions from right to left and verify the final result.
    f = compose(add_one, double, square)

    assert f(3) == 64

#Test pipeline

from mission import (
    add_role,
    set_active,
    uppercase_name,
    pipeline,
)


def test_pipeline():
    # Apply each record transformation in pipeline order.
    record = {"name": "Ahmad"}

    result = pipeline(
        record,
        add_role,
        set_active,
        uppercase_name,
    )

    assert result == {
        "name": "AHMAD",
        "role": "developer",
        "active": True,
    }