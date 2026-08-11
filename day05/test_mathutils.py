from mathutils import add, is_even, divide

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False

def test_divide_wrong():
    assert divide(10, 2) == 6  # deliberately wrong — should be 5
