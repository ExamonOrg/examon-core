from examon_core.entities import Question
from examon_core.protocols import (
    QuestionDecoratorProtocol,
)


class ChoicesDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if not question.choices:
            question.choices = []

        if question.correct_answer and question.correct_answer not in question.choices:
            question.choices.append(question.correct_answer)

        return question
