from typing import Callable, Optional


def examon(
    internal_id: Optional[str] = None,
    choices: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
    hints: Optional[list[str]] = None,
    repository: Optional[str] = None,
    version: Optional[str] = None,
) -> Callable[[Callable[..., object]], Callable[..., object]]:
    def inner_function(function: Callable[..., object]) -> Callable[..., object]:
        return function

    return inner_function
