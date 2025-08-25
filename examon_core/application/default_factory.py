from examon_core.application.analysis.metrics_analyser import MetricsAnalyser
from examon_core.application.analysis.radon_metrics_analysis import RadonMetricsAnalysis
from examon_core.application.analysis.simple_difficulty_classifier import (
    SimpleDifficultyClassifier,
)
from examon_core.application.decorators.choices_decorator import ChoicesDecorator
from examon_core.application.decorators.decorator_chain import (
    DecoratorChain,
)
from examon_core.application.decorators.difficulty_classification_decorator import (
    DifficultyClassificationDecorator,
)
from examon_core.application.decorators.metrics_decorator import MetricsDecorator
from examon_core.application.decorators.print_function_call import (
    PrintFunctionCall,
)
from examon_core.application.decorators.print_logs_decorator import PrintLogsDecorator
from examon_core.application.decorators.remove_python_decorators_decorator import (
    RemoveWrapperFunctionsDecorator,
)
from examon_core.application.decorators.unique_id_enricher import UniqueIdDecorator
from examon_core.application.execute.unrestricted_driver import (
    UnrestrictedDriver,
)
from examon_core.services.unique_id_generator import UniqueIdGenerator


def default_instance() -> DecoratorChain:
    return DecoratorChain(
        [
            ChoicesDecorator(),
            RemoveWrapperFunctionsDecorator(),
            PrintFunctionCall(),
            PrintLogsDecorator(UnrestrictedDriver()),
            MetricsDecorator(RadonMetricsAnalysis()),
            DifficultyClassificationDecorator(SimpleDifficultyClassifier()),
            UniqueIdDecorator(UniqueIdGenerator()),
        ]
    )
