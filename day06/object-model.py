"""
Day 6: Python Object Model & Dynamic Typing
Demonstrates: aliasing, mutable default argument bug + fix, shallow vs deep copy.
"""

import copy


def add_item_buggy(item, my_list=[]):
    my_list.append(item)
    return my_list


def add_item_fixed(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


def demo_bug():
    a = add_item_buggy("a")
    b = add_item_buggy("b")
    assert a is b
    assert a == ["a", "b"]


def demo_fix():
    a = add_item_fixed("a")
    b = add_item_fixed("b")
    assert a is not b
    assert a == ["a"]
    assert b == ["b"]


def demo_aliasing():
    a = [1, 2, 3]
    b = a
    b.append(4)
    assert a == [1, 2, 3, 4]
    assert id(a) == id(b)


def demo_copy():
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    shallow[0].append(99)
    assert original == [[1, 2, 99], [3, 4]]
    assert deep == [[1, 2], [3, 4]]


if __name__ == "__main__":
    demo_bug()
    demo_fix()
    demo_aliasing()
    demo_copy()
    print("All Day 6 assertions passed.")