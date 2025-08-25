from examon_core.entities.question import Question
from examon_core.protocols import (
    DifficultyClassifierProtocol,
    QuestionDecoratorProtocol,
)


class DifficultyClassificationDecorator(QuestionDecoratorProtocol):
    def __init__(self, difficulty_classifier: DifficultyClassifierProtocol):
        self.difficulty_classifier = difficulty_classifier

    def decorate(self, question: Question) -> Question:
        if question.metrics is not None:
            question.metrics.categorised_difficulty = self.difficulty_classifier.run(
                question.metrics
            )

        return question
