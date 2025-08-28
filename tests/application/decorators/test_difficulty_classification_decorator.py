from examon_core.application.decorators import DifficultyClassificationDecorator
from examon_core.entities import Metrics, Question


class TestDifficultyClassificationDecorator:
    def test_converts_function_to_string(self):
        question = Question(metrics=Metrics(difficulty=2))

        assert (
            DifficultyClassificationDecorator()
            .decorate(question)
            .metrics.categorised_difficulty
            == "hard"
        )
