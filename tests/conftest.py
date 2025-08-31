import pytest


@pytest.fixture
def function_src_with_decorator():
    return """
@decorator
def a():
    return 6
"""


@pytest.fixture
def very_complex_code():
    return """
import sys, os
print(9)
o = {'e': 9}
x = [1,(1,2,3)]
a, b, c = 1, 2, 3
e = dict()
for a in range(7):
    ...

del o['e']
def fun_a():
    def fun_b():
        def fun_c():
            return 5
        return 5

    try:
        x = 1; y = 2
    except:
        ...
    print('hi')
    count = range(5)
    if 3 < len([1,2,3,4,5,6,7]):
        x = 8

    if False:
        def fun_d():
            ...
    else:
        ...
    return x + y
len([1,2,3])
class Parent:
    def __init__(self):
        self.value = 4

class Child(Parent):
    def __init__(self):
        self.value = 5

child = Child()
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()

"""


@pytest.fixture
def many_prints():
    return """
def function1():
    print("1")
    print("2")
    print("3")
    return "4"
print(function1())
"""


@pytest.fixture
def complex_code():
    return """
import os, sys

def function1():

    def function2():
        return 44

    def function3(n):
        for i in range(10):
            if n > 55:
                n = n - 1
        if n > 55:
            if n > 66:
                return 34
        else:
            return 55

    return function3(104) - function2()

print(function1())
"""


@pytest.fixture
def code():
    return """
def function1():
    def function2():
        return 44

    def function3(n):
        for i in range(10):
            if n > 55:
                n = n - 1
        if n > 55:
            if n > 66:
                return 34
        else:
            return 55

    return function3(104) - function2()

print(function1())
"""


@pytest.fixture
def question_fn():
    return """
def question_fn():
    print("test")
    answer = 4 + 3
    print(answer)
    return answer
"""
