import ast

from examon_core.application.analysis.code_analysis_visitor import (
    CodeAnalysisVisitor,
)
from examon_core.entities.metrics import Metrics
from examon_core.protocols import (
    MetricsAnalysisProtocol,
)


class MetricsAnalyser:
    def __init__(
        self,
        collector: MetricsAnalysisProtocol,
    ) -> None:
        self.collector = collector

    def run(self, code: str) -> Metrics:
        metrics = Metrics()
        if code == "" or code is None:
            return Metrics()

        metrics = self.collector.run(code)
        tree = ast.parse(code)
        m = CodeAnalysisVisitor()
        m.visit(tree)

        metrics.imports = list(m.modules)
        metrics.calls = list(m.calls)
        metrics.counts = m.counts

        return metrics
