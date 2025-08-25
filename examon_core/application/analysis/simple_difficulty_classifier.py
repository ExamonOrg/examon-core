from examon_core.entities.metrics import Metrics
from examon_core.protocols.difficulty_classifier_protocol import (
    DifficultyClassifierProtocol,
)


class SimpleDifficultyClassifier(DifficultyClassifierProtocol):
    def run(self, metrics: Metrics) -> str:
        value = metrics.difficulty
        if value is None:
            return "unknown"
        if value == 0:
            return "easy"
        elif value <= 1:
            return "medium"
        elif value < 3:
            return "hard"
        else:
            return "very_hard"
