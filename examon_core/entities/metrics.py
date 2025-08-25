from dataclasses import dataclass
from typing import Optional


@dataclass
class Metrics:
    no_of_functions: Optional[int] = None
    loc: Optional[int] = None
    lloc: Optional[int] = None
    sloc: Optional[int] = None
    difficulty: Optional[float] = None
    categorised_difficulty: Optional[str] = None
    imports: Optional[list[str]] = None
    calls: Optional[list[str]] = None
    counts: Optional[dict[str, int]] = None
