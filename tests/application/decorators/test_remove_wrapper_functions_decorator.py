from examon_core.application.decorators.remove_wrapper_functions_decorator import (
    RemoveWrapperFunctionsDecorator,
)
from examon_core.entities.question import Question


class TestRemoveWrapperFunctionsDecorator:
    def test_converts_function_to_string(self, function_src_with_decorator):
        question = Question(function_src=function_src_with_decorator)

        assert (
            RemoveWrapperFunctionsDecorator().decorate(question).function_src
            == "def a():\n    return 6\n"
        )
