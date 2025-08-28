import ast

from examon_core.application.analysis.code_analysis_visitor import (
    CodeAnalysisVisitor,
)
from examon_core.entities.metrics import Metrics
from examon_core.entities.question import Question
from examon_core.protocols import QuestionDecoratorProtocol


class MetricsDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if question.metrics is None:
            question.metrics = Metrics()

        if question.function_src == "":
            return question

        tree = ast.parse(question.function_src or "")
        m = CodeAnalysisVisitor()
        m.visit(tree)

        question.metrics.imports = list(m.modules)
        question.metrics.calls = list(m.calls)
        question.metrics.counts = m.counts

        return question
