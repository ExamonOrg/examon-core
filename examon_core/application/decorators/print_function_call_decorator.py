import re
from typing import Optional

from examon_core.entities.question import Question
from examon_core.protocols.question_decorator_protocol import QuestionDecoratorProtocol


class PrintFunctionCallDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if question.function_src is not None:
            function_name = self.__function_name(question.function_src)
            println = f"\n\nprint({function_name}())" if function_name else ""
            question.function_src = question.function_src + println
        return question

    def __function_name(self, function_src: str) -> Optional[str]:
        # todo get this from ast
        match = re.search(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", function_src)
        if match:
            return match.group(1)
        return None
