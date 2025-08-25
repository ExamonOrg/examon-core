from typing import Protocol

from examon_core.entities.metrics import Metrics


class DifficultyClassifierProtocol(Protocol):
    def run(self, code_metrics: Metrics) -> str: ...
