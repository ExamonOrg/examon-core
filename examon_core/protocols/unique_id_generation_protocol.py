from typing import Protocol


class UniqueIdGenerationProtocol(Protocol):
    def run(self, function_src: str) -> str: ...
