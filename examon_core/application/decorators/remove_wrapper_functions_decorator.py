from examon_core.entities.question import Question
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol


class RemoveWrapperFunctionsDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if question.function_src is not None:
            idx = question.function_src.find("def")
            question.function_src = (
                question.function_src[idx:] if idx != -1 else question.function_src
            )
        return question
