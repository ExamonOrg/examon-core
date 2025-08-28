from examon_core.application.decorators import RadonMetricsDecorator
from examon_core.entities import Question


class TestRadonMetricsDecorator:
    def test_analyzes_code(self, complex_code):
        metrics = (
            RadonMetricsDecorator()
            .decorate(Question(function_src=complex_code))
            .metrics
        )

        assert metrics.difficulty == 1.67
        assert metrics.no_of_functions == 1
        assert metrics.loc == 21
        assert metrics.lloc == 15
        assert metrics.sloc == 15
