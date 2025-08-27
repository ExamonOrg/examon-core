from examon_core.application.decorators.difficulty_classification_decorator import (
    DifficultyClassificationDecorator,
)
from examon_core.entities.metrics import Metrics
from examon_core.entities.question import Question


class TestSimpleDifficultyClassifier:
    def test_converts_function_to_string(self):
        question = Question(metrics=Metrics(difficulty=2))

        assert (
            DifficultyClassificationDecorator()
            .decorate(question)
            .metrics.categorised_difficulty
            == "hard"
        )
