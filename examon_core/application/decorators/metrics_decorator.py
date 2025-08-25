import ast

from examon_core.application.analysis.code_analysis_visitor import (
    CodeAnalysisVisitor,
)
from examon_core.entities.metrics import Metrics
from examon_core.entities.question import Question
from examon_core.protocols import (
    MetricsAnalysisProtocol,
    QuestionDecoratorProtocol,
)


class MetricsDecorator(QuestionDecoratorProtocol):
    def __init__(self, analyser: MetricsAnalysisProtocol):
        self.analyser = analyser

    def decorate(self, question: Question) -> Question:
        metrics = Metrics()
        if question.function_src == "":
            return question

        metrics = self.analyser.run(question.function_src or "")

        tree = ast.parse(question.function_src or "")
        m = CodeAnalysisVisitor()
        m.visit(tree)

        metrics.imports = list(m.modules)
        metrics.calls = list(m.calls)
        metrics.counts = m.counts

        question.metrics = metrics

        return question
