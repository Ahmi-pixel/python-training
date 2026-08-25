import time

from mission import rate_limiter

from mission import compose

import pytest


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

def test_rate_limiter_closure():
    # A closure keeps the limiter configuration available after creation.
    limiter = rate_limiter(2, 3)

    # Inspect the captured values to confirm the limit and window are retained.
    captured_values = [
        cell.cell_contents
        for cell in limiter.__closure__
    ]

    assert 2 in captured_values
    assert 3 in captured_values

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
    # Apply the functions from left to right and verify the final result.
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

from mission import (
    add_one,
    double,
    square,
    compose,
)


# pytest.mark.parametrize lets one test run several times with different data.
# Each tuple below supplies an input value and the result expected for that input.
# This avoids writing a separate test function for every input value.
@pytest.mark.parametrize(
    # Check the same composed function with several input and expected values.
    "x, expected",
    [
        (1, 17),
        (2, 37),
        (3, 65),
        (5, 145),
    ],
)
def test_compose(x, expected):
    # The composed steps are add_one, double, square, then add_one.
    f = compose(add_one, double, square, add_one)

    # Each parameter pair verifies one complete composition result.
    assert f(x) == expected


