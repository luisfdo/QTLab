from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from qtlab.domain.study.entities import Study
from qtlab.domain.study.status import StudyStatus
from qtlab.domain.study.value_objects import Observation

from .models import StudyModel


class SQLiteStudyRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, study: Study) -> None:
        model = StudyModel(
            id=study.id,
            observation=study.observation.text,
            status=study.status.value,
            created_at=study.created_at,
            updated_at=study.updated_at,
        )

        self._session.merge(model)
        self._session.commit()

    def get(self, study_id: UUID) -> Study | None:
        model = self._session.scalar(
            select(StudyModel).where(
                StudyModel.id == study_id
            )
        )

        if model is None:
            return None

        return Study(
            id=model.id,
            observation=Observation(
                text=model.observation,
                created_at=model.created_at,
            ),
            status=StudyStatus(model.status),
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
