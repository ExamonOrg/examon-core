from examon_core.application.decorators.print_function_call_decorator import (
    PrintFunctionCallDecorator,
)
from examon_core.entities.question import Question

simple_function = """
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


class TestPrintFunctionCallDecorator:
    def test_converts_function_with_print_decorator(self):
        result = PrintFunctionCallDecorator().decorate(
            Question(function_src=simple_function)
        )
        assert "print(function1())" in result.function_src

    def test_all(self):
        result = PrintFunctionCallDecorator().decorate(
            Question(function_src=question_with_decorator_mutliline)
        )
        assert "print(question_with_decorator_mutliline())" in result.function_src
