from radon.metrics import h_visit  # type: ignore
from radon.raw import analyze  # type: ignore

from examon_core.entities.metrics import Metrics
from examon_core.entities.question import Question
from examon_core.protocols import QuestionDecoratorProtocol


class RadonMetricsDecorator(QuestionDecoratorProtocol):
    def decorate(self, question: Question) -> Question:
        if question.metrics is None:
            question.metrics = Metrics()
        raw = analyze(question.function_src)
        visit_data = h_visit(question.function_src)
        question.metrics.difficulty = round(visit_data.total.difficulty, 2)
        question.metrics.no_of_functions = len(visit_data.functions)
        question.metrics.loc = raw.loc
        question.metrics.lloc = raw.lloc
        question.metrics.sloc = raw.sloc

        return question
