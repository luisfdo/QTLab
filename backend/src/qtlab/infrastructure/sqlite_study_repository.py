from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from qtlab.domain.study.entities import Study
from qtlab.domain.study.events import StudyCreated
from qtlab.domain.study.research_question import ResearchQuestion
from qtlab.domain.study.status import StudyStatus
from qtlab.domain.study.value_objects import Observation

from .models import StudyModel, StudyEventModel
from ..domain.study.events import ResearchQuestionDefined


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

        self._session.query(StudyEventModel).filter(
            StudyEventModel.study_id == study.id
        ).delete()

        for event in study.timeline:
            self._session.add(
                StudyEventModel(
                    study_id=study.id,
                    event_type=type(event).__name__,
                    occurred_at=event.occurred_at,
                )
            )

        self._session.commit()

    def get(self, study_id: UUID) -> Study | None:
        model = self._session.scalar(
            select(StudyModel).where(
                StudyModel.id == study_id
            )
        )

        if model is None:
            return None

        return self._to_domain(model)

    def list(self) -> list[Study]:
        models = self._session.scalars(
            select(StudyModel).order_by(
                StudyModel.updated_at.desc()
            )
        ).all()

        return [
            self._to_domain(model)
            for model in models
        ]

    def _to_domain(self, model: StudyModel) -> Study:
        events = (
            self._session.query(StudyEventModel)
            .filter(
                StudyEventModel.study_id == model.id
            )
            .order_by(StudyEventModel.occurred_at)
            .all()
        )

        timeline = []

        for event in events:
            if event.event_type == "StudyCreated":
                timeline.append(
                    StudyCreated(
                        study_id=model.id,
                        occurred_at=event.occurred_at,
                    )
                )
            elif event.event_type == "ResearchQuestionDefined":
                timeline.append(
                    ResearchQuestionDefined(
                        study_id=model.id,
                        occurred_at=event.occurred_at,
                    )
                )

        research_question = (
            ResearchQuestion(
                text=model.research_question,
                created_at=model.created_at,
            )
            if model.research_question
            else None
        )

        return Study(
            id=model.id,
            observation=Observation(
                text=model.observation,
                created_at=model.created_at,
            ),
            research_question=research_question,
            status=StudyStatus(model.status),
            created_at=model.created_at,
            updated_at=model.updated_at,
            timeline=timeline,
        )