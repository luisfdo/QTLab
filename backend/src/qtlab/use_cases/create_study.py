from dataclasses import dataclass
from uuid import UUID

from qtlab.domain.study.entities import Study
from qtlab.domain.study.repository import StudyRepository


@dataclass(frozen=True)
class CreateStudyRequest:
    observation: str


class CreateStudy:
    def __init__(self, repository: StudyRepository) -> None:
        self._repository = repository

    def execute(self, request: CreateStudyRequest) -> UUID:
        study = Study.create(
            observation=request.observation,
        )

        self._repository.save(study)

        return study.id