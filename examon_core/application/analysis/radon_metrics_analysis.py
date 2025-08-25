# mypy: ignore-errors
from radon.metrics import h_visit
from radon.raw import analyze  # type: ignore

from examon_core.entities.metrics import Metrics
from examon_core.protocols.metrics_analysis_protocol import MetricsAnalysisProtocol


class RadonMetricsAnalysis(MetricsAnalysisProtocol):
    def run(self, code: str) -> Metrics:
        raw = analyze(code)
        visit_data = h_visit(code)
        return Metrics(
            difficulty=round(visit_data.total.difficulty, 2),
            no_of_functions=len(visit_data.functions),
            loc=raw.loc,
            lloc=raw.lloc,
            sloc=raw.sloc,
        )
