from examon_core.application.analysis.radon_metrics_analysis import RadonMetricsAnalysis
from examon_core.application.decorators.metrics_decorator import MetricsDecorator
from examon_core.entities.question import Question


class TestMetricsCollector:
    def test_analyzes_code(self, complex_code):
        metrics = (
            MetricsDecorator(RadonMetricsAnalysis())
            .decorate(Question(function_src=complex_code))
            .metrics
        )

        assert metrics.difficulty == 1.67
        assert metrics.no_of_functions == 1
        assert metrics.loc == 21
        assert metrics.lloc == 15
        assert metrics.sloc == 15
        assert metrics.imports.sort() == ["os", "sys"].sort()
        assert metrics.counts["Return"] == 4
        assert metrics.counts["Constant"] == 9
        assert metrics.counts["arg"] == 1
        assert metrics.counts["For"] == 1
        assert metrics.counts["Name"] == 11
        assert metrics.counts["Store"] == 2
        assert metrics.counts["Load"] == 9
        assert metrics.counts["If"] == 3
        assert metrics.counts["Compare"] == 3
        assert metrics.counts["Gt"] == 3
        assert metrics.counts["Assign"] == 1
        assert metrics.counts["BinOp"] == 2
        assert metrics.counts["Sub"] == 2
