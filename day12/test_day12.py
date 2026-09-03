from day12.mission import Matrix, Product
import pytest


def test_matrix_addition():
    a = Matrix([
        [1, 2],
        [3, 4]
    ])

    b = Matrix([
        [5, 6],
        [7, 8]
    ])

    result = a + b

    assert result.data == [
        [6, 8],
        [10, 12]
    ]

    assert a.data == [
        [1, 2],
        [3, 4]
    ]

    assert b.data == [
        [5, 6],
        [7, 8]
    ]

def test_matrix_multiplication():
    a = Matrix([
        [1, 2],
        [3, 4]
    ])

    b = Matrix([
        [5, 6],
        [7, 8]
    ])

    result = a * b

    assert result.data == [
        [5, 12],
        [21, 32]
    ]

def test_matrix_indexing():
    matrix = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    assert matrix[0] == [1, 2]
    assert matrix[2] == [5, 6]

def test_matrix_length():
    matrix = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    assert len(matrix) == 3

def test_matrix_iteration():
    matrix = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    rows = list(matrix)

    assert rows == [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

def test_product_is_hashable():
    product = Product("Laptop", 1200)

    assert isinstance(hash(product), int)


def test_product_rejects_negative_price():
    with pytest.raises(ValueError):
        Product("Laptop", -1)