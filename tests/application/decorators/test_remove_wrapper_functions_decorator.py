from examon_core.application.decorators import RemoveWrapperFunctionsDecorator
from examon_core.entities import Question


class TestRemoveWrapperFunctionsDecorator:
    def test_converts_function_to_string(self, function_src_with_decorator):
        question = Question(function_src=function_src_with_decorator)

        assert (
            RemoveWrapperFunctionsDecorator().decorate(question).function_src
            == "def a():\n    return 6\n"
        )
