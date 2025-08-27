from examon_core.application.decorators.decorator_chain import DecoratorChain
from examon_core.application.decorators.print_function_call import (
    PrintFunctionCall,
)
from examon_core.application.decorators.remove_wrapper_functions_decorator import (
    RemoveWrapperFunctionsDecorator,
)
from examon_core.entities.question import Question

simple_function = """
def function1():
    return 1 - 7
"""

question_with_decorator = """
@examon()
def function1():
    return 1 - 7
"""

question_with_decorator_mutliline = """
@examon_item(choices=["Hello, Bob. How are you?"], tags=["strings", "beginner"])
def question_with_decorator_mutliline():
    name = "Jeff"
    name = "Bob"
    greeting = f"Hello, {name}"
    greeting += ". How are you?"
    return greeting
"""


def instance():
    return DecoratorChain([RemoveWrapperFunctionsDecorator(), PrintFunctionCall()])


class TestFunctionSourceEnricher:
    def test_default_code_with_decorator_one_line(self):
        result = instance().decorate(Question(function_src=question_with_decorator))
        assert "@examon_item" not in result.function_src

    def test_default_code_with_decorator_multi_line(self):
        result = instance().decorate(
            Question(function_src=question_with_decorator_mutliline)
        )
        assert "@examon_item" not in result.function_src

    def test_default_code_as_string_factory(self):
        result = instance().decorate(Question(function_src=simple_function))
        assert "def function1():\n    return 1 - 7" in result.function_src

    def test_converts_function_to_string2(self):
        result = instance().decorate(Question(function_src=simple_function))
        assert "def function1():\n    return 1 - 7" in result.function_src

    def test_converts_function_with_print_decorator(self):
        decorator = PrintFunctionCall()
        result = DecoratorChain([decorator]).decorate(
            Question(function_src=simple_function)
        )
        assert "def function1():\n    return 1 - 7" in result.function_src
        assert "print(function1())" in result.function_src

    def test_all(self):
        result = instance().decorate(Question(function_src=question_with_decorator))
        assert "@examon" not in result.function_src
        assert "def function1():\n    return 1 - 7" in result.function_src
        assert "print(function1())" in result.function_src
