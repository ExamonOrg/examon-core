from typing import Protocol

from examon_core.entities.metrics import Metrics


class MetricsAnalysisProtocol(Protocol):
    def run(self, code: str) -> Metrics: ...
