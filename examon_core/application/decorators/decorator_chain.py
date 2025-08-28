from typing import List, Optional

from examon_core.entities import Question
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol


class DecoratorChain(QuestionDecoratorProtocol):
    def __init__(
        self, decorators: Optional[List[QuestionDecoratorProtocol]] = None
    ) -> None:
        self.decorators: List[QuestionDecoratorProtocol] = (
            [] if decorators is None else decorators
        )

    def decorate(self, question: Question) -> Question:
        for decorator in self.decorators:
            question = decorator.decorate(question)
        return question
