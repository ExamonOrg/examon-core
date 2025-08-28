from examon_core.application.decorators import (
    AppendPrintDecorator,
    ChoicesDecorator,
    DecoratorChain,
    DifficultyClassificationDecorator,
    MetricsDecorator,
    PrintLogsDecorator,
    RadonMetricsDecorator,
    RemoveWrapperFunctionsDecorator,
    UniqueIdDecorator,
)
from examon_core.application.execute.unrestricted_driver import (
    UnrestrictedDriver,
)


def default_instance() -> DecoratorChain:
    return DecoratorChain(
        [
            RemoveWrapperFunctionsDecorator(),
            AppendPrintDecorator(),
            PrintLogsDecorator(UnrestrictedDriver()),
            ChoicesDecorator(),
            MetricsDecorator(),
            RadonMetricsDecorator(),
            DifficultyClassificationDecorator(),
            UniqueIdDecorator(),
        ]
    )
