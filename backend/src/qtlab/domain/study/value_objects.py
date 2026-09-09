from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Observation:
    text: str
    created_at: datetime

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Observation cannot be empty.")
