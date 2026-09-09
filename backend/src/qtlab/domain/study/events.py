from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class StudyCreated:
    study_id: UUID
    occurred_at: datetime

TimelineEvent = StudyCreated
