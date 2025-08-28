import pytest


@pytest.fixture
def print_logs_code():
    return """
def f1():
    print('hello')
    print('hello2')
    return 3
print(f1())
"""


@pytest.fixture
def complex_print_logs_code():
    return """
def f1():
    x = 0
    for a in [1, 2, 3]:
        x = x + a
        print(x)
    return x
print(f1())
    """


@pytest.fixture
def print_logs_with_params_code():
    return """
def f2(x):
    y = 5
    print(y)
    z = 9
    return y * 7 + x

print(f2(4))
"""


@pytest.fixture
def source_code():
    return """
def f2():
    y = 5
    z = 9
    for x in range(8):
        z = z + 8
    return y * 7

print(f2())
"""


@pytest.fixture
def lru_cache_source_code():
    return """
from functools import lru_cache

@lru_cache
def go():
    return 1
print(go())
"""


@pytest.fixture
def source_code_with_block():
    return """
def question_01():
    class LookingGlass:
        def __enter__(self):
            return 'enter'

        def __exit__(self, exc_type, exc_value, traceback):
            return 'exit'

    with LookingGlass() as what:
        return what
print(question_01())
"""


@pytest.fixture
def unpack_source_code():
    return """
def question_01():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    return latitude

print(question_01())
"""


@pytest.fixture
def splat_source_code():
    return """
def question():
    *rest, a, b = range(5)
    return rest[1]

print(question())
"""


@pytest.fixture
def classes_source_code():
    return """
def question():
    class A:
        pass

    return A()

print(question())
"""
