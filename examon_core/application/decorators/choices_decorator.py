from examon_core.entities.question import Question
from examon_core.protocols import (
    QuestionDecoratorProtocol,
)


class ChoicesDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if not question.choices:
            question.choices = []

        return question
