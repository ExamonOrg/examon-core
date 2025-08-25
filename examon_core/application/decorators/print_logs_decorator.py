from examon_core.entities.question import Question
from examon_core.protocols import CodeExecutionProtocol
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol


class PrintLogsDecorator(QuestionDecoratorProtocol):
    def __init__(self, code_executor: CodeExecutionProtocol):
        self.code_executor = code_executor

    def decorate(self, question: Question) -> Question:
        if question.function_src is None or question.function_src == "":
            return question
        question.print_logs = self.__execute(question.function_src)
        answer = question.print_logs[-1]
        question.correct_answer = answer
        return question

    def __execute(self, code: str) -> list[str]:
        try:
            self.code_executor.setup()
            return self.code_executor.execute(code)
        finally:
            self.code_executor.teardown()
