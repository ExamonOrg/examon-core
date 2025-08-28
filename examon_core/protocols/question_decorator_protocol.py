from typing import Protocol

from examon_core.entities import Question


class QuestionDecoratorProtocol(Protocol):
    def decorate(self, function: Question) -> Question: ...
