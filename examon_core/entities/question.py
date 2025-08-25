from dataclasses import dataclass
from typing import Optional

from examon_core.entities.metrics import Metrics


@dataclass
class Question:
    function_src: Optional[str] = None
    unique_id: Optional[str] = None
    tags: Optional[list[str]] = None
    repository: Optional[str] = None
    hints: Optional[list[str]] = None
    print_logs: Optional[list[str]] = None
    correct_answer: Optional[str] = None
    choices: Optional[list[str]] = None
    metrics: Optional[Metrics] = None
    