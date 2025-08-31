from examon_core.application.decorators.print_logs_decorator import PrintLogsDecorator
from examon_core.application.execute.unrestricted_driver import UnrestrictedDriver
from examon_core.entities import Question


class TestChoicesDecorator:
    def test_analyzes_code(self, many_prints):
        result = PrintLogsDecorator(UnrestrictedDriver()).decorate(
            Question(function_src=many_prints)
        )
        assert result.print_logs == ["1", "2", "3", "4"]
