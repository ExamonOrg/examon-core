import builtins
import io
from contextlib import redirect_stdout
from typing import Any, Optional

from examon_core.protocols.code_execution_protocol import CodeExecutionProtocol


class UnrestrictedDriver(CodeExecutionProtocol):
    def __init__(self) -> None:
        self.default_print = builtins.print

    def setup(self) -> None:
        builtins.print = self.default_print

    def teardown(self) -> None:
        builtins.print = self.default_print

    def execute(self, code: str) -> list[str]:
        logs = []

        def new_print(
            *args: object,
            sep: str = " ",
            end: str = "\n",
            file: Optional[Any] = None,
            flush: bool = False,
        ) -> None:
            f = io.StringIO()
            with redirect_stdout(f):
                self.default_print(*args, sep=sep, end=end, file=file, flush=flush)
            out = f.getvalue().rstrip()
            logs.append(out)
            return None

        # overriding all calls to print so that the output can be recorded
        builtins.print = new_print  # type: ignore[assignment]
        exec(code)
        return logs
