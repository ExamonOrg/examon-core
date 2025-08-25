from examon_core.entities.question import Question
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol
from examon_core.protocols.unique_id_generation_protocol import (
    UniqueIdGenerationProtocol,
)


class UniqueIdDecorator(QuestionDecoratorProtocol):
    def __init__(self, unique_id_generator: UniqueIdGenerationProtocol):
        self.unique_id_generator = unique_id_generator

    def decorate(self, question: Question) -> Question:
        question.unique_id = self.unique_id_generator.run(question.function_src or "")

        return question
