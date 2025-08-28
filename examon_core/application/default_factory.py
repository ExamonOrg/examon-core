from examon_core.application.decorators.choices_decorator import ChoicesDecorator
from examon_core.application.decorators.decorator_chain import (
    DecoratorChain,
)
from examon_core.application.decorators.difficulty_classification_decorator import (
    DifficultyClassificationDecorator,
)
from examon_core.application.decorators.metrics_decorator import MetricsDecorator
from examon_core.application.decorators.print_function_call_decorator import (
    PrintFunctionCallDecorator,
)
from examon_core.application.decorators.print_logs_decorator import PrintLogsDecorator
from examon_core.application.decorators.radon_metrics_decorator import (
    RadonMetricsDecorator,
)
from examon_core.application.decorators.remove_wrapper_functions_decorator import (
    RemoveWrapperFunctionsDecorator,
)
from examon_core.application.decorators.unique_id_decorator import UniqueIdDecorator
from examon_core.application.execute.unrestricted_driver import (
    UnrestrictedDriver,
)


def default_instance() -> DecoratorChain:
    return DecoratorChain(
        [
            RemoveWrapperFunctionsDecorator(),
            PrintFunctionCallDecorator(),
            PrintLogsDecorator(UnrestrictedDriver()),
            ChoicesDecorator(),
            MetricsDecorator(),
            RadonMetricsDecorator(),
            DifficultyClassificationDecorator(),
            UniqueIdDecorator(),
        ]
    )
