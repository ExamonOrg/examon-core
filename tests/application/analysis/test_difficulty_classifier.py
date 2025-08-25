
from examon_core.application.analysis.simple_difficulty_classifier import SimpleDifficultyClassifier
from examon_core.entities.metrics import Metrics

class TestSimpleDifficultyClassifier:
    def test_converts_function_to_string(self, code):
        metrics = Metrics(difficulty=2)

        assert SimpleDifficultyClassifier().run(metrics) == "hard"
