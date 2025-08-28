from examon_core.entities import Metrics, Question
from examon_core.protocols import (
    QuestionDecoratorProtocol,
)


class DifficultyClassificationDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if question.metrics is not None:
            question.metrics.categorised_difficulty = self.__classify(question.metrics)

        return question

    def __classify(self, metrics: Metrics) -> str:
        value = metrics.difficulty
        if value is None:
            return "unknown"
        if value == 0:
            return "easy"
        if value <= 1:
            return "medium"
        if value < 3:
            return "hard"

        return "very_hard"
