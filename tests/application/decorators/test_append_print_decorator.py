from examon_core.application.decorators import (
    AppendPrintDecorator,
)
from examon_core.entities import Question

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


class TestAppendPrintDecorator:
    def test_converts_function_with_print_decorator(self):
        result = AppendPrintDecorator().decorate(Question(function_src=simple_function))
        assert "print(function1())" in result.function_src

    def test_all(self):
        result = AppendPrintDecorator().decorate(
            Question(function_src=question_with_decorator_mutliline)
        )
        assert "print(question_with_decorator_mutliline())" in result.function_src
