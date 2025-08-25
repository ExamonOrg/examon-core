from examon_core.application.default_factory import default_instance
from examon_core.entities.question import Question


class TestQuestionProcessorExpectedResult:
    def test_build_print_logs(self, question_fn):
        question = default_instance().decorate(
            Question(function_src=question_fn, tags=["a"], hints=[])
        )
        assert question.print_logs == ["test", "7", "7"]

    def test_build_unique_id(self, question_fn):
        question = default_instance().decorate(
            Question(
                function_src=question_fn,
                tags=["a"],
                hints=[],
            )
        )
        for i in range(0, 10):
            assert question.unique_id == "15237805204168215635582438298174"
