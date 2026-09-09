from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .events import StudyCreated
from .status import StudyStatus
from .value_objects import Observation


@dataclass
class Study:
    id: UUID
    observation: Observation
    status: StudyStatus
    created_at: datetime
    updated_at: datetime
    timeline: list[StudyCreated] = field(default_factory=list)

    @classmethod
    def create(cls, observation: str) -> "Study":
        now = datetime.now(timezone.utc)
        study_id = uuid4()

        observation_value = Observation(
            text=observation,
            created_at=now,
        )

        study = cls(
            id=study_id,
            observation=observation_value,
            status=StudyStatus.UNDER_INVESTIGATION,
            created_at=now,
            updated_at=now,
        )

        study.timeline.append(
            StudyCreated(
                study_id=study_id,
                occurred_at=now,
            )
        )

        return study
