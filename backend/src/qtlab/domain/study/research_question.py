from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ResearchQuestion:
    text: str
    created_at: datetime

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Research question cannot be empty.")
