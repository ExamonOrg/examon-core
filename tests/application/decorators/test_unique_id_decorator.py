from examon_core.application.decorators.unique_id_decorator import (
    UniqueIdDecorator,
)
from examon_core.entities.question import Question


class TestDifficultyClassificationDecorator:
    def test_converts_function_to_string(self, complex_code):
        question = Question(function_src=complex_code)

        assert (
            UniqueIdDecorator().decorate(question).unique_id
            == "15521195969649415002899363404397"
        )
