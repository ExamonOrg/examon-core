import hashlib

from examon_core.entities import Question
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol


class UniqueIdDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        question.unique_id = self.__generate(question)

        return question

    def __generate(self, question: Question) -> str | None:
        if not question.function_src:
            return None

        m = hashlib.md5()
        m.update(question.function_src.encode())
        return str(int(m.hexdigest(), 16))[0:32]
