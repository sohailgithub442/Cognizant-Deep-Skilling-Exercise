import pytest

# -------------------------
# Calculator Functions
# -------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# -------------------------
# Fixture
# -------------------------

@pytest.fixture
def numbers():
    return 20, 10


# -------------------------
# Test Cases (11 Tests)
# -------------------------

def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 30


def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == 10


def test_multiply(numbers):
    a, b = numbers
    assert multiply(a, b) == 200


def test_divide(numbers):
    a, b = numbers
    assert divide(a, b) == 2


def test_add_negative():
    assert add(-5, -5) == -10


def test_subtract_negative():
    assert subtract(-5, -3) == -2


def test_multiply_zero():
    assert multiply(10, 0) == 0


def test_divide_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_add_zero():
    assert add(0, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 5) == -10
